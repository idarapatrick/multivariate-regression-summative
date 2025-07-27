#!/usr/bin/env python3
"""
Local API Test Script
Run this to test your API locally before deployment
"""

import requests
import json

def test_local_api():
    """Test the API running locally"""
    base_url = "http://localhost:8000"
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health Check: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")
        return False
    
    # Test prediction endpoint
    test_data = {
        "age": 45,
        "sex": "Female",
        "year": 2024,
        "country": "Nigeria"
    }
    
    try:
        response = requests.post(
            f"{base_url}/predict",
            headers={"Content-Type": "application/json"},
            json=test_data
        )
        print(f"\nPrediction Test: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Success! Prediction: {result}")
            return True
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Prediction test failed: {e}")
        return False

def test_railway_api():
    """Test the Railway API"""
    base_url = "https://hypertension-prediction-api-production.up.railway.app"
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Railway Health Check: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Railway health check failed: {e}")
        return False
    
    # Test prediction endpoint
    test_data = {
        "age": 45,
        "sex": "Female",
        "year": 2024,
        "country": "Nigeria"
    }
    
    try:
        response = requests.post(
            f"{base_url}/predict",
            headers={"Content-Type": "application/json"},
            json=test_data
        )
        print(f"\nRailway Prediction Test: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Success! Prediction: {result}")
            return True
        else:
            print(f"Error: {response.text}")
            return False
    except Exception as e:
        print(f"Railway prediction test failed: {e}")
        return False

if __name__ == "__main__":
    print("=== API Testing ===")
    print("\n1. Testing Local API...")
    local_success = test_local_api()
    
    print("\n2. Testing Railway API...")
    railway_success = test_railway_api()
    
    print("\n=== Results ===")
    print(f"Local API: {'✅ Working' if local_success else '❌ Failed'}")
    print(f"Railway API: {'✅ Working' if railway_success else '❌ Failed'}")
    
    if not railway_success:
        print("\n🚨 Railway API is not working!")
        print("You need to redeploy your API to Railway or use a different hosting service.") 