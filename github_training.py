import pandas as pd

def load_prices(filepath):
    """Load day-ahead prices from CSV."""
    df = pd.read_csv(filepath, parse_dates=["datetime"])
    return df

if __name__ == "__main__":
    print("BESS Analysis Tool")