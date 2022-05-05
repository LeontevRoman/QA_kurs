from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import math
import time
import os


try:
    browser: WebDriver = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    first_name = browser.find_element(by=By.NAME, value='firstname')
    first_name.send_keys('Роман')

    last_name = browser.find_element(by=By.NAME, value='lastname')
    last_name.send_keys('Леонтьев')

    e_mail = browser.find_element(by=By.NAME, value='email')
    e_mail.send_keys('roman@mail.ru')

    input_file = browser.find_element(by=By.ID, value='file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '../requirements.txt')  # добавляем к этому пути имя файла
    input_file.send_keys(file_path)

    button = browser.find_element(by=By.TAG_NAME, value='button')
    button.click()

    time.sleep(3)


finally:
    time.sleep(5)
    browser.quit()