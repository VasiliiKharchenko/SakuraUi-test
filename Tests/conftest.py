import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

# настройки браузера
@pytest.fixture
def get_chrome_options():
    options = chrome_options() # https://peter.sh/experiments/chromium-command-line-switches/ что можно делать с хром
    options.add_argument('chrome')  # Use "headless" if you do not need a browser UI
    options.add_argument('--start-maximized') # окно открыто во всю
    options.add_argument('--window-size=1688,768') # задать расширение окна для тестов
    return options

# Инициализация драйвера он добавлен в директорию проекта, в другом случае прописываем путь к нему
@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver

# подготовка для теста
@pytest.fixture(scope='function') # function для запуска паралельных тестов
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'http://sakuratest.cloud.tehnosk.ru/uaa/login.html' # сменить на тестовый стенд
    if request.cls is not None:     # if dont use class for tests
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies() # По необходимости если на сайте защита от роботов и сбора данных
    yield driver
    driver.quit()  # quit закрывает весь браузер, при условии запуска параллельных тестов












