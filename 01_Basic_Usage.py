from bs4 import BeautifulSoup  # Import BeautifulSoup from the bs4 library


# Read HTML content from a local file
with open('01_Simple_About_Me.html', 'r') as file:  # Open the HTML file in read mode
    html_file = file.read()                         # Read the entire content of the file as a string

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_file, 'html.parser')  # Create a BeautifulSoup object and parse using 'html.parser'

print(soup.prettify())  # Prettify gives a readable, indented version of the HTML
print(soup.get_text())  # Returns only the text content from the HTML, no tags

print(soup.h2)          # Finds and prints the first <h2> tag with its HTML
print(soup.h2.text)     # Prints only the text inside the first <h2> tag

# Find and print all <h3> tags (returns a list of all <h3> tag elements)
print(soup.find_all('h3'))  # Finds every <h3> tag and returns them in a list
