from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/file_input.html")
    
    first_name = browser.find_element(By.NAME, "firstname").send_keys("Roman")
    last_name = browser.find_element(By.NAME, "lastname").send_keys("Coolgun")
    email = browser.find_element(By.NAME, "email").send_keys("qwerty@gmail.com")
    
    
    file = browser.find_element(By.ID, "file")
    dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir, "test.txt")
    file.send_keys(file_path)
    
    button = browser.find_element(By.CLASS_NAME, "btn-primary").click()
finally:
    time.sleep(30)
    browser.quit()