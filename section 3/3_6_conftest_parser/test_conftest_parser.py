from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(by=By.CSS_SELECTOR, value="#login_link")
    time.sleep(10)