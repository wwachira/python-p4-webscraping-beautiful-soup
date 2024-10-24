from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

# we'll create a Beautiful Soup object to take the string of HTML returned by requests's get method which represents the document as a nested data structure
doc = BeautifulSoup(html.text, 'html.parser')

print(doc)
