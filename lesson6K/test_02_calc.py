import pytest 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
 
 
def test_calculator(): 
    # Инициализация браузера 
    google = webdriver.Chrome() 
    google.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html') 
 
    # Установка задержки 
    delay_button = google.find_element(By.CSS_SELECTOR, '#delay') 
    delay_button.clear() 
    delay_button.send_keys('45') 
 
    # Нажатие кнопок 7 + 8 = 
    google.find_element(By.XPATH, '//span[text()="7"]').click() 
    google.find_element(By.XPATH, '//span[text()="+"]').click() 
    google.find_element(By.XPATH, '//span[text()="8"]').click() 
 
    # Нажатие на "=" и ожидание результата 
    google.find_element(By.XPATH, '//span[text()="="]').click() 
 
    # Ожидание результата "15" на экране 
    wait = WebDriverWait(google, 46) 
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15')) 
 
    # Проверка результата 
    result = google.find_element(By.CLASS_NAME, 'screen').text 
    assert result == "15", f"Ожидаемый результат был '15', но получил '{result}'" 
 
    # Закрытие браузера 
    google.quit()