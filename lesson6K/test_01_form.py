import pytest 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
google = webdriver.Chrome() 
google.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html') 
google.maximize_window() 
google.execute_script("document.body.style.zoom='50%'") 
 
first_name = google.find_element(By.NAME, 'first-name') 
first_name.send_keys('Иван') 
 
last_name = google.find_element(By.NAME, 'last-name') 
last_name.send_keys('Петров') 
 
address = google.find_element(By.NAME, 'address') 
address.send_keys('Ленина, 55-3') 
 
e_mail = google.find_element(By.NAME, 'e-mail') 
e_mail.send_keys('test@skypro.com') 
 
phone = google.find_element(By.NAME, 'phone') 
phone.send_keys('+7985899998787') 
 
zip_code = google.find_element(By.NAME, 'zip-code') 
zip_code.send_keys("") 
 
city = google.find_element(By.NAME, 'city') 
city.send_keys('Москва') 
 
country = google.find_element(By.NAME, 'country') 
country.send_keys('Россия') 
 
job_position = google.find_element(By.NAME, 'job-position') 
job_position.send_keys('QA') 
 
company = google.find_element(By.NAME, 'company') 
company.send_keys('SkyPro') 
 
element = google.find_element(By.CSS_SELECTOR, "button[type='submit']") 
element.click() 
 
 
def test_01_form(): 
    WebDriverWait(google, 30).until(EC.presence_of_element_located((By.ID, "zip-code"))) 
 
    zip_code_element = google.find_element(By.ID, "zip-code") 
    assert "alert-danger" in zip_code_element.get_attribute( 
        "class"), "Zip code is not highlighted in red!" 
 
    fields_to_check = [ 
        "first-name", 
        "last-name", 
        "address", 
        "city", 
        "country", 
        "e-mail", 
        "phone", 
        "job-position", 
        "company"] 
    for field in fields_to_check: 
        element = google.find_element(By.ID, field) 
        assert "alert-success" in element.get_attribute( 
            "class"), f"{field.replace('-', ' ').title()} is not highlighted in green!"