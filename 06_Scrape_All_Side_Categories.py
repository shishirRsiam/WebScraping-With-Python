import requests
from bs4 import BeautifulSoup 


url = f'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


categories = soup.select_one('.side_categories').find_all('a')
with open('06_All_Side_Categories.txt', 'w', encoding='utf-8') as file:
    for index, category in enumerate(categories, start=1):
        file.write(f"{index}. {category.text.strip()}\n")


print("✅ All side categories saved to '06_All_Side_Categories.txt' Done!")