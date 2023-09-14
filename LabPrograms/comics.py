# this program download comics from xkcd site

import os
from bs4 import BeautifulSoup
import requests

url = 'https://xkcd.com'
archive = url + '/archive/'

folderPath = 'XKCD'
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

response = requests.get(archive)
soup = BeautifulSoup(response.content, 'html.parser')

comicLink = soup.select('#middleContainer > a')

for link in comicLink:
    comic_url = url + link.get('href')

    comicResponse = requests.get(comic_url)
    comicSoup = BeautifulSoup(comicResponse.content, 'html.parser')

    comicImage = comicSoup.select('#comic > img')[0]
    imageUrl = 'https:' + comicImage.get('src')

    imageResponse = requests.get(imageUrl)

    imageName = imageUrl.split('/')[-1]
    imagePath = os.path.join(folderPath, imageName)

    with open(imagePath, 'wb') as f:
        f.write(imageResponse.content)
    print(f"Downloaded: {imageName}")

print("All XKCD comics downloaded.")
