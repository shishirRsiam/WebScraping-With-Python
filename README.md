
# 🕸️ WebScraping-With-Python

This repository is a beginner-friendly guide to web scraping using Python. It includes simple scripts to help you learn how to extract data from websites.

---

## 📌 What is Web Scraping?

Web scraping is the process of automatically collecting information from websites. It's useful for things like:
- Getting product prices
- Collecting news articles
- Gathering job listings

---

## 🧰 Tools Used

- `requests` – to send HTTP requests
- `BeautifulSoup` – to parse HTML content
- `Selenium` – to scrape dynamic websites (optional)

---

## 🚀 Example Code

```python
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

for quote in soup.select('.quote'):
    text = quote.select_one('.text').text
    author = quote.select_one('.author').text
    print(f"{text} — {author}")
````

---

## 📦 Setup

```bash
git clone https://github.com/yourusername/WebScraping-With-Python.git
cd WebScraping-With-Python
pip install -r requirements.txt
```

---

## 📂 Folders (Optional)

* `basics/` – simple scrapers
* `dynamic-sites/` – Selenium examples
* `pagination/` – handling multi-page scraping

---


---

Happy Scraping! 🕷️
