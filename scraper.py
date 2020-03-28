import requests
from bs4 import BeautifulSoup

result = requests.get("https://news.ycombinator.com/")

# print(result.status_code)

# print(result.headers)

src = result.content

# print(src)

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
print(urls)
print(len(urls))
print(athings)