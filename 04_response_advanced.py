import requests

url = 'https://jsonplaceholder.typicode.com/posts/'  # Sample public JSON API
response = requests.get(url)

print("Elapsed Time:", response.elapsed)                             # Time taken to get response (timedelta object)
print("Cookies:", response.cookies)                                  # Cookies sent by the server (if any)
print("Redirection History:", response.history)                      # List of Response objects if redirected
print("Content-Type Header:", response.headers.get('Content-Type'))  # Check if response is JSON, HTML, etc.


# Try parsing the response as JSON
print("\nJSON Response (parsed):")
try:
    data = response.json()   # Parses JSON content
    print(data)              # Prints parsed Python dict
except ValueError:
    print("❌ Response is not valid JSON.")

# Optional: Raw content in bytes (useful for images, files)
# print("Raw Content (bytes):", response.content)