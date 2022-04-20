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


# Прокликивание элементов на странице с удалением куки, которая определяет тест как робот
#    def test_login_page_links(self):
#        login_page_nav = TestLoginPage(self.driver)
#        cookies = login_page_nav.driver.get_cookies()
#        cookies_names = [cookie['name'] for cookie in cookies]
#        print(cookie)
#        print('-------------------')
#        print(cookies_names)
#        for index in range(12):
#            login_page_nav.get_nav_links()[index].click()
#            for cookie_name in cookies_names:
#                login_page_nav.driver.delete_cookie(cookie_name)
#                login_page_nav.driver.refresh()
#                login_page_nav.is_visible('tag_name', 'h1', cookie_name)

#                time.sleep(1)

#   Тест после нахождения куки которая ломала доступ name-название куки
#    def test_nav_links(self):
#        LoginPage_nav = LoginPageNav(self.driver)
#        LoginPage_nav.driver.delete_cookie('name')
#        for index in range(12):
#            LoginPage_nav.get_nav_links()[index].click()
#            LoginPage_nav.driver.delete_cookie('name')












