from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Link:
    def __init__(self):
        pass

    def link_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Petrov")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys('Smolensk')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text
        browser.quit()

    def link_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Petrov")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys('Smolensk')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text
        browser.quit()