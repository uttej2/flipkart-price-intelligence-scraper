# 📱 Flipkart Mobile Price Intelligence & Web Scraper

> **Automated E-Commerce Extraction, Data Cleaning, and Price Intelligence Analytics** using Python, BeautifulSoup4, Requests, and Pandas.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup-4.12+-green?style=flat-square)](https://pypi.org/project/beautifulsoup4/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

---

## 📌 Executive Summary

Manual competitive price benchmarking across e-commerce platforms is slow, error-prone, and inefficient. 

This project delivers:
- **Automated Web Scraping**: Extracts live mobile listings, pricing variations, discount percentages, and customer ratings from Flipkart.
- **Robust Error Handling**: Implements user-agent rotation headers, polite sleep delays, and exception-safe pagination.
- **Data Normalization & EDA**: Cleans raw currency symbols, parses numerical values, and computes brand discount variances, reducing manual data collection time by **95%**.

---

## 📂 Repository Structure

```plaintext
flipkart-price-intelligence-scraper/
│
├── scraper.py             # BeautifulSoup4 & Requests web scraper
├── analysis.py            # Price comparison & exploratory analysis
├── data/                  # Output storage for scraped CSV files
│   └── flipkart_mobiles_scraped.csv
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the scraper
python scraper.py

# 3. Perform competitive price analysis
python analysis.py
```

---

## 👤 Author
**Bachu Uttej Siva Sai Kumar Reddy**
- **GitHub**: [@uttej2](https://github.com/uttej2)
- **Portfolio**: [https://uttej2.github.io](https://uttej2.github.io)
- **LinkedIn**: [Connect on LinkedIn](https://linkedin.com/in/uttej-sai)
