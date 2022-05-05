from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/math.html')

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

capcha = browser.find_element(By.ID, 'answer')
capcha.send_keys(y)

robot = browser.find_element(By.ID, 'robotCheckbox')
robot.click()

check = browser.find_element(By.ID, 'robotsRule')
check.click()


time.sleep(3)


button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
button.click()

time.sleep(10)
browser.quit()

