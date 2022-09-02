import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or ru")


@pytest.fixture()
def browser(request):
    # browser_language = request.config.getoption("language")
    browser = webdriver.Chrome()
    # options = Options()
    # if browser_language == 'en':
    #     options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    #     browser = webdriver.Chrome(options=options)
    # elif browser_language == 'ru':
    #     options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
    #     browser = webdriver.Chrome(options=options)
    # else:
    #     raise pytest.UsageError("--language should be en or ru")
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
