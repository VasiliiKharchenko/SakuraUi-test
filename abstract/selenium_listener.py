from selenium.webdriver.support.events import AbstractEventListener


# создание класса по удалению куки которая блочила переходы
class MyListener(AbstractEventListener):

    def before_click(self, element, driver):
        driver.delete_cookie('name')

    def after_click(self, element, driver):
        driver.delete_cookie('name')

