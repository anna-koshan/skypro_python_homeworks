from selenium import webdriver
from time import sleep

google = webdriver.Chrome()

google.get('http://uitestingplayground.com/classattr')
add_button = google.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
sleep(3)
