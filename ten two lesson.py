from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")
    
    x_value = browser.find_element(By.ID, "input_value").text
    y = calc(x_value)
    
    answer = browser.find_element(By.ID, "answer").send_keys(y)
    
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton) #скрипт заставляет прокрутить вниз до нужного элемента так, чтобы он полностью входил в область экрана
    radiobutton.click()
    
    button = browser.find_element(By.CLASS_NAME, "btn-primary").click()
finally:
    time.sleep(30)
    browser.quit()
    