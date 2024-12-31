from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/get_attribute.html")
    
    image = browser.find_element(By.ID,"treasure")
    image_value = image.get_attribute("valuex")
    y = calc(image_value)
    
    ansver = browser.find_element(By.ID, 'answer')
    ansver.send_keys(y)
    
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    
    button = browser.find_element(By.CLASS_NAME, "btn-default")
    button.click()
finally:
    time.sleep(30)
    browser.quit()