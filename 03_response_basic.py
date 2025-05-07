import requests

url = 'https://books.toscrape.com/'
response = requests.get(url)

print("Status Code:", response.status_code)          # HTTP status code (e.g., 200, 404, 500)
print("OK?:", response.ok)                           # True if status code is < 400 (shortcut for checking success)
print("Final URL:", response.url)                    # Final URL (useful after redirects), In case of redirect
print("Encoding:", response.encoding)                # Encoding used to decode res.text (like 'utf-8')
# print("Content:", response.content)                # Content in bytes (useful for images, files)
print("Headers:", response.headers)                  # Dictionary of HTTP response headers


print("\n\nFirst 300 chars of responseponse body:\n")
print(response.text[:300])                           # Content of the response as a string (usually HTML or JSON)