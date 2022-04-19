from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class LoginPageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = 'document.querySelector("#username")'

# search elements
    def get_nav_links(self) -> WebElement :
        return self.are_visible('selector', self.__nav_links, 'Login Navigation Links')

    @property
    def get_nav_links(self) -> str:
        nav_links = self.get_nav_links
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)








