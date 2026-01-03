import pandas as pd

def clean_data():
    # Load raw data
    df = pd.read_csv("data/sample/Metro_Interstate_Traffic_Volume.csv")

    # Remove rows with missing values
    df = df.dropna()

    # Convert date_time column to datetime format
    df['date_time'] = pd.to_datetime(df['date_time'])

    # Remove invalid traffic volume values
    df = df[df['traffic_volume'] >= 0]

    # Save cleaned data
    df.to_csv("data/sample/clean_traffic_data.csv", index=False)

    print("✅ Data cleaned and saved successfully")
    print(df.head())

    return df

if __name__ == "__main__":
    clean_data()
