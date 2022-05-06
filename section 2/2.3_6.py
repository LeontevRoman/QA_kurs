from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    button = browser.find_element(by=By.TAG_NAME, value='button')
    button.click()

    names_windows = browser.window_handles
    browser.switch_to.window(names_windows[1])

    print(names_windows[1])

    value = browser.find_element(by=By.ID, value='input_value')
    result = calc(value.text)

    result_label = browser.find_element(by=By.ID, value='answer')
    result_label.send_keys(result)

    button_1 = browser.find_element(by=By.TAG_NAME, value='button')
    button_1.click()

    time.sleep(2)
finally:
    time.sleep(5)
    browser.quit()
