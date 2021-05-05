import requests
from bs4 import BeautifulSoup

# set the url to perform the get request
URL = 'https://science.nasa.gov/science-news'
page = requests.get(URL)

# load the page content
text = page.content

# make a soup object by using beautiful
# soup and set the markup as html parser
soup = BeautifulSoup(text, "html.parser")
