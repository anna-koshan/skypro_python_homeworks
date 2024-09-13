from selenium import webdriver
from time import sleep

google = webdriver.Chrome()

google.get('http://uitestingplayground.com/dynamicid')
add_button = google.find_element("xpath", '//button[text() = "Button with Dynamic ID"]').click()
sleep(3)
