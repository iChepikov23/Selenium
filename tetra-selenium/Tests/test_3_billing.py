import allure
import pytest

from Pages import PageFactory


@pytest.mark.usefixtures("myDriver")
class TestBilling:

    @allure.feature('Registration')
    @allure.story('XRAY-4 - Billing Tab')
    @pytest.mark.flaky(reruns=3)
    def test_billing_tab(self):
        assert PageFactory.get_page_object(self.driver, "billing").exist_billing_tab()

    @allure.feature('Registration')
    @allure.story('XRAY-4 - Check billing plan')
    @pytest.mark.flaky(reruns=3)
    def test_basic_plan(self):
        assert PageFactory.get_page_object(self.driver, "billing").basic_plan()

    @allure.feature('Registration')
    @allure.story('Check billing plan')
    @pytest.mark.flaky(reruns=3)
    def test_plan_details(self):
        assert PageFactory.get_page_object(self.driver, "billing").show_plan_details()

    @allure.feature('Registration')
    @allure.story('Contact us')
    @pytest.mark.flaky(reruns=3)
    def test_contact_us(self):
        assert PageFactory.get_page_object(self.driver, "billing").show_contact_us()

    @allure.feature('Registration')
    @allure.story('Add valid credit card')
    @pytest.mark.flaky(reruns=3)
    def test_add_valid_credit_card(self):
        assert PageFactory.get_page_object(self.driver, "billing").add_valid_credit_card()

    @allure.feature('Add invalid credit card')
    @allure.story('Check billing plan')
    @pytest.mark.flaky(reruns=3)
    def test_add_invalid_number_credit_card(self):
        assert PageFactory.get_page_object(self.driver, "billing").add_invalid_number_credit_card()

    @allure.feature('Registration')
    @allure.story('Add invalid bank account')
    @pytest.mark.flaky(reruns=3)
    def test_add_invalid_bank(self):
        assert PageFactory.get_page_object(self.driver, "billing").add_invalid_bank_account()
