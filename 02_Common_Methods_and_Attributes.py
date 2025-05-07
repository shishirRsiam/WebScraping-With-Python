# === 02_Common BeautifulSoup Methods and Attributes ===

# soup.title               => Access the <title> tag
# soup.title.text          => Text inside the <title>
# soup.find('tag')         => Finds the first occurrence of the tag
# soup.find_all('tag')     => Returns all tags in a list
# tag.name                 => Name of the tag (e.g., 'h3')
# tag.attrs                => All attributes of a tag as a dictionary
# tag.get('attribute')     => Get a specific attribute value safely
# tag['attribute']         => Same as get(), but will throw error if missing
# tag.text / tag.string    => Text inside the tag
# tag.parent               => Get the parent tag
# tag.children             => Generator for child tags (use list() to view)
# tag.descendants          => All nested tags and strings
# tag.next_sibling         => Next element on the same level
# tag.previous_sibling     => Previous element on the same level
# soup.get_text()          => All visible text in the HTML
# soup.prettify()          => Nicely formatted HTML output


from bs4 import BeautifulSoup  # Import BeautifulSoup from the bs4 library

# Read HTML content from a local file
with open('01_Simple_About_Me.html', 'r') as file:  # Open the HTML file in read mode
    html_file = file.read()                         # Read the entire content of the file as a string

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_file, 'html.parser')  # Create a BeautifulSoup object and parse using 'html.parser'


# === Accessing a single tag using .find() ===
tag = soup.find('h3')            # Finds the first <h3> tag
print(tag)                       # Prints the entire tag: <h3>...</h3>
print(tag.text)                  # Prints the text inside the <h3> tag
print(tag.get('id'))             # Prints the value of the 'id' attribute if present
print(tag.get('href'))           # Prints the value of the 'href' attribute if present (None if not)
print(tag.get('class'))          # Prints the value of the 'class' attribute as a list, or None if not present
print(tag.select('span'))        # Finds all <span> tags inside the <h3> tag
print(tag.select_one('span'))    # Finds the first <span> tag inside the <h3> tag

print('\n\n\n')


# === Accessing multiple tags using .find_all() ===
tags = soup.find_all('a')        # Finds all <a> (anchor) tags
for tag in tags:
    print(f"{tag.text} -> {tag.get('href')}")  # Prints the link text and its href value