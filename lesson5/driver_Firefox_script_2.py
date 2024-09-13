from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

firefox.get('https://the-internet.herokuapp.com/inputs')
input_button = firefox.find_element(By.TAG_NAME, 'input')
input_button.send_keys('1000')
sleep(5)
input_button.clear()
sleep(2)
input_button.send_keys('999')
sleep(5)