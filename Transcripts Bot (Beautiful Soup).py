from bs4 import BeautifulSoup
import requests

# How To Get The HTML
website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

# Locate the box that contains title and transcript
box = soup.find('article', class_='main-article')
# Locate title and transcript
title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# export data in a text file with the "title" name.
with open(f'{title}.txt', 'w') as file:
    file.write(transcript)