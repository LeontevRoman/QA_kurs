from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element(by=By.ID, value='book').click()

    result = calc(browser.find_element(by=By.ID, value='input_value').text)

    browser.find_element(by=By.ID, value='answer').send_keys(result)
    browser.find_element(by=By.ID, value='solve').click()


finally:
    time.sleep(5)
    browser.quit()