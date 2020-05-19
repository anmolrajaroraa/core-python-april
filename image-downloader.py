# import urllib.request as req
from urllib.request import urlopen
from urllib.request import urlretrieve
# import bs4
from bs4 import BeautifulSoup as BS

url = "https://imdb.com"
response = urlopen(url)
sourceCode = BS(response, 'lxml')
# image = sourceCode.find('img')
# imageLink = image['src']
# print(imageLink)
# urlretrieve(imageLink, 'image.jpg')
imagesList = sourceCode.find_all('img')
for i, img in enumerate(imagesList):
    imageLink = img['src']
    fileExtension = imageLink[-3:]
    urlretrieve(imageLink, f"image_{i}.{fileExtension}")
