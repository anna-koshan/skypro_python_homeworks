from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

firefox.get('https://the-internet.herokuapp.com/entry_ad')
wait = WebDriverWait(firefox, 10)
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.modal-footer')))
close_button.click()    