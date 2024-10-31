import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

user_name = driver.find_element(By.NAME, 'user-name')
user_name.send_keys('standard_user')

password = driver.find_element(By.NAME, 'password')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.NAME, 'login-button')
login_button.click()

element = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id=\"page_wrapper\"]')))

backpack = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
backpack.click()

t_shirt = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
t_shirt.click()

onesie = driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie")
onesie.click()

shopping_cart = driver.find_element(By.XPATH, "//*[@id=\"shopping_cart_container\"]/a")
shopping_cart.click()

cart = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="contents_wrapper"]')))

checkout = driver.find_element(By.NAME, "checkout")
checkout.click()

checkout_info = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="page_wrapper"]')))

first_name = driver.find_element(By.NAME, 'firstName')
first_name.send_keys('Иван')

last_name = driver.find_element(By.NAME, 'lastName')
last_name.send_keys('Петров')

zip_code = driver.find_element(By.NAME, 'postalCode')
zip_code.send_keys('199358')

continue_button = driver.find_element(By.NAME, 'continue')
continue_button.click()

total_sum = driver.find_element (By.CSS_SELECTOR, '[data-test="total-label"]').text

def test_third():
    assert total_sum == 'Total: $58.29'
