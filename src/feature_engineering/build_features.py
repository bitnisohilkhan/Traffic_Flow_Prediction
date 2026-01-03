import pandas as pd

def build_features():
    # Load cleaned data
    df = pd.read_csv("data/sample/clean_traffic_data.csv")

    # Convert date_time to datetime
    df['date_time'] = pd.to_datetime(df['date_time'])

    # Create new features
    df['hour'] = df['date_time'].dt.hour
    df['weekday'] = df['date_time'].dt.weekday

    # Save feature-engineered data
    df.to_csv("data/sample/features_traffic_data.csv", index=False)

    print("✅ Features created successfully")
    print(df[['date_time', 'hour', 'weekday']].head())

    return df

if __name__ == "__main__":
    build_features()
