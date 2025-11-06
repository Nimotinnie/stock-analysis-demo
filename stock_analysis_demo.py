# ==============================================================
# Author: Meng-Ting Lee
# GitHub: https://github.com/mengtinglee/stock-analysis-demo
# Project: Stock Price Trend Analysis (Python + yfinance)
# ==============================================================

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import datetime

sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")

# 2. Download data
tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)
company_data = {t: yf.download(t, start=start, end=end, auto_adjust=False) for t in tech_list}

# 3. Wrangle and combine
company_names = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]
for df, name in zip(company_data.values(), company_names):
    df.columns = df.columns.get_level_values(0)
    df['company_name'] = name
df_all = pd.concat(company_data.values()).reset_index()

# 4. Function for quick stats
def summary_stats(name):
    """Return summary statistics for the given company"""
    df = df_all[df_all["company_name"] == name]
    return df.describe()[["Open", "Close", "Volume"]]

# Example output
print("=== Summary Statistics for APPLE ===")
print(summary_stats("APPLE").round(2))

# 5. Visualization: Closing Price
plt.figure(figsize=(10, 6))
for i, (ticker, df) in enumerate(company_data.items(), 1):
    plt.subplot(2, 2, i)
    df['Adj Close'].plot()
    plt.title(f"{ticker} Closing Price")
    plt.ylabel('Adj Close')
    plt.xlabel(None)
plt.tight_layout()

# 6. Visualization: Trading Volume
plt.figure(figsize=(10, 6))
for i, (ticker, df) in enumerate(company_data.items(), 1):
    plt.subplot(2, 2, i)
    df['Volume'].plot(color='purple')
    plt.title(f"{ticker} Volume")
    plt.ylabel('Volume')
    plt.xlabel(None)
plt.tight_layout()
plt.show()
