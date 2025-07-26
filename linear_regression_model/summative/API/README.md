# Hypertension Prediction API

A FastAPI-based REST API for predicting hypertension prevalence in African countries using machine learning models.

## Features

- **Machine Learning Model**: Uses a Random Forest model trained on hypertension data from African countries
- **Input Validation**: Comprehensive data validation using Pydantic models
- **CORS Support**: Cross-Origin Resource Sharing enabled for web applications
- **Interactive Documentation**: Auto-generated Swagger UI documentation
- **Health Monitoring**: Built-in health check endpoints

## API Endpoints

### Base URL
- **Production**: `https://your-app-name.onrender.com`
- **Local Development**: `http://localhost:8000`

### Available Endpoints

1. **GET /** - Root endpoint
   - Returns API information and available endpoints

2. **GET /health** - Health check
   - Returns API status and model loading status

3. **GET /countries** - List valid countries
   - Returns list of supported African countries

4. **POST /predict** - Make prediction
   - Accepts: age, sex, year, country
   - Returns: prediction, age_group, message, model_used

5. **GET /docs** - Interactive API documentation
   - Swagger UI interface for testing endpoints

## Input Parameters

### Prediction Request
```json
{
  "age": 35,
  "sex": "Men",
  "year": 2020,
  "country": "Nigeria"
}
```

### Validation Rules
- **age**: Integer between 30-100
- **sex**: String ("Men" or "Women")
- **year**: Integer between 1990-2030
- **country**: String (must be a valid African country)

### Response Format
```json
{
  "prediction": 0.2345,
  "age_group": "35-39",
  "message": "Predicted hypertension prevalence for 35-year-old men in Nigeria (2020): 0.2345",
  "model_used": "Random Forest"
}
```

## Deployment

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Render Deployment
1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Select the repository and branch
4. Render will automatically detect the Python environment
5. The API will be available at your Render URL

### Environment Variables
- `PORT`: Automatically set by Render
- `PYTHON_VERSION`: Set to 3.9.16

## Model Information

- **Algorithm**: Random Forest Regressor
- **Training Data**: Hypertension prevalence data from African countries (2010-2019)
- **Features**: Age, Sex, Year, Country
- **Performance**: R² Score: 0.9727, RMSE: 0.0296

## Supported Countries

Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi, Cabo Verde, Cameroon, Central African Republic, Chad, Comoros, Democratic Republic of the Congo, Republic of the Congo, Côte d'Ivoire, Djibouti, Egypt, Equatorial Guinea, Eritrea, Eswatini, Ethiopia, Gabon, Gambia, Ghana, Guinea, Guinea-Bissau, Kenya, Lesotho, Liberia, Libya, Madagascar, Malawi, Mali, Mauritania, Mauritius, Morocco, Mozambique, Namibia, Niger, Nigeria, Rwanda, Sao Tome and Principe, Senegal, Seychelles, Sierra Leone, Somalia, South Africa, South Sudan, Sudan, Tanzania, Togo, Tunisia, Uganda, Zambia, Zimbabwe

## Testing

Use the interactive documentation at `/docs` to test the API endpoints, or use the provided test script:

```bash
python test_api.py
```

## License

This project is part of a machine learning course assignment. 