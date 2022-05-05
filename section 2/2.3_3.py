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

    '''input_numbers = browser.find_element(by=By.ID, value='input_value')
    x = input_numbers.text
    print(x)
    result = calc(x)

    capcha = browser.find_element(By.ID, 'answer')
    capcha.send_keys(result)

    button = browser.find_element(by=By.TAG_NAME, value="button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robot = browser.find_element(By.ID, 'robotCheckbox')
    robot.click()

    check = browser.find_element(By.ID, 'robotsRule')
    check.click()

    button.click()'''

    time.sleep(3)


finally:
    time.sleep(5)
    browser.quit()