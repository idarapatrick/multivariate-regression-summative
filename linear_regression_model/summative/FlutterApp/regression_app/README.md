# Hypertension Prediction Flutter App

A Flutter application for predicting hypertension prevalence in African countries using machine learning models.

## Features

- **Input Validation**: Age, sex, year, and country selection with validation
- **API Integration**: Connects to the deployed FastAPI backend
- **Real-time Predictions**: Get hypertension prevalence predictions instantly
- **User-friendly Interface**: Clean, modern UI with Material Design 3

## Getting Started

1. **Install Flutter dependencies:**
   ```bash
   flutter pub get
   ```

2. **Run the app:**
   ```bash
   flutter run
   ```

## API Endpoint

The app connects to the deployed FastAPI backend at:
`https://prediction-api.up.railway.app`

## Supported Countries

All African countries including Nigeria, South Africa, Kenya, Ghana, Egypt, Ethiopia, and more.

## Input Requirements

- **Age**: 30-100 years
- **Sex**: Men or Women
- **Year**: 1990-2030
- **Country**: Select from available African countries
