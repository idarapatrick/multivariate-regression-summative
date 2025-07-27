import requests
import json

# Test the API endpoints
base_url = "http://localhost:8000"

def test_root():
    """Test root endpoint"""
    response = requests.get(f"{base_url}/")
    print("Root endpoint:", response.json())
    return response.status_code == 200

def test_health():
    """Test health endpoint"""
    response = requests.get(f"{base_url}/health")
    print("Health endpoint:", response.json())
    return response.status_code == 200

def test_countries():
    """Test countries endpoint"""
    response = requests.get(f"{base_url}/countries")
    print("Countries endpoint:", response.json())
    return response.status_code == 200

def test_prediction():
    """Test prediction endpoint"""
    data = {
        "age": 35,
        "sex": "Men",
        "year": 2020,
        "country": "Nigeria"
    }
    
    response = requests.post(
        f"{base_url}/predict",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data)
    )
    
    if response.status_code == 200:
        result = response.json()
        print("Prediction successful:", result)
        return True
    else:
        print("Prediction failed:", response.status_code, response.text)
        return False

if __name__ == "__main__":
    print("Testing Hypertension Prediction API...")
    print("=" * 50)
    
    # Test all endpoints
    tests = [
        ("Root", test_root),
        ("Health", test_health),
        ("Countries", test_countries),
        ("Prediction", test_prediction)
    ]
    
    for test_name, test_func in tests:
        print(f"\nTesting {test_name}...")
        success = test_func()
        status = "✅ PASS" if success else "FAIL"
        print(f"{test_name}: {status}")
    
    print("\n" + "=" * 50)
    print("API Testing Complete!") 