import allure
import pytest

from Pages import PageFactory


@pytest.mark.usefixtures("myDriver" , "myEnvironment")
class TestRegistration:

    @allure.feature('User Registration')
    @allure.story('Click Back icon')
    @pytest.mark.flaky(reruns=3)
    def test_user_registration_back_icon(self, myEnvironment):
        assert PageFactory.get_page_object(self.driver, "registration").user_registration_back_icon(myEnvironment)

    @allure.feature('User Registration')
    @allure.story('XRAY-3 - Sign Up')
    @pytest.mark.flaky(reruns=3)
    def test_user_registration(self):
        b_result = PageFactory.get_page_object(self.driver, "registration").user_registration()
        if b_result:
            assert True
        else:
            assert False

    @allure.feature('User Registration')
    @allure.story('XRAY-3 - Email duplicated')
    @pytest.mark.flaky(reruns=3)
    def test_user_registration_duplicate_mail(self):
        assert PageFactory.get_page_object(self.driver, "registration").user_registration_duplicate_mail()

    @allure.feature('User Registration')
    @allure.story('Invalid Mail')
    @pytest.mark.flaky(reruns=3)
    def test_user_registration_error_mail(self):
        assert PageFactory.get_page_object(self.driver, "registration").user_registration_error_mail()

    @allure.feature('User Registration')
    @allure.story('Sign disabled')
    @pytest.mark.flaky(reruns=3)
    def test_sign_up_button_disable(self):
        assert PageFactory.get_page_object(self.driver, "registration").sign_up_button_disable()

    @allure.feature('User Registration')
    @allure.story('Duplicated organization')
    @pytest.mark.flaky(reruns=3)
    def test_user_registration_duplicate_organization(self):
        assert PageFactory.get_page_object(self.driver, "registration").user_registration_duplicate_organization()

    @allure.feature('User Registration')
    @allure.story('User Terms')
    @pytest.mark.flaky(reruns=3)
    def test_user_registration_terms(self):
        assert PageFactory.get_page_object(self.driver, "registration").user_registration_terms()

    @allure.feature('User Registration')
    @allure.story('Invalid password')
    @pytest.mark.flaky(reruns=3)
    def test_user_registration_policy(self):
        assert PageFactory.get_page_object(self.driver, "registration").user_registration_policy()

    @allure.feature('Test Valid Password')
    @allure.story('Sign Up')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('password', ['New_password1*', 'Password2+', '**MYAWES0mePass'])
    def test_valid_password(self, password):
        b_result = PageFactory.get_page_object(self.driver, "registration").user_registration_valid_pass(password)
        if b_result:
            assert True
        else:
            assert False

    @allure.feature('Test Valid Password')
    @allure.story('Sign Up')
    @pytest.mark.flaky(reruns=3)
    @pytest.mark.parametrize('password',
                             ['Pass*1234', 'password', 'password*', 'password45', 'password45*.', 'Password*-',
                              'Password45', 'PASSWORD*12'])
    def test_invalid_password(self, password):
        b_result = PageFactory.get_page_object(self.driver, "registration").user_registration_valid_pass(password)
        if b_result:
            assert False
        else:
            assert True
