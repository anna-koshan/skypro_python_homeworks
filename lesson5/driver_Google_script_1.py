from selenium import webdriver

google = webdriver.Chrome()

google.get('https://the-internet.herokuapp.com/add_remove_elements/')
for time in range(5):
    add_button = google.find_element("xpath", '//button[text() = "Add Element"]').click()
    find_delete = google.find_elements("xpath", '//button[text() = "Delete"]')

print (f'Размер списка кнопок Delete в Google: {len(find_delete)}')