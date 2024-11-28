import pytest
from selenium import webdriver
from lib.gostteam.fixtures import gost_team_page


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

