#!/usr/bin/env python3
"""
Test script to verify model loading
"""

import os
import pickle
import sys

def test_model_loading():
    """Test if the model can be loaded correctly"""
    print("🧪 Testing Model Loading...")
    print(f"📂 Current directory: {os.getcwd()}")
    print(f"📁 Files: {os.listdir('.')}")
    
    model_path = 'hypertension_model.pkl'
    
    if not os.path.exists(model_path):
        print(f"❌ Model file not found: {model_path}")
        return False
    
    try:
        print(f"📁 Loading model from: {os.path.abspath(model_path)}")
        
        with open(model_path, 'rb') as file:
            model_data = pickle.load(file)
        
        # Check required keys
        required_keys = ['model', 'scaler', 'feature_names', 'model_name', 'age_mapping', 'sex_mapping']
        missing_keys = [key for key in required_keys if key not in model_data]
        
        if missing_keys:
            print(f"❌ Missing keys: {missing_keys}")
            return False
        
        print("✅ Model loaded successfully!")
        print(f"📊 Model name: {model_data['model_name']}")
        print(f"🔧 Features: {len(model_data['feature_names'])} features")
        print(f"👥 Sex mapping: {model_data['sex_mapping']}")
        print(f"📅 Age mapping: {model_data['age_mapping']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_model_loading()
    if success:
        print("\n🎉 Model loading test PASSED!")
        sys.exit(0)
    else:
        print("\n💥 Model loading test FAILED!")
        sys.exit(1) 