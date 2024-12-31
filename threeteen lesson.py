from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/redirect_accept.html")
    
    btn = browser.find_element(By.CLASS_NAME, "trollface").click()
    
    new_window = browser.window_handles[1] #задаю переменную которой присваиваю номер вкладки
    
    browser.switch_to.window(new_window) # использую предыдущую переменную переключаю активное окно для взаимодействия
    
    
    x_value = browser.find_element(By.ID, "input_value").text
    y = calc(x_value)
    
    answer = browser.find_element(By.ID, "answer").send_keys(y)
    
    btn2 = browser.find_element(By.CLASS_NAME, "btn-primary").click()
    
finally:
    time.sleep(20)
    browser.quit()