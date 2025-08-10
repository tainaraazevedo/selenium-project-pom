import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/")

    # run test
    yield

    # teardown
    driver.quit()
