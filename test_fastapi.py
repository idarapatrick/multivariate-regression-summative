from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Test the app
client = TestClient(app)
response = client.get("/")
print("FastAPI test successful!")
print(f"Response: {response.json()}") 