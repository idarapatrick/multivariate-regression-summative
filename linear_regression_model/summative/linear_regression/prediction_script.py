import joblib
import numpy as np
import pandas as pd

def load_model():
    """Load the saved best model"""
    try:
        model_data = joblib.load('best_hypertension_model.pkl')
        return model_data
    except FileNotFoundError:
        print("Model file not found. Please run model_comparison.py first.")
        return None

def age_to_group(age):
    """Convert numeric age to age group string"""
    if 30 <= age <= 34:
        return '30-34'
    elif 35 <= age <= 39:
        return '35-39'
    elif 40 <= age <= 44:
        return '40-44'
    elif 45 <= age <= 49:
        return '45-49'
    elif 50 <= age <= 54:
        return '50-54'
    elif 55 <= age <= 59:
        return '55-59'
    elif 60 <= age <= 64:
        return '60-64'
    elif 65 <= age <= 69:
        return '65-69'
    elif 70 <= age <= 74:
        return '70-74'
    elif 75 <= age <= 79:
        return '75-79'
    elif age >= 80:
        return '80+'
    else:
        return None

def age_to_encoded(age):
    """Convert numeric age to encoded value for model"""
    age_mapping_ordinal = {
        '30-34': 0, '35-39': 1, '40-44': 2, '45-49': 3, '50-54': 4,
        '55-59': 5, '60-64': 6, '65-69': 7, '70-74': 8, '75-79': 9, '80+': 10
    }
    age_group = age_to_group(age)
    if age_group:
        return age_mapping_ordinal[age_group]
    else:
        return None

def validate_inputs(age, sex, country, year):
    """Validate input parameters"""
    errors = []
    
    # Check age
    if age < 30:
        errors.append(f"Age {age} is below minimum supported age (30)")
    elif age > 100:
        errors.append(f"Age {age} is above maximum supported age (100)")
    
    # Check sex
    if sex.lower() not in ['male', 'female', 'men', 'women']:
        errors.append(f"Invalid sex: {sex}. Use 'male'/'female' or 'men'/'women'")
    
    # Check year
    if year < 1990 or year > 2030:
        errors.append(f"Year {year} is outside supported range (1990-2030)")
    
    return errors

def make_prediction(age, sex, country, year):
    """
    Make prediction using the best trained model
    
    Parameters:
    - age: int (30-100)
    - sex: str ('male'/'female' or 'men'/'women')
    - country: str (country name)
    - year: int (1990-2030)
    
    Returns:
    - dict with prediction results
    """
    # Load model
    model_data = load_model()
    if model_data is None:
        return {"error": "Model not found"}
    
    # Validate inputs
    errors = validate_inputs(age, sex, country, year)
    if errors:
        return {"error": "Validation failed", "details": errors}
    
    try:
        # Extract model components
        model = model_data['model']
        scaler = model_data['scaler']
        feature_names = model_data['feature_names']
        model_name = model_data['model_name']
        
        # Convert age to encoded value
        age_encoded = age_to_encoded(age)
        if age_encoded is None:
            return {"error": f"Age {age} is outside the supported range (30-80+)"}
        
        # Convert sex to binary
        sex_binary = 0 if sex.lower() in ['male', 'men'] else 1
        
        # Create feature vector
        # Note: This is a simplified version. In practice, you'd need to handle country encoding
        # For now, we'll use a placeholder approach
        features = np.zeros(len(feature_names))
        
        # Set the features we know
        if 'Sex_binary' in feature_names:
            features[feature_names.index('Sex_binary')] = sex_binary
        if 'Age_encoded' in feature_names:
            features[feature_names.index('Age_encoded')] = age_encoded
        if 'Year' in feature_names:
            features[feature_names.index('Year')] = year
        
        # Reshape for prediction
        features = features.reshape(1, -1)
        
        # Scale features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        
        # Get age group
        age_group = age_to_group(age)
        
        return {
            "prediction": round(prediction, 2),
            "age_group": age_group,
            "model_used": model_name,
            "input_features": {
                "age": age,
                "age_group": age_group,
                "age_encoded": age_encoded,
                "sex": sex,
                "sex_binary": sex_binary,
                "country": country,
                "year": year
            }
        }
        
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}

def test_predictions():
    """Test the prediction function with various inputs"""
    print("Testing prediction function...")
    print("="*50)
    
    test_cases = [
        {"age": 40, "sex": "male", "country": "Nigeria", "year": 2020},
        {"age": 55, "sex": "female", "country": "South Africa", "year": 2020},
        {"age": 70, "sex": "male", "country": "Kenya", "year": 2020},
        {"age": 25, "sex": "female", "country": "Ghana", "year": 2020},  # Should show error
        {"age": 45, "sex": "invalid", "country": "Egypt", "year": 2020},  # Should show error
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input: {test_case}")
        
        result = make_prediction(**test_case)
        
        if "error" in result:
            print(f"❌ Error: {result['error']}")
        else:
            print(f"✅ Prediction: {result['prediction']}%")
            print(f"   Age Group: {result['age_group']}")
            print(f"   Model Used: {result['model_used']}")

def interactive_prediction():
    """Interactive prediction interface"""
    print("\n" + "="*50)
    print("HYPERTENSION PREVALENCE PREDICTION")
    print("="*50)
    
    while True:
        try:
            print("\nEnter prediction parameters (or 'quit' to exit):")
            
            age_input = input("Age (30-100): ").strip()
            if age_input.lower() == 'quit':
                break
            
            age = int(age_input)
            sex = input("Sex (male/female or men/women): ").strip()
            country = input("Country: ").strip()
            year = int(input("Year (1990-2030): ").strip())
            
            result = make_prediction(age, sex, country, year)
            
            if "error" in result:
                print(f"❌ Error: {result['error']}")
            else:
                print(f"\n✅ PREDICTION RESULTS:")
                print(f"   Hypertension Prevalence: {result['prediction']}%")
                print(f"   Age Group: {result['age_group']}")
                print(f"   Model Used: {result['model_used']}")
                
        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break

if __name__ == "__main__":
    # Test predictions
    test_predictions()
    
    # Interactive mode
    interactive_prediction() 