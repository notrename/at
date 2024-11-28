from selenium.webdriver.remote.webdriver import WebDriver

from lib.gostteam.elements.main_page_elements import MainPageElements
from utils.page import Page


class GostTeamPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.url = 'https://gost.team/'
        self.__elements = MainPageElements(driver=driver)

    @property
    def elems(self):
        return self.__elements

    def open(self):
        self.open_site(url=self.url)

    def switch_to_eng(self):
        self.elems.link_to_eng_version.click()

