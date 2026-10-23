"""
Flipkart Mobile Price Intelligence & Web Scraper
================================================
Extracts mobile phone listings, prices, user ratings, discounts, and specs
using BeautifulSoup4, Requests, and Pandas.
Author: Bachu Uttej Siva Sai Kumar Reddy
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

BASE_URL = "https://www.flipkart.com/search?q=mobiles&page="


def scrape_flipkart_mobiles(num_pages=3):
    print(f"🕷️ Starting Flipkart Web Scraper across {num_pages} pages...")
    products = []

    for page in range(1, num_pages + 1):
        url = f"{BASE_URL}{page}"
        print(f"  Fetching page {page}: {url}")
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            if resp.status_code != 200:
                print(f"  ⚠️ Page {page} returned status code {resp.status_code}")
                continue

            soup = BeautifulSoup(resp.content, "html.parser")
            cards = soup.select("div._75nlfW, div.tUxRFH, div._1AtVbE")

            for card in cards:
                title_el = card.select_one("div.KzDlHZ, div._4rR01T")
                price_el = card.select_one("div.Nx9bqj, div._30jeq3")
                orig_price_el = card.select_one("div.yRaY8j, div._3I9_wc")
                rating_el = card.select_one("div.XQDdHH, div._3LWZlK")
                reviews_el = card.select_one("span.Wphh3N")

                if title_el and price_el:
                    products.append({
                        "Product_Name": title_el.text.strip(),
                        "Discounted_Price_INR": price_el.text.replace("₹", "").replace(",", "").strip(),
                        "Original_Price_INR": orig_price_el.text.replace("₹", "").replace(",", "").strip() if orig_price_el else "",
                        "Rating": rating_el.text.strip() if rating_el else "N/A",
                        "Ratings_Count": reviews_el.text.split("&")[0].replace("Ratings", "").replace(",", "").strip() if reviews_el else "N/A"
                    })

            time.sleep(1)  # Respect rate limits
        except Exception as e:
            print(f"  ❌ Error on page {page}: {e}")

    df = pd.DataFrame(products)
    out_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "flipkart_mobiles_scraped.csv")
    df.to_csv(out_file, index=False)
    print(f"✅ Scraping complete! Collected {len(df)} records → {out_file}")
    return df


if __name__ == "__main__":
    scrape_flipkart_mobiles(num_pages=2)
