import pytest
from selenium import webdriver

from lib.gostteam.page.gostteam_page import GostTeamPage


@pytest.fixture
def gost_team_page(browser: webdriver) -> GostTeamPage:
    return GostTeamPage(driver=browser)
