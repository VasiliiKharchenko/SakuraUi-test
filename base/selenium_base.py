from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = wait = WebDriverWait(driver, 3, 0.3)

# Описание функции "By"
    def __get_selenium_by(self, find_by: str) -> dict:
            find_by = find_by.lower()
            locating = {'xpath': By.XPATH,
                        'css': By.CSS_SELECTOR,
                        'class_name': By.CLASS_NAME,
                        'id': By.ID,
                        'partial_link_text': By.PARTIAL_LINK_TEXT,
                        'tag_name': By.TAG_NAME,
                        'link_text': By.LINK_TEXT,
                        'name': By.NAME
            }
            return locating[find_by]

# ес - ожидание элемента/ов до появления далее тест продолжается
    def is_visible(self, find_by: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by))),
                                 locator_name)

    def is_present(self, find_by: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by))),
                                 locator_name)

    def is_not_present(self, find_by: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by))),
                                 locator_name)

    def are_visible(self, find_by: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by))),
                                 locator_name)

    def are_present(self, find_by: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by))),
                                 locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        return [link.text for link in nav_links]

# возвращает первый элемент из списка
    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name()
        return [element for element in elements if element.text == name][0]

# При удалении куки
#    def delete_cookie(self, cookie_name: str) -> None:
#        self.driver.delete_cookie(cookie_name)
























