"""
Flipkart Mobile Price Intelligence — Exploratory Data Analysis
==============================================================
Loads scraped e-commerce mobile data and calculates:
1. Brand market share & average price points
2. Discount percentages
3. Rating distributions
Author: Bachu Uttej Siva Sai Kumar Reddy
"""

import pandas as pd
import numpy as np
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data", "flipkart_mobiles_scraped.csv")

# Create a sample dataset if scraping hasn't run yet
if not os.path.exists(DATA_PATH):
    os.makedirs(os.path.join(BASE, "data"), exist_ok=True)
    sample_data = [
        {"Product_Name": "Apple iPhone 15 (Black, 128 GB)", "Brand": "Apple", "Discounted_Price_INR": 69999, "Original_Price_INR": 79900, "Rating": 4.6, "Ratings_Count": 24510},
        {"Product_Name": "Samsung Galaxy S24 5G (Onyx Black, 256 GB)", "Brand": "Samsung", "Discounted_Price_INR": 74999, "Original_Price_INR": 82999, "Rating": 4.5, "Ratings_Count": 11200},
        {"Product_Name": "OnePlus 12R (Iron Gray, 256 GB)", "Brand": "OnePlus", "Discounted_Price_INR": 42999, "Original_Price_INR": 45999, "Rating": 4.5, "Ratings_Count": 9400},
        {"Product_Name": "Redmi Note 13 Pro 5G (Arctic White, 128 GB)", "Brand": "Xiaomi", "Discounted_Price_INR": 24999, "Original_Price_INR": 28999, "Rating": 4.3, "Ratings_Count": 42100},
        {"Product_Name": "Realme 12 Pro+ 5G (Submarine Blue, 256 GB)", "Brand": "Realme", "Discounted_Price_INR": 29999, "Original_Price_INR": 34999, "Rating": 4.4, "Ratings_Count": 18900},
        {"Product_Name": "Motorola Edge 50 Pro 5G (Black Beauty, 256 GB)", "Brand": "Motorola", "Discounted_Price_INR": 31999, "Original_Price_INR": 36999, "Rating": 4.4, "Ratings_Count": 8750},
        {"Product_Name": "Google Pixel 8 (Hazel, 128 GB)", "Brand": "Google", "Discounted_Price_INR": 58999, "Original_Price_INR": 75999, "Rating": 4.4, "Ratings_Count": 5400},
        {"Product_Name": "vivo V30 Pro (Classic Black, 256 GB)", "Brand": "Vivo", "Discounted_Price_INR": 41999, "Original_Price_INR": 46999, "Rating": 4.5, "Ratings_Count": 12300},
    ]
    pd.DataFrame(sample_data).to_csv(DATA_PATH, index=False)

df = pd.read_csv(DATA_PATH)
print("="*60)
print(" Flipkart Price Intelligence & Competitive Analytics")
print("="*60)
print(f"Total Listings Analyzed: {len(df)}\n")

# Calculate Discount Percentage
df["Discounted_Price_INR"] = pd.to_numeric(df["Discounted_Price_INR"], errors="coerce")
df["Original_Price_INR"] = pd.to_numeric(df["Original_Price_INR"], errors="coerce")
df["Discount_Pct"] = ((df["Original_Price_INR"] - df["Discounted_Price_INR"]) / df["Original_Price_INR"] * 100).round(1)

print("📊 Top 5 Highest Value Deals by Discount %:")
top_deals = df.sort_values(by="Discount_Pct", ascending=False)[["Product_Name", "Discounted_Price_INR", "Original_Price_INR", "Discount_Pct", "Rating"]].head(5)
print(top_deals.to_string(index=False))

print("\n📊 Summary Statistics:")
print(df[["Discounted_Price_INR", "Discount_Pct", "Rating"]].describe().round(2).to_string())
