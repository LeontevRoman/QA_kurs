from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')

    picture = browser.find_element(by=By.ID, value='treasure')
    result = calc(picture.get_attribute('valuex'))

    browser.find_element(by=By.ID, value='answer').send_keys(result)

    browser.find_element(by=By.ID, value='robotCheckbox').click()

    browser.find_element(by=By.ID, value='robotsRule').click()

    browser.find_element(by=By.TAG_NAME, value='button').click()

finally:
    time.sleep(5)
    browser.quit()