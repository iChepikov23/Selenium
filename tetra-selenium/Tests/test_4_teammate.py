import allure
import pytest

from Pages import PageFactory


@pytest.mark.usefixtures("myDriver")
class TestTeammate:

    @allure.story('Teammates')
    @allure.feature('Invite Teammate')
    @pytest.mark.flaky(reruns=3)
    def test_teammate(self):
        assert PageFactory.get_page_object(self.driver, "teammate").invite_teammate()
