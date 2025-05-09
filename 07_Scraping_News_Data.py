
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

# Scrape The Daily Star
def scrape_daily_star_news():
    response = []
    base_url = 'https://www.thedailystar.net/'
    url = f'{base_url}news/bangladesh'
    url = 'https://www.thedailystar.net/news/bangladesh?page=2'
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            with open("07_The_Daily_Star.html", "w", encoding="utf-8") as file:
                file.write(soup.prettify())

            # Select all cards inside .view-content
            for card in soup.select('.card.position-relative.horizontal'):
                try:
                    image_url = card.select_one('source')['data-srcset'].replace('medium_202', 'very_big_1')
                    card = card.select_one('.card-content')
                    content = {
                        'id': len(response) + 1,
                        'title': card.select_one('a').text.strip(),
                        'intro': card.select_one('.intro').text.strip() if card.select_one('.intro') else '',
                        'interval': card.select_one('.interval').text.strip() if card.select_one('.interval') else '',
                        'url': base_url + card.select_one('a')['href'],
                        'image': image_url.replace(' 1x', ''),
                    }
                    response.append(content)
                except Exception as inner_e:
                    print(f"Error parsing a card: {inner_e}")
        else:
            print(f"Request failed with status code {res.status_code}")
    except Exception as e:
        print(f"The Daily Star error: {e}")
    return response


response = scrape_daily_star_news()
print(response)


with open("07_The_Daily_Star.json", "w", encoding="utf-8") as file:
    file.write(str(response))