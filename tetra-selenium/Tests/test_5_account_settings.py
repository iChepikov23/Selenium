import allure
import pytest

from Pages import PageFactory


@pytest.mark.usefixtures("myDriver")
class TestAccountSettings:

    @allure.feature('Registration')
    @allure.story('XRAY-4 - Check Role Admin')
    @pytest.mark.flaky(reruns=3)
    def test_user_role_admin(self):
        assert PageFactory.get_page_object(self.driver, "setting").user_role_admin()

    @allure.feature('Account Setting')
    @allure.story('Change avatar')
    @pytest.mark.flaky(reruns=3)
    def test_change_avatar(self):
        assert PageFactory.get_page_object(self.driver, "setting").change_avatar()

    @allure.feature('Account Setting')
    @allure.story('XRAY-6 - Change Password')
    @pytest.mark.flaky(reruns=3)
    def test_change_password(self):
        assert PageFactory.get_page_object(self.driver, "setting").change_password()

    @allure.feature('Account Setting')
    @allure.story('XRAY-6 - Cant change invalid password')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('password',
                             ['Pass*1234', 'password', 'password*', 'password45', 'password45*.', 'Password*-',
                              'Password45', 'PASSWORD*12'])
    def test_change_invalid_password(self, password):
        assert PageFactory.get_page_object(self.driver, "setting").change_invalid_password(password)

    @allure.feature('Account Setting')
    @allure.story('XRAY-6 - Cant change invalid password')
    @pytest.mark.flaky(reruns=3)
    def test_change_invalid_password(self, ):
        assert PageFactory.get_page_object(self.driver, "setting").change_invalid_password_similar()
