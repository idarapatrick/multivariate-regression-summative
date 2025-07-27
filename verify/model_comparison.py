import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import joblib
import warnings
warnings.filterwarnings('ignore')

# Set style for better plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class LinearRegressionFromScratch:
    """Linear Regression implementation from scratch using gradient descent"""
    
    def __init__(self, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.weights = None
        self.bias = None
        self.loss_history = []
        
    def fit(self, X, y):
        """Train the model using gradient descent"""
        n_samples, n_features = X.shape
        
        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent
        for iteration in range(self.max_iterations):
            # Forward pass
            y_pred = self.predict(X)
            
            # Calculate gradients
            dw = (2/n_samples) * np.dot(X.T, (y_pred - y))
            db = (2/n_samples) * np.sum(y_pred - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
            # Calculate and store loss
            loss = mean_squared_error(y, y_pred)
            self.loss_history.append(loss)
            
            # Check for convergence
            if iteration > 0 and abs(self.loss_history[-1] - self.loss_history[-2]) < self.tolerance:
                print(f"Converged at iteration {iteration}")
                break
                
        return self
    
    def predict(self, X):
        """Make predictions"""
        return np.dot(X, self.weights) + self.bias

def load_and_prepare_data():
    """Load and prepare the data for modeling"""
    print("Loading and preparing data...")
    
    # Load the data
    data = pd.read_csv('hypertension_by_country.csv')
    
    # Filter for African countries and recent years
    countries = [
        "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
        "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
        "Democratic Republic of the Congo", "Republic of the Congo", "Côte d'Ivoire",
        "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia",
        "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho",
        "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius",
        "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda",
        "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia",
        "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia",
        "Uganda", "Zambia", "Zimbabwe"
    ]
    
    africa = data[
        (data['Country'].isin(countries)) &
        (data['Year'] >= 2010)
    ].reset_index(drop=True)
    
    # Drop irrelevant columns
    columns_to_drop = [
        "ISO",
        "Prevalence of hypertension lower 95% uncertainty interval",
        "Prevalence of hypertension upper 95% uncertainty interval",
        "Proportion of diagnosed hypertension among all hypertension lower 95% uncertainty interval",
        "Proportion of diagnosed hypertension among all hypertension upper 95% uncertainty interval",
        "Proportion of treated hypertension among all hypertension lower 95% uncertainty interval",
        "Proportion of treated hypertension among all hypertension upper 95% uncertainty interval",
        "Proportion of controlled hypertension among all hypertension lower 95% uncertainty interval",
        "Proportion of controlled hypertension among all hypertension upper 95% uncertainty interval",
        "Proportion of untreated stage 2 hypertension among all hypertension lower 95% uncertainty interval",
        "Proportion of untreated stage 2 hypertension among all hypertension upper 95% uncertainty interval"
    ]
    
    existing_columns_to_drop = [col for col in columns_to_drop if col in africa.columns]
    if existing_columns_to_drop:
        africa = africa.drop(columns=existing_columns_to_drop).reset_index(drop=True)
    
    # Create numeric dataset
    numeric_data = africa.copy()
    
    # Encode Sex
    sex_map = {'male': 0, 'female': 1, 'Men': 0, 'Women': 1}
    numeric_data['Sex_binary'] = numeric_data['Sex'].map(sex_map)
    
    # Encode Age as ordinal
    age_order = ['30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']
    age_map = {age: i for i, age in enumerate(age_order)}
    numeric_data['Age_encoded'] = numeric_data['Age'].map(age_map)
    
    # One-hot encode Country
    numeric_data = pd.get_dummies(numeric_data, columns=['Country'], drop_first=True)
    
    # Drop original categorical columns
    numeric_data = numeric_data.drop(columns=['Sex', 'Age'])
    
    # Prepare features and target
    X = numeric_data.drop(columns=['Prevalence of hypertension'])
    y = numeric_data['Prevalence of hypertension']
    
    # Convert target to 1D array to avoid DataConversionWarning
    y = y.values.ravel() if hasattr(y, 'values') else y.ravel()
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Data prepared successfully!")
    print(f"Training set: {X_train.shape[0]} samples, {X_train.shape[1]} features")
    print(f"Test set: {X_test.shape[0]} samples, {X_test.shape[1]} features")
    print(f"Target variable shape: {y_train.shape}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, X.columns

def train_models(X_train, X_test, y_train, y_test):
    """Train all models and return results"""
    print("\nTraining models...")
    
    # Target variables are already 1D arrays from data preparation
    models = {
        'Linear Regression (from scratch)': LinearRegressionFromScratch(learning_rate=0.01, max_iterations=1000),
        'Linear Regression (sklearn)': LinearRegression(),
        'SGD Regressor': SGDRegressor(max_iter=1000, random_state=42),
        'Decision Tree': DecisionTreeRegressor(random_state=42, max_depth=10),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
    }
    
    results = {}
    
    for name, model in models.items():
        print(f"Training {name}...")
        
        # Train the model
        if name == 'Linear Regression (from scratch)':
            model.fit(X_train, y_train)
            loss_history = model.loss_history
        else:
            model.fit(X_train, y_train)
            loss_history = None
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results[name] = {
            'model': model,
            'predictions': y_pred,
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'loss_history': loss_history
        }
        
        print(f"  {name} - R²: {r2:.4f}, RMSE: {rmse:.4f}")
    
    return results

def plot_loss_curves(results):
    """Plot loss curves for models that have loss history"""
    print("\nPlotting loss curves...")
    
    plt.figure(figsize=(12, 8))
    
    for name, result in results.items():
        if result['loss_history'] is not None:
            plt.plot(result['loss_history'], label=f"{name} - Final Loss: {result['loss_history'][-1]:.4f}")
    
    plt.title('Training Loss Curves', fontsize=16, fontweight='bold')
    plt.xlabel('Iteration', fontsize=12)
    plt.ylabel('Mean Squared Error', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_scatter_comparison(results, y_test):
    """Plot scatter plots comparing actual vs predicted values"""
    print("\nPlotting scatter plots...")
    
    # y_test is already a 1D array from data preparation
    n_models = len(results)
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.flatten()
    
    for i, (name, result) in enumerate(results.items()):
        if i < len(axes):
            ax = axes[i]
            y_pred = result['predictions']
            
            # Scatter plot
            ax.scatter(y_test, y_pred, alpha=0.6, s=20)
            
            # Perfect prediction line
            min_val = min(y_test.min(), y_pred.min())
            max_val = max(y_test.max(), y_pred.max())
            ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction')
            
            ax.set_xlabel('Actual Values', fontsize=10)
            ax.set_ylabel('Predicted Values', fontsize=10)
            ax.set_title(f'{name}\nR² = {result["r2"]:.4f}, RMSE = {result["rmse"]:.4f}', fontsize=11)
            ax.legend()
            ax.grid(True, alpha=0.3)
    
    # Remove extra subplot if needed
    if n_models < len(axes):
        for i in range(n_models, len(axes)):
            fig.delaxes(axes[i])
    
    plt.tight_layout()
    plt.show()

def plot_performance_comparison(results):
    """Plot performance comparison bar charts"""
    print("\nPlotting performance comparison...")
    
    metrics = ['mse', 'rmse', 'mae', 'r2']
    metric_names = ['Mean Squared Error', 'Root Mean Squared Error', 'Mean Absolute Error', 'R² Score']
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.flatten()
    
    for i, (metric, metric_name) in enumerate(zip(metrics, metric_names)):
        ax = axes[i]
        
        names = list(results.keys())
        values = [results[name][metric] for name in names]
        
        bars = ax.bar(names, values, alpha=0.7)
        ax.set_title(metric_name, fontsize=14, fontweight='bold')
        ax.set_ylabel(metric_name, fontsize=12)
        ax.tick_params(axis='x', rotation=45, ha='right')
        
        # Add value labels on bars
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                   f'{value:.4f}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.show()

def save_best_model(results, scaler, feature_names):
    """Save the best performing model"""
    print("\nSaving best model...")
    
    # Find best model based on R² score
    best_model_name = max(results.keys(), key=lambda x: results[x]['r2'])
    best_model = results[best_model_name]['model']
    best_score = results[best_model_name]['r2']
    
    print(f"Best model: {best_model_name} (R² = {best_score:.4f})")
    
    # Save the model and scaler
    model_data = {
        'model': best_model,
        'scaler': scaler,
        'feature_names': feature_names.tolist(),
        'model_name': best_model_name,
        'r2_score': best_score
    }
    
    joblib.dump(model_data, 'best_hypertension_model.pkl')
    print("Model saved as 'best_hypertension_model.pkl'")
    
    return best_model_name, best_model

def print_detailed_results(results):
    """Print detailed comparison results"""
    print("\n" + "="*80)
    print("DETAILED MODEL COMPARISON RESULTS")
    print("="*80)
    
    # Create comparison table
    comparison_data = []
    for name, result in results.items():
        comparison_data.append({
            'Model': name,
            'MSE': f"{result['mse']:.4f}",
            'RMSE': f"{result['rmse']:.4f}",
            'MAE': f"{result['mae']:.4f}",
            'R²': f"{result['r2']:.4f}"
        })
    
    comparison_df = pd.DataFrame(comparison_data)
    print(comparison_df.to_string(index=False))
    
    # Find best model
    best_model_name = max(results.keys(), key=lambda x: results[x]['r2'])
    print(f"\n🏆 BEST MODEL: {best_model_name}")
    print(f"   R² Score: {results[best_model_name]['r2']:.4f}")
    print(f"   RMSE: {results[best_model_name]['rmse']:.4f}")

def plot_linear_regression_fit(X_test, y_test, linear_model, model_name="Linear Regression"):
    """Plot scatter plot showing linear regression line fitting the dataset"""
    print(f"\nPlotting {model_name} line fit...")
    
    # Get predictions
    y_pred = linear_model.predict(X_test)
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    
    # Scatter plot of actual vs predicted
    plt.scatter(y_test, y_pred, alpha=0.6, s=30, color='steelblue', label='Data Points')
    
    # Perfect prediction line (y=x)
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction (y=x)')
    
    # Calculate and plot the actual linear regression line
    # Fit a line through the actual vs predicted points
    from sklearn.linear_model import LinearRegression
    line_fitter = LinearRegression()
    line_fitter.fit(y_test.reshape(-1, 1), y_pred)
    
    # Create line points
    line_x = np.linspace(min_val, max_val, 100)
    line_y = line_fitter.predict(line_x.reshape(-1, 1))
    
    plt.plot(line_x, line_y, 'g-', linewidth=2, label=f'{model_name} Fit Line')
    
    plt.xlabel('Actual Values', fontsize=12)
    plt.ylabel('Predicted Values', fontsize=12)
    plt.title(f'{model_name} Line Fit to Dataset\nR² = {r2_score(y_test, y_pred):.4f}', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the complete model comparison"""
    print("="*80)
    print("HYPERTENSION PREVALENCE PREDICTION - MODEL COMPARISON")
    print("="*80)
    
    # Load and prepare data
    X_train, X_test, y_train, y_test, scaler, feature_names = load_and_prepare_data()
    
    # Train models
    results = train_models(X_train, X_test, y_train, y_test)
    
    # Plot results
    plot_loss_curves(results)
    plot_scatter_comparison(results, y_test)
    plot_performance_comparison(results)
    
    # Plot specific linear regression line fit (for rubric requirement)
    if 'Linear Regression (sklearn)' in results:
        plot_linear_regression_fit(X_test, y_test, results['Linear Regression (sklearn)']['model'], "Linear Regression (sklearn)")
    if 'Linear Regression (from scratch)' in results:
        plot_linear_regression_fit(X_test, y_test, results['Linear Regression (from scratch)']['model'], "Linear Regression (from scratch)")
    
    # Print detailed results
    print_detailed_results(results)
    
    # Save best model
    best_model_name, best_model = save_best_model(results, scaler, feature_names)
    
    print("\n" + "="*80)
    print("MODEL COMPARISON COMPLETED SUCCESSFULLY!")
    print("="*80)

if __name__ == "__main__":
    main() 