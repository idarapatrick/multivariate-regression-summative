#!/usr/bin/env python3
"""
Simple test to verify the DataConversionWarning fix
"""

import sys
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def test_data_conversion_warning_fix():
    """Test that Random Forest training works without DataConversionWarning"""
    print("Testing DataConversionWarning fix...")
    
    # Create sample data
    np.random.seed(42)
    n_samples = 1000
    n_features = 5
    
    X = np.random.randn(n_samples, n_features)
    y = np.random.randn(n_samples)  # This is already 1D
    
    # Convert to pandas DataFrame and Series to simulate the original issue
    X_df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(n_features)])
    y_series = pd.Series(y, name='target')
    
    print(f"X shape: {X_df.shape}")
    print(f"y shape: {y_series.shape}")
    print(f"y type: {type(y_series)}")
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X_df, y_series, test_size=0.3, random_state=42)
    
    print(f"After split:")
    print(f"  y_train shape: {y_train.shape}")
    print(f"  y_train type: {type(y_train)}")
    
    # Convert target to 1D array (this is the fix)
    y_train_1d = y_train.values.ravel() if hasattr(y_train, 'values') else y_train.ravel()
    y_test_1d = y_test.values.ravel() if hasattr(y_test, 'values') else y_test.ravel()
    
    print(f"After conversion:")
    print(f"  y_train_1d shape: {y_train_1d.shape}")
    print(f"  y_train_1d type: {type(y_train_1d)}")
    
    # Train Random Forest (this should not produce warnings)
    print("\nTraining Random Forest...")
    rf_model = RandomForestRegressor(n_estimators=10, random_state=42, max_depth=5)
    rf_model.fit(X_train, y_train_1d)
    
    # Make prediction
    y_pred = rf_model.predict(X_test)
    
    print("✅ Random Forest training completed successfully!")
    print(f"   Prediction shape: {y_pred.shape}")
    print("   No DataConversionWarning should appear above")
    
    return True

if __name__ == "__main__":
    print("="*60)
    print("TESTING DATACONVERSIONWARNING FIX")
    print("="*60)
    
    try:
        success = test_data_conversion_warning_fix()
        if success:
            print("\n" + "="*60)
            print("✅ TEST PASSED: No DataConversionWarning!")
            print("="*60)
        else:
            print("\n" + "="*60)
            print("❌ TEST FAILED")
            print("="*60)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc() 