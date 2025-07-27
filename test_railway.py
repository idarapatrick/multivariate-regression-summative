import requests
import sys

def test_railway_deployment(base_url):
    """Test if the Railway deployment is working"""
    print(f"Testing Railway deployment at: {base_url}")
    
    try:
        # Test root endpoint
        response = requests.get(f"{base_url}/", timeout=10)
        print(f"✅ Root endpoint: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Test health endpoint
        response = requests.get(f"{base_url}/health", timeout=10)
        print(f"✅ Health endpoint: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Test prediction endpoint
        data = {
            "age": 35,
            "sex": "Men",
            "year": 2020,
            "country": "Nigeria"
        }
        response = requests.post(f"{base_url}/predict", json=data, timeout=10)
        print(f"✅ Prediction endpoint: {response.status_code}")
        print(f"Response: {response.json()}")
        
        print(f"\n🎉 Your API is working! Swagger UI: {base_url}/docs")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        print("Make sure you have the correct Railway URL")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        test_railway_deployment(url)
    else:
        print("Usage: python test_railway.py <your-railway-url>")
        print("Example: python test_railway.py https://my-app.railway.app") 