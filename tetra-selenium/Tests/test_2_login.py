import allure
import pytest

from Pages import PageFactory


@pytest.mark.usefixtures("myDriver")
class TestLogin:

    @allure.feature('Login')
    @allure.story('User Login')
    @pytest.mark.flaky(reruns=3)
    def test_login(self):
        assert PageFactory.get_page_object(self.driver, "login").user_login()
