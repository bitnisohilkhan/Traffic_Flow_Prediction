import pandas as pd

def load_data():
    df = pd.read_csv("data/sample/Metro_Interstate_Traffic_Volume.csv")
    print("✅ Data loaded successfully")
    print(df.head())
    return df

if __name__ == "__main__":
    load_data()
