import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def train_model():
    # Load feature-engineered data
    df = pd.read_csv("data/sample/features_traffic_data.csv")

    # Select input features (X) and target (y)
    X = df[['hour', 'weekday']]
    y = df['traffic_volume']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate model
    mae = mean_absolute_error(y_test, predictions)

    print("✅ Model trained successfully")
    print("📉 Mean Absolute Error (MAE):", mae)

if __name__ == "__main__":
    train_model()
