# from turtle import ht
# from bs4 import BeautifulSoup
# import requests

# headers = {'user-agent': 'my-app/0.0.1'}
# html = requests.get("https://flatironschool.com/", headers=headers)

# <h2 class="heading-60-black color-black mb-20">
# we'll create a Beautiful Soup object to take the string of HTML returned by requests's get method which represents the document as a nested data structure
# doc = BeautifulSoup(html.text, 'html.parser') #

#print(doc)
#.free-lessons/#coding
from bs4 import BeautifulSoup
import requests

# Headers to simulate a real browser request
headers = {'user-agent': 'my-app/0.0.1'}

# Fetch the HTML content from the Flatiron School website
html = requests.get("https://flatironschool.com/", headers=headers)

# Create a BeautifulSoup object to parse the HTML content
doc = BeautifulSoup(html.text, 'html.parser')

# Search for <h2> tags with a specific class (e.g., "heading-60-black color-black mb-20")
h2_tag = doc.find('h2', class_="heading-60-black color-black mb-20")

# Print the found <h2> tag text if it exists
if h2_tag:
    print(h2_tag.text.strip())  # Stripping to remove extra spaces
else:
    print("No <h2> tag found with the specified class.")