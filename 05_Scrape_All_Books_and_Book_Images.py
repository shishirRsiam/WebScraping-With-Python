import os, requests, datetime, re
from bs4 import BeautifulSoup 

current_page, book_count = 1, 1
os.makedirs('Books', exist_ok=True)
os.makedirs('Images', exist_ok=True)

store = set()
main_url = 'https://books.toscrape.com'
while True:
    start_time = datetime.datetime.now()
    url = f'https://books.toscrape.com/catalogue/page-{current_page}.html'
    response = requests.get(url)
    print(f"Time Taken: {response.elapsed}")
    print(f"Scraping page {current_page} -> Status Code: {response.status_code}")
    if response.status_code != 200: break

    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.select('.image_container')
    with open('05_All_Books.txt', 'a', encoding='utf-8') as file:
        for book in books:
            image_url = book.select_one('img').get('src')
            book_name = book.select_one('img').get('alt').strip()
            file.write(f"{book_count}. {book_name}\n")

            safe_name = re.sub(r'[^A-Za-z]', '_', book_name)  # Replace non A-Z, a-z with '_'
            # print(f"Saving {book_count}_{safe_name}.jpg")
            image = requests.get(main_url + image_url[2:])
            with open(f"Images/{book_count}_{safe_name}.jpg", 'wb') as img_file:
                img_file.write(image.content)

            book_count += 1
    end_time = datetime.datetime.now()
    print(f"Page {current_page} took {end_time - start_time} time to scrape\n")
    current_page += 1