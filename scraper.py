import requests
from bs4 import BeautifulSoup

result = requests.get("https://news.ycombinator.com/")

src = result.content

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
stuff = soup.find_all('div', {"class": "athing"})
class HackerNewsStory:
    def __init__(self, title, url, author, points, comments, rank):
        self.title = title
        self.url = url
        self.author = author
        self.points = points
        self.comments = comments
        self.rank = rank
 
urls = []
for link in soup.find_all("a"):
    site = link.get('href')
    if "http" in site:
        urls.append(site)
athings = []
finalisedInfo = []
for item in soup.find_all('tr', {"class": "athing"}): 
    athings.append(item)
    rank = soup.find_all('span', {"class": "rank"})
    url = soup.find_all('a', {"class": "storylink"})
    HNItem = HackerNewsStory('something', url, 'something', 'something', 'something', rank)
    finalisedInfo.append(HNItem)


# print(athings)
print(athings[1])
# print(finalisedInfo)