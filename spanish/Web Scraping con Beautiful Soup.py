from bs4 import BeautifulSoup
import requests

# Obtener el documento HTML
website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

# Localizar la caja (box) que contiene el titulo (title) y transcript
box = soup.find('article', class_='main-article')
# Localizar el titulo (title) y transcript
title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# Exportar data en un archivo txt con el nombre de la variable titulo (title)
with open(f'{title}.txt', 'w') as file:
    file.write(transcript)
