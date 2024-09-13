from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

firefox.get('https://the-internet.herokuapp.com/login')
login_button = firefox.find_element(By.ID, 'username')
login_button.send_keys('tomsmith')
password_button = firefox.find_element(By.ID, 'password')
password_button.send_keys('SuperSecretPassword!')
sleep(10)
click_button = firefox.find_element(By.TAG_NAME, 'button').click()
sleep(5)