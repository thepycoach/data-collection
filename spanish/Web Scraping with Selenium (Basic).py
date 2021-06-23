from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# Temas: Localizar un boton, seleccionar elemento de listas desplegables y extraer datos de tabla

# definer pagina a scrapear y ruta donde descargaste chromediver
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = '/Users/frank/Downloads/chromedriver' #escribe tu ruta aqui

# definer variable 'driver'
driver = webdriver.Chrome(path)
# abrir Google Chrome mediante chromedriver
driver.get(website)

# localizar un botón
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
# dar click en un botón
all_matches_button.click()

# usar una sección como referencia para garantizar que vamos a encontrar el elemento que buscamos (util cuando no hay id y queremos evitar nombre de clases repetitivos)
caja = driver.find_element_by_class_name('panel-body')
# seleccionar dropdown y seleccionar por texto
dropdown = Select(caja.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')
# wait implicito (util cuando la página demora en cargar elemetos varios segundos y obtenemor el error "ElementNotVisibleException")
time.sleep(5)
# seleccionar elementos de la tabla
matches = driver.find_elements_by_css_selector('tr')

# almacenar en listar
partidos = [match.text for match in matches]

#cerrar Google Chrome abierto por chromedriver
driver.quit()

# Bonus: Crea Dataframe en Pandas y exporta data en CSV (Excel)
df = pd.DataFrame({'goals': partidos})
print(df)
df.to_csv('tutorial.csv', index=False)
