#!/usr/bin/env python3
"""
Test script to verify package versions are compatible
"""

import sys
import importlib

def test_versions():
    """Test if all required packages are available and compatible"""
    print("🧪 Testing Package Versions...")
    
    required_packages = {
        'fastapi': '0.104.1',
        'uvicorn': '0.24.0',
        'pydantic': '2.5.0',
        'numpy': '1.26.4',
        'pandas': '2.1.4',
        'sklearn': '1.7.1',
        'pickle': None  # Built-in module
    }
    
    all_good = True
    
    for package, expected_version in required_packages.items():
        try:
            if package == 'sklearn':
                module = importlib.import_module('sklearn')
            else:
                module = importlib.import_module(package)
            
            if hasattr(module, '__version__'):
                actual_version = module.__version__
                print(f"✅ {package}: {actual_version}")
                
                if expected_version and actual_version != expected_version:
                    print(f"⚠️  Version mismatch for {package}: expected {expected_version}, got {actual_version}")
                    all_good = False
            else:
                print(f"✅ {package}: loaded (no version info)")
                
        except ImportError as e:
            print(f"❌ {package}: ImportError - {e}")
            all_good = False
        except Exception as e:
            print(f"❌ {package}: Error - {e}")
            all_good = False
    
    return all_good

if __name__ == "__main__":
    success = test_versions()
    if success:
        print("\n🎉 All packages are compatible!")
        sys.exit(0)
    else:
        print("\n💥 Some packages have issues!")
        sys.exit(1) 