import pytest
from selenium import webdriver
from testdata import constants as dataval

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope = "class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\Users\\prakash\\PycharmProjects\\demotours\\drivers\\chromedriver.exe")
    elif browser == 'ff':
        driver = webdriver.Firefox()
    driver.get(dataval.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    # yield
    # driver.quit()