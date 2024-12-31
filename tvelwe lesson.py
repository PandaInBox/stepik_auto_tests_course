from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/alert_accept.html")
    
    button = browser.find_element(By.CLASS_NAME, "btn-primary").click()
    
    alert = browser.switch_to.alert #Переключение взаимодействия на появившийся алекрт
    alert.accept() # подтверждение алекта
    
    x_value = browser.find_element(By.ID, "input_value").text
    y = calc(x_value)
    
    answer = browser.find_element(By.ID, "answer").send_keys(y)
    
    btn2 = browser.find_element(By.CLASS_NAME, "btn-primary").click()
finally:
    time.sleep(30)
    browser.quit()