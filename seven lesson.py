from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text #считывает значение текста
    y = calc(x)
    
    answer=browser.find_element(By.ID,"answer")
    answer.send_keys(y)
    
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for=robotCheckbox]")
    checkbox.click()
    
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    
    button= browser.find_element(By.CLASS_NAME,"btn-default")
    button.click()
finally:
    time.sleep(30)
    
    browser.quit()