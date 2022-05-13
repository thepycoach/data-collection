from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

path = ''  # Introduce your chromedriver path here
website = "https://web.whatsapp.com/"
phone_number = ""  # Write a phone number here
photo_path = ""  # introduce your photo path here

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.maximize_window()
time.sleep(30)  # scan QR code (we don't need to wait that much when we connect to an existing browser)

search_phone = driver.find_element(by='xpath', value='//div[@title="Search input textbox"]')
search_phone.send_keys(phone_number)
time.sleep(2)

contacts = driver.find_elements(by='xpath', value='//div[@aria-label="Search results."]//div[@data-testid="cell-frame-container"]')
contacts[-1].click()  # picks last element in the list (this one represents first in the whatsapp search list)
time.sleep(2)

# upload and send photo
attach_button = driver.find_element(by='xpath', value='//span[@data-testid="clip"]')
attach_button.click()
time.sleep(2)

# when inspecting choose the element containing the word "input" so you can send keys with the path of the photo
attach_image_input = driver.find_element(by='xpath', value='//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
attach_image_input.send_keys(photo_path)
time.sleep(2)

send_image_button = driver.find_element(by='xpath', value='//div[@data-testid="drawer-middle"]//span[@data-testid="send"]')
send_image_button.click()
time.sleep(5)  # wait till the message is delivered

driver.quit()
