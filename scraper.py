import requests
from bs4 import BeautifulSoup

result = requests.get("https://news.ycombinator.com/")

# print(result.status_code)

# print(result.headers)

src = result.content

# print(src)

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
urls = []
for a in soup.find_all("a"):
    urls.append(a)
print(urls)