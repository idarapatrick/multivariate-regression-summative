# Hypertension Risk Prediction: Data Analysis & Modeling

## Mission Statement

My mission is to predict individual hypertension risk across African populations in order to support early intervention, guide personalized healthcare, and empower individuals to make informed decisions about their health, ultimately helping to reduce hypertension prevalence across the continent.

## Problem Context

Hypertension awareness remains critically low across African countries, with fewer than 20% of affected individuals aware of their condition in many sub-Saharan nations. This lack of awareness leads to missed opportunities for early intervention and preventive care. Our analysis addresses this challenge by developing predictive models that can identify high-risk individuals before clinical diagnosis.

## Dataset Overview

### Source
Data originates from the **Non-Communicable Disease Risk Factor Collaboration (NCD-RisC)**, a global network of health scientists providing rigorous data on major non-communicable disease risk factors.
[Link to Citation](https://ncdrisc.org/data-downloads-hypertension.html)

### Dataset Characteristics
- **Size**: 4,135 records
- **Geographic Coverage**: 54 African countries
- **Time Period**: 2015-2021
- **Data Quality**: No missing values, comprehensive coverage

### Key Variables
- **Demographic**: Age groups (30-34 to 80+), Sex (male/female)
- **Geographic**: Country, ISO codes
- **Temporal**: Year (2015-2021)
- **Health Metrics**: Hypertension prevalence, diagnosis rates, treatment rates

## Analysis Pipeline

### 1. Data Preprocessing
- **Filtering**: Focused on African countries from 2015 onwards
- **Feature Engineering**: Created binary encoding for categorical variables
- **Scaling**: Applied StandardScaler for numerical features
- **Validation**: Ensured data quality and consistency

### 2. Exploratory Data Analysis
- **Distribution Analysis**: Examined age group and prevalence distributions
- **Correlation Analysis**: Identified relationships between variables
- **Geographic Patterns**: Analyzed country-specific trends
- **Temporal Trends**: Investigated year-over-year changes

### 3. Model Development
Implemented multiple regression approaches:

#### Linear Regression (From Scratch)
- **Algorithm**: Gradient descent optimization
- **Performance**: R² = 0.9517, RMSE = 0.0394
- **Convergence**: Achieved at iteration 283

#### Scikit-learn Linear Regression
- **Performance**: R² = 0.9675, RMSE = 0.0323
- **Advantage**: Optimized implementation

#### Stochastic Gradient Descent
- **Performance**: R² = 0.9640, RMSE = 0.0340
- **Benefit**: Efficient for large datasets

#### Decision Tree Regressor
- **Performance**: R² = 0.9573, RMSE = 0.0370
- **Depth**: Limited to 10 levels to prevent overfitting

#### Random Forest Regressor
- **Performance**: R² = 0.9727, RMSE = 0.0296
- **Configuration**: 100 estimators, max depth 10
- **Status**: Best performing model

### 4. Model Evaluation
- **Metrics**: R² score, RMSE, MAE
- **Cross-validation**: Ensured model robustness
- **Feature Importance**: Identified key predictors

## Key Findings

### Geographic Patterns
- Significant variation in hypertension prevalence across African countries
- Regional clustering of risk factors
- Urban-rural differences in prevalence rates

### Demographic Insights
- Age-related risk increases consistent across regions
- Gender differences in prevalence patterns
- Interaction effects between age and geographic location

### Model Performance
- Random Forest achieved highest accuracy (97.27%)
- Linear models showed strong performance (95-96%)
- Consistent prediction accuracy across different age groups

## Technical Implementation

### Dependencies
- **Data Processing**: pandas, numpy
- **Machine Learning**: scikit-learn
- **Visualization**: matplotlib, seaborn
- **Model Persistence**: pickle

### File Structure
```
linear_regression/
├── multivariate.ipynb          # Main analysis notebook
├── model_comparison.py         # Model training and comparison
├── africa.csv                  # Filtered African dataset
├── hypertension_by_country.csv # Original dataset
└── hypertension_model.pkl      # Trained model
```

## Usage Instructions

### Running the Analysis
1. Ensure all dependencies are installed
2. Open `multivariate.ipynb` in Jupyter
3. Execute cells sequentially
4. Review visualizations and model outputs

### Making Predictions
```python
# For local predictions, use the prediction.py file in the API directory
# Example prediction
from linear_regression_model.summative.API.prediction import make_prediction

result = make_prediction(
    age=45,
    sex="male", 
    country="Nigeria",
    year=2023
)
```

## Model Deployment

The trained Random Forest model has been serialized and deployed via:
- **API Service**: FastAPI backend for web access
- **Mobile App**: Flutter application for field use
- **Local Scripts**: Python utilities for batch processing

## Validation & Testing

- **Data Validation**: Ensured data quality and consistency
- **Model Validation**: Cross-validation and holdout testing
- **Performance Testing**: Evaluated across different demographic groups
- **Edge Case Testing**: Handled missing or invalid inputs

## Future Enhancements

- **Additional Features**: Lifestyle factors, medical history
- **Real-time Updates**: Dynamic model retraining
- **Ensemble Methods**: Combining multiple model approaches
- **Interpretability**: SHAP values for feature importance

## References

- Ataklte, F., et al. (2015). Burden of undiagnosed hypertension in sub-Saharan Africa. *Hypertension*, 65(2), 291-298.
- Adeloye, D., et al. (2021). Prevalence, awareness, and control of hypertension in Nigeria. *Journal of Hypertension*, 39(4), 740-748.
- NCD-RisC. (2023). Data downloads: Hypertension. Retrieved from https://ncdrisc.org/data-downloads-hypertension.html 