import pandas as pd

def load_prices(filepath):
    """Load day-ahead prices from CSV."""
    df = pd.read_csv(filepath, parse_dates=["datetime"])
    return df

if __name__ == "__main__":
    print("BESS Analysis Tool")


def calculate_spread(prices):
    """Calculate the daily spread between max and min price."""
    return prices.max() - prices.min()

def bess_profit(buy_price, sell_price, capacity_mwh=100, efficiency=0.90):
    """Calculate profit from one charge/discharge cycle."""
    cost = buy_price * capacity_mwh
    revenue = sell_price * capacity_mwh * efficiency
    return revenue - cost

def round_trip_efficiency(charge_mwh, discharge_mwh):
    """Calculate actual round-trip efficiency."""
    return discharge_mwh / charge_mwh