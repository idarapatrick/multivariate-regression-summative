 # Prediction logic and model loading
import numpy as np
import pandas as pd


# Age mapping functions
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


def make_prediction(age, sex, country, year):
    """
    Main prediction function for the API
    """
    # Validate inputs
    errors = validate_prediction_input(age, sex, country, year)
    if errors:
        raise ValueError(f"Invalid inputs: {', '.join(errors)}")
    
    # Convert age to encoded value
    age_encoded = age_to_encoded(age)
    if age_encoded is None:
        raise ValueError(f"Age {age} is outside the supported range (30-80+)")
    
    # Convert sex to binary
    sex_binary = 0 if sex.lower() in ['male', 'men'] else 1
    
    # For now, use a simple placeholder prediction
    # In the future, you'll load your trained model here
    # model = load_model()  # You'll need to implement this
    # prediction = model.predict(input_data)[0]
    
    # Simple placeholder prediction based on age and sex
    base_risk = 20.0
    age_factor = age_encoded * 2.5  # Higher age = higher risk
    sex_factor = 5.0 if sex_binary == 1 else 0.0  # Women slightly higher risk
    
    prediction = base_risk + age_factor + sex_factor
    
    return round(prediction, 2)


# Validation function
def validate_prediction_input(age, sex, country, year):
    """Validate inputs before prediction"""
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

def encoded_to_age_group(encoded_value):
    """Convert encoded value back to age group"""
    age_order = ['30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']
    if 0 <= encoded_value < len(age_order):
        return age_order[encoded_value]
    else:
        return None

# Test the functions
print("Testing Age Mapping Functions:")
print("=" * 40)
test_ages = [33, 40, 55, 85, 13, 25]
for age in test_ages:
    age_group = age_to_group(age)
    encoded = age_to_encoded(age)
    print(f"Age {age} → Group: {age_group} → Encoded: {encoded}")