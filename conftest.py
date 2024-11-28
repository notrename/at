import pytest
from selenium import webdriver
from lib.gostteam.fixtures import gost_team_page


# @pytest.fixture(scope='module')
# def browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

@pytest.fixture(scope='module')
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://chrome:4444/wd/hub',
        options=options
    )
    yield driver
    driver.quit()
