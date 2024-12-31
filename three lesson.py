from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    
    first=browser.find_element(By.TAG_NAME, 'input')
    first.send_keys('Roman')
    last_name=browser.find_element(By.NAME,'last_name')
    last_name.send_keys('Petrov')
    city=browser.find_element(By.CLASS_NAME,'city')
    city.send_keys('Smolensk')
    country=browser.find_element(By.CSS_SELECTOR, 'div.form-group:nth-child(4) input')
    country.send_keys('Russia')
    button=browser.find_element(By.CSS_SELECTOR,'button')
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла