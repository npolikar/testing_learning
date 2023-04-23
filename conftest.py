import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: XXX or YYY")


@pytest.fixture(scope="function")
def browser(request):
    languages_list = ["ru", "es", "fr", "en"]
    browser_language = request.config.getoption("language")
    if not browser_language:
        browser_language = "en"
    if browser_language in languages_list:
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError(f"--language should be in {languages_list}")
    yield browser, browser_language
    print("\nquit browser..")
    browser.quit()
