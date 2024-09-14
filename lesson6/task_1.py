from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

google = webdriver.Chrome()

google.get('http://uitestingplayground.com/ajax')
button = google.find_element(By.ID, 'ajaxButton')
button.click()
wait = WebDriverWait(google, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success")))

line = google.find_element(By.CSS_SELECTOR, "#content")
txt = line.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)
google.quit()