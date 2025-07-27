from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
from contextlib import asynccontextmanager
import pickle
import os
import numpy as np
import pandas as pd
from typing import Optional

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events"""
    # Startup
    print("Starting Hypertension Prediction API...")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    
    success = load_model()
    if success:
        print("API startup completed successfully!")
    else:
        print("API startup failed - Model not loaded!")
        print("Warning: API may not function properly without the model.")
        print("Will attempt to load model on first prediction request...")
    
    yield
    
    # Shutdown
    print("Shutting down Hypertension Prediction API...")

# Create FastAPI app
app = FastAPI(
    title="Hypertension Prediction API",
    description="API for predicting hypertension prevalence in African countries",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Pydantic models for request/response
class PredictionRequest(BaseModel):
    model_config = {"protected_namespaces": ()}
    
    age: int = Field(..., ge=30, le=100, description="Age in years (30-100)")
    sex: str = Field(..., description="Sex: 'Men' or 'Women'")
    year: int = Field(..., ge=1990, le=2030, description="Year (1990-2030)")
    country: str = Field(..., min_length=2, max_length=100, description="Country name")
    
    @field_validator('sex')
    @classmethod
    def validate_sex(cls, v):
        if v.lower() not in ['men', 'women']:
            raise ValueError('Sex must be "Men" or "Women"')
        return v.title()  # Normalize to title case
    
    @field_validator('country')
    @classmethod
    def validate_country(cls, v):
        # List of valid African countries from the dataset
        valid_countries = [
            "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
            "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
            "Democratic Republic of the Congo", "Republic of the Congo", "Côte d'Ivoire",
            "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia",
            "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho",
            "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius",
            "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda",
            "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia",
            "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia",
            "Uganda", "Zambia", "Zimbabwe"
        ]
        if v.title() not in valid_countries:
            raise ValueError(f'Country must be one of the valid African countries: {", ".join(valid_countries[:10])}...')
        return v.title()

class PredictionResponse(BaseModel):
    model_config = {"protected_namespaces": ()}
    
    prediction: float = Field(..., description="Predicted hypertension prevalence")
    age_group: str = Field(..., description="Age group corresponding to the input age")
    message: str = Field(..., description="Human-readable message")
    model_used: str = Field(..., description="Name of the model used for prediction")

# Global variable to store loaded model
model_data = None

def load_model():
    """Load the trained model"""
    global model_data
    try:
        # Load model from current directory
        model_path = 'hypertension_model.pkl'
        
        # Check if file exists
        if not os.path.exists(model_path):
            print(f"Model file not found: {model_path}")
            print(f"Current working directory: {os.getcwd()}")
            print(f"Files in directory: {os.listdir('.')}")
            
            # Try alternative paths
            alternative_paths = [
                './hypertension_model.pkl',
                '../hypertension_model.pkl',
                '/app/hypertension_model.pkl',
                '/tmp/hypertension_model.pkl'
            ]
            
            for alt_path in alternative_paths:
                if os.path.exists(alt_path):
                    print(f"Found model at alternative path: {alt_path}")
                    model_path = alt_path
                    break
            else:
                print("Model file not found in any location")
                return False
        
        print(f"Loading model from: {os.path.abspath(model_path)}")
        
        with open(model_path, 'rb') as file:
            model_data = pickle.load(file)
        
        # Verify model data structure
        required_keys = ['model', 'scaler', 'feature_names', 'model_name', 'age_mapping', 'sex_mapping']
        missing_keys = [key for key in required_keys if key not in model_data]
        
        if missing_keys:
            print(f"Model data missing keys: {missing_keys}")
            return False
        
        print("Model loaded successfully!")
        print(f"Model name: {model_data['model_name']}")
        print(f"Features: {len(model_data['feature_names'])} features")
        return True
        
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def age_to_group(age: int) -> str:
    """Convert age to age group"""
    age_groups = {
        (30, 34): '30-34',
        (35, 39): '35-39',
        (40, 44): '40-44',
        (45, 49): '45-49',
        (50, 54): '50-54',
        (55, 59): '55-59',
        (60, 64): '60-64',
        (65, 69): '65-69',
        (70, 74): '70-74',
        (75, 79): '75-79',
        (80, 120): '80+'
    }
    
    for (min_age, max_age), group in age_groups.items():
        if min_age <= age <= max_age:
            return group
    return '30-34'  # Default fallback

def make_prediction(age: int, sex: str, year: int, country: str) -> dict:
    """Make prediction using the loaded model"""
    if model_data is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    try:
        model = model_data['model']
        scaler = model_data['scaler']
        feature_names = model_data['feature_names']
        model_name = model_data['model_name']
        age_mapping = model_data['age_mapping']
        sex_mapping = model_data['sex_mapping']
        
        # Convert age to age group
        age_group = age_to_group(age)
        
        # Encode inputs
        sex_encoded = sex_mapping[sex]
        age_encoded = age_mapping[age_group]
        
        # Create feature vector
        features = {}
        
        # Add basic features
        features['Year'] = year
        features['Sex_binary'] = sex_encoded
        features['Age_encoded'] = age_encoded
        
        # Add country features (one-hot encoded)
        for feature in feature_names:
            if feature.startswith('Country_'):
                country_name = feature.replace('Country_', '')
                features[feature] = 1 if country_name == country else 0
        
        # Create DataFrame
        input_df = pd.DataFrame([features])
        
        # Ensure all required features are present
        for feature in feature_names:
            if feature not in input_df.columns:
                input_df[feature] = 0
        
        # Reorder columns to match training data
        input_df = input_df[feature_names]
        
        # Scale features
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        return {
            'prediction': float(prediction),
            'age_group': age_group,
            'message': f"Predicted hypertension prevalence for {age}-year-old {sex.lower()} in {country} ({year}): {prediction:.4f}",
            'model_used': model_name
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {str(e)}")



@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Hypertension Prediction API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if model_data is not None else "unhealthy",
        "model_loaded": model_data is not None,
        "model_name": model_data['model_name'] if model_data else None,
        "model_features": len(model_data['feature_names']) if model_data else 0,
        "working_directory": os.getcwd(),
        "model_file_exists": os.path.exists('hypertension_model.pkl') if model_data else False
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict_hypertension(request: PredictionRequest):
    """
    Predict hypertension prevalence
    
    - **age**: Age in years (30-100)
    - **sex**: Sex ('Men' or 'Women')
    - **year**: Year (1990-2030)
    - **country**: Country name (must be a valid African country)
    """
    # Try to load model if not already loaded
    if model_data is None:
        print("🔄 Attempting to load model on demand...")
        if not load_model():
            raise HTTPException(status_code=500, detail="Model not loaded and could not be loaded")
    
    try:
        result = make_prediction(
            age=request.age,
            sex=request.sex,
            year=request.year,
            country=request.country
        )
        
        return PredictionResponse(**result)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/countries")
async def get_countries():
    """Get list of valid countries"""
    countries = [
        "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
        "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
        "Democratic Republic of the Congo", "Republic of the Congo", "Côte d'Ivoire",
        "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia",
        "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho",
        "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius",
        "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda",
        "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia",
        "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia",
        "Uganda", "Zambia", "Zimbabwe"
    ]
    return {"countries": countries}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)