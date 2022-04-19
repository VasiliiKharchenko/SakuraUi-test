import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from  selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestLoginPage:

    def test_login_page(self):
        LoginPage_nav = LoginPageNav(self.driver)
        actual_links = LoginPage_nav.get_nav_links_text()
        expected_links = LoginPage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validating Nav Links text'
# Прокликать все элементы которые найдутся на странице + запрос нового списка после каждого клика
#        for index in range(12):
#            login_page_nav()[index].click()
#            login_page_nav.driver.delete_all_cookies()
#            time.sleep(3)
        login_page_nav.get_nav_link_by_name('Имя').click()
        time.sleep(3)   # wait for test some seconds



















