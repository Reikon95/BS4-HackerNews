import requests
from bs4 import BeautifulSoup

result = requests.get("https://news.ycombinator.com/")

src = result.content

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
stuff = soup.find_all('div', {"class": "athing"})
urls = []
for link in soup.find_all("a"):
    site = link.get('href')
    if "http" in site:
        urls.append(site)
athings = []
for items in soup.find_all('tr', {"class": "athing"}): 
    athings.append(items)

# print(athings)
print(type(athings))
print(athings[1])
class HackerNewsStory:
    def __init__(self, title, url, author, points, comments, rank):
        self.title = title
        self.url = url
        self.author = author
        self.points = points
        self.comments = comments
        self.rank = rank
 