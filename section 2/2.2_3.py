from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    a = browser.find_element(By.ID, 'num1').text
    b = browser.find_element(By.ID, 'num2').text
    summa = int(a) + int(b)

    find = Select(browser.find_element(By.ID, 'dropdown'))
    find.select_by_value(str(summa))

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    print(summa)

finally:
    time.sleep(10)
    browser.quit()