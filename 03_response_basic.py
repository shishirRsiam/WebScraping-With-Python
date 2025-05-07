import requests

url = 'https://books.toscrape.com/'
response = requests.get(url)

print("Status Code:", response.status_code)         # 200 = OK
print("OK?:", response.ok)                           # True if status_code < 400
print("Final URL:", response.url)                    # In case of redirect
print("Encoding:", response.encoding)                # Usually 'utf-8'
print("Headers:", response.headers)                  # responseponse headers


print("\n\nFirst 300 chars of responseponse body:\n")
print(response.text[:300])                           # HTML body as string