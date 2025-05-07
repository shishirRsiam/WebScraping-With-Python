import os, requests
from bs4 import BeautifulSoup 

current_page, book_count = 1, 1
os.makedirs('Books', exist_ok=True)

while True:
    url = f'https://books.toscrape.com/catalogue/page-{current_page}.html'
    response = requests.get(url)
    print(f"Time Taken: {response.elapsed}")
    print(f"Scraping page {current_page} -> Status Code: {response.status_code}\n")
    if response.status_code != 200: break

    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.select('.image_container')
    with open('05_All_Books.txt', 'w', encoding='utf-8') as file:
        for book in books:
            image_url = book.select_one('img').get('src')
            book_name = book.select_one('img').get('alt').strip()
            file.write(f"{book_count}. {book_name}\n")
            book_count += 1
        
    current_page += 1