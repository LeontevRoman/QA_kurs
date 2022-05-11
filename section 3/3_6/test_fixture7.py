from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope='function')
def browser():
    print('\n[+] start browser, please wait...')
    browser = webdriver.Chrome()
    yield browser
    print('\n[!] quit browser. end test')
    browser.quit()


@pytest.mark.parametrize('language', ['ru', 'en-gb'])
def test_guest_should_see_login_link(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/'
    browser.get(link)
    browser.find_element(by=By.CSS_SELECTOR, value='#login_link')
