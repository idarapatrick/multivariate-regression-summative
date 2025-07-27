# Hypertension Risk Prediction for African Populations

## Project Overview

This project addresses a critical healthcare challenge facing African communities: the early detection and prevention of hypertension. Using machine learning techniques, I've developed predictive models to identify individuals at risk of hypertension before clinical diagnosis, enabling timely intervention and improved health outcomes.

## What This Project Does

The system analyzes demographic and geographic factors to predict hypertension risk across African populations. It combines statistical modeling with mobile technology to deliver personalized risk assessments, supporting healthcare workers in resource-limited settings.

## Key Components

### **Data Analysis & Modeling**
- **Dataset**: 4,135 records covering 54 African countries (2015-2021)
- **Features**: Age groups, sex, geographic location, and demographic factors
- **Models**: Linear regression, Random Forest, Decision Trees, and SGD regression
- **Performance**: Achieved 97% accuracy with Random Forest model

### **Mobile Application**
- **Platform**: Flutter app for Android 
- **Functionality**: Real-time hypertension risk assessment
- **User Interface**: Intuitive design for healthcare workers and patients

### **Web API**
- **Backend**: FastAPI-based prediction service with CORS middleware
- **Deployment**: Cloud-hosted at `https://prediction-api.up.railway.app`
- **Documentation**: Public Swagger UI at `https://prediction-api.up.railway.app/docs` with Pydantic validation
- **Integration**: RESTful API with comprehensive input validation

## Technical Architecture

The project follows a modular design with three main components:

1. **Data Processing Pipeline**: Handles data cleaning, feature engineering, and model training
2. **Prediction Engine**: Deployed API serving trained models
3. **User Interface**: Mobile application for risk assessment

## Data Source

Our analysis uses data from the **Non-Communicable Disease Risk Factor Collaboration (NCD-RisC)**, a global network of health scientists providing rigorous data on major non-communicable disease risk factors. The dataset includes comprehensive hypertension prevalence data across African populations, enabling region-specific risk modeling.

## Impact & Applications

This system addresses several critical healthcare challenges:

- **Early Detection**: Identifies high-risk individuals before clinical symptoms
- **Resource Optimization**: Helps healthcare workers prioritize screening efforts
- **Preventive Care**: Supports lifestyle intervention and monitoring programs
- **Regional Insights**: Provides country-specific risk patterns and trends

## Getting Started

### For Data Scientists
Navigate to `linear_regression_model/summative/linear_regression/` to access the Jupyter notebook containing the complete analysis pipeline.

### For Developers
The mobile application code is located in `linear_regression_model/summative/FlutterApp/regression_app/`.

### For API Users
The prediction API is documented in `linear_regression_model/summative/API/README.md`.

## Project Structure

```
Math-for-ML-Summative/
├── linear_regression_model/
│   ├── summative/
│   │   ├── linear_regression/     # Data analysis and modeling
│   │   ├── FlutterApp/           # Mobile application
│   │   └── API/                  # Web API service with prediction.py
│   └── hypertension_model.pkl    # Trained model
├── main.py                       # FastAPI application
└── requirements.txt              # Python dependencies
```

## Contributing

This project welcomes contributions from healthcare professionals, data scientists, and developers. Please review the specific README files in each component directory for detailed contribution guidelines.

## License

This project is developed for educational and healthcare improvement purposes. Please ensure compliance with local healthcare data regulations when deploying in clinical settings.
