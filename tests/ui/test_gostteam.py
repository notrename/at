import pytest

from lib.gostteam.page.gostteam_page import GostTeamPage


class TestGostTeam:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, gost_team_page: GostTeamPage):
        self.page = gost_team_page

    def test_main_page(self):
        self.page.open()
        self.page.xpath_is_present(xpath='//title')
        self.page.switch_to_eng()
      