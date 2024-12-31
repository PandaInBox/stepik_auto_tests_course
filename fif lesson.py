from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    first=browser.find_element(By.XPATH, '//div[@class="form-group"][1]/input')
    first.send_keys('Roman')
    last_name=browser.find_element(By.NAME,'last_name')
    last_name.send_keys('Petrov')
    city=browser.find_element(By.NAME,'firstname')
    city.send_keys('Smolensk')
    country=browser.find_element(By.ID, 'country')
    country.send_keys('Russia')
    button=browser.find_element(By.XPATH,'//button[text()="Submit"]')
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла