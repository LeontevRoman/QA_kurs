from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button_1 = browser.find_element(by=By.TAG_NAME, value='button')
    button_1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    value = browser.find_element(by=By.ID, value='input_value')
    result = calc(value.text)

    result_label = browser.find_element(by=By.ID, value='answer')
    result_label.send_keys(result)

    button_2 = browser.find_element(by=By.TAG_NAME, value='button')
    button_2.click()

    time.sleep(3)

finally:
    time.sleep(5)
    browser.quit()
