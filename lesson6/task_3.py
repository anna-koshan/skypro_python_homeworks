from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

google = webdriver.Chrome()

google.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
wait = WebDriverWait(google, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="landscape"]')))
get_attribute = google.find_element(By.ID, 'award').get_attribute('src')
print(get_attribute)

google.quit()