from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

google = webdriver.Chrome()

google.get('http://uitestingplayground.com/textinput')
input_button = google.find_element(By.TAG_NAME, 'input')
input_button.send_keys('SkyPro')
add_button = google.find_element("xpath", '''//button[text() = "Button That Should Change it's Name Based on Input Value"]''').click()
wait = WebDriverWait(google, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="updatingButton"]')))

print(google.find_element("id", "updatingButton").text)

google.quit()