import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def browser():
    print('\n[+] Start test. Open browser. Please wait...')
    time.sleep(2)
    browser = webdriver.Chrome()
    yield browser
    print('\n[!] Quit browser. End test')
    browser.quit()


class TestParam:
    @pytest.mark.parametrize('number', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_parametrize(self, browser, number):
        link = f'https://stepik.org/lesson/{number}/step/1'
        browser.get(link)
        browser.implicitly_wait(3)
        answer = math.log(int(time.time()))
        browser.find_element(by=By.TAG_NAME, value='textarea').send_keys(answer)
        browser.find_element(by=By.CLASS_NAME, value='submit-submission').click()
        time.sleep(5)
        result = browser.find_element(by=By.CLASS_NAME, value='smart-hints__hint').text
        assert 'Correct!' == result, f'Oh, my GOD....WTF!!!! -----> {result}'
