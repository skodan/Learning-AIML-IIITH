import requests
from bs4 import BeautifulSoup

# get content from webpage
url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page,"html.parser")

# get the list of links and their texts
inNews = soup.find('div',id='mp-right')
News = inNews.find_all('li')

# loop through all the list items and get the name and link
for items in News:
    print(items.get_text())
    links = items.find_all('a')
    for link in links:
        print(link['href'])
    print()

# get picture details and save it
picDiv = inNews.find('div',class_='itn-img')
picture = picDiv.find('img')
src = picture['src']

# fetch the name from the src
fname = src[src.rfind('/')+1:]

# save the picture
r = requests.get('https:'+src)
open(fname,'wb').write(r.content)