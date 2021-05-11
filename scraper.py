import requests
from bs4 import BeautifulSoup


# set the url to perform the get request
URL = requests.get('https://science.nasa.gov/science-news')

# make a soup object by using beautiful
# soup and set the markup as html parser
soup = BeautifulSoup(URL.content, "html.parser")


titles = []
images = []
descriptions = []

t_results = soup.find_all('span', class_='views-field-title')

for tag in t_results:
    title = tag.find('a')
    titles.append(title)
print(titles)

d_results = soup.find_all('span', class_='field-content')

for text in d_results[1:]:
    descript = text.get_text()
    descriptions.append(descript)
print(descriptions)