import time

from Locators.LocatorBilling import LocatorBilling
from Pages import PageFactory
from Pages.BasePage import BasePage

url_plan_details = 'https://www.tetrainsights.com/pricing/'
url_contact_us = 'https://explore.tetrainsights.com/contact-tetra-insights'


class PageBilling(BasePage):
    CLASS_ACTIVE_PLAN = 'card-body active-plan'

    def exist_billing_tab(self):
        PageFactory.get_page_object(self.driver, "login").user_login()
        # show billing
        return PageFactory.get_page_object(self.driver,
                                           "leftmenu").mouse_over_left_menu().click_button_settings().exist_billings()

    def basic_plan(self):
        PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
            .click_button_settings() \
            .wait_billings()
        PageFactory.get_page_object(self.driver, "leftmenu").click_billing()
        return PageFactory.get_page_object(self.driver, "billing").wait_basic_pan()

    def show_plan_details(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
            .click_button_settings() \
            .wait_billings()
        PageFactory.get_page_object(self.driver, "leftmenu").click_billing()
        PageFactory.get_page_object(self.driver, "billing").wait_for_contact_us()
        # TODO
        time.sleep(2)
        PageFactory.get_page_object(self.driver, "billing").click_plan_details()
        bReturn = False
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if url_plan_details == self.driver.current_url:
                bReturn = True
                break
        return bReturn

    def show_contact_us(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
            .click_button_settings() \
            .wait_billings()
        PageFactory.get_page_object(self.driver, "leftmenu").click_billing()
        PageFactory.get_page_object(self.driver, "billing").wait_for_contact_us()
        # TODO
        time.sleep(2)
        PageFactory.get_page_object(self.driver, "billing").click_contact_us()
        bReturn = False
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if url_contact_us == self.driver.current_url:
                bReturn = True
                break
        return bReturn

    def add_valid_credit_card(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
            .click_button_settings() \
            .wait_billings()
        PageFactory.get_page_object(self.driver, "leftmenu").click_billing()
        # TODO
        time.sleep(2)
        PageFactory.get_page_object(self.driver, "billing").add_number_valid()
        PageFactory.get_page_object(self.driver, "billing").click_add_button_methods()
        return PageFactory.get_page_object(self.driver, "billing").wait_for_primary()

    def add_invalid_number_credit_card(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
            .click_button_settings() \
            .wait_billings()
        PageFactory.get_page_object(self.driver, "leftmenu").click_billing()
        # TODO
        time.sleep(2)
        PageFactory.get_page_object(self.driver, "billing").add_number_verification_error_card()
        PageFactory.get_page_object(self.driver, "billing").click_add_button_methods()
        if PageFactory.get_page_object(self.driver, "billing").wait_for_error_number():
            PageFactory.get_page_object(self.driver, "billing").click_cancel_button_methods()
            return True
        else:
            return False

    def add_invalid_bank_account(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
            .click_button_settings() \
            .wait_billings()
        PageFactory.get_page_object(self.driver, "leftmenu").click_billing()
        # TODO
        time.sleep(2)
        PageFactory.get_page_object(self.driver, "billing").add_number_transaction_error_card()
        PageFactory.get_page_object(self.driver, "billing").click_add_button_methods()
        self.driver.switch_to.default_content()
        PageFactory.get_page_object(self.driver, "billing").wait_for_mem_plan()
        PageFactory.get_page_object(self.driver, "billing").click_mem_plan()
        PageFactory.get_page_object(self.driver, "billing").click_update_premium()
        PageFactory.get_page_object(self.driver, "billing").click_purchase()
        PageFactory.get_page_object(self.driver, "billing").wait_for_update_problem()
        PageFactory.get_page_object(self.driver, "billing").click_problem()
        PageFactory.get_page_object(self.driver, "billing").click_back_error_update()
        return PageFactory.get_page_object(self.driver, "billing").wait_basic_pan()

    def update_premium(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
            .click_button_settings() \
            .wait_billings()
        PageFactory.get_page_object(self.driver, "leftmenu").click_billing()
        PageFactory.get_page_object(self.driver, "billing").click_update_premium()
        PageFactory.get_page_object(self.driver, "billing").click_purchase()
        PageFactory.get_page_object(self.driver, "billing").wait_for_upgraded()
        PageFactory.get_page_object(self.driver, "billing").click_back()
        return PageFactory.get_page_object(self.driver, "billing").wait_premium_pan()

    def verify_noupdate_premium(self):
        PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
            .click_button_settings() \
            .wait_billings()
        PageFactory.get_page_object(self.driver, "leftmenu").click_billing()
        PageFactory.get_page_object(self.driver, "billing").click_update_premium()
        PageFactory.get_page_object(self.driver, "billing").click_purchase()
        if PageFactory.get_page_object(self.driver, "billing").wait_for_upgraded():
            return False
        else:
            return True

    #############################################################
    #                      Actions                              #
    #############################################################
    def get_basic_plan_class(self):
        if self.wait_basic_pan():
            return self._get_element_attribute(LocatorBilling.billing_plan_basic, 'class')
        else:
            return False

    def get_premium_plan_class(self):
        return self._get_element_attribute(LocatorBilling.billing_plan_premium, 'class')

    def get_enterprise_plan_class(self):
        return self._get_element_attribute(LocatorBilling.billing_plan_enterprise, 'class')

    def wait_basic_pan(self):
        return self._wait_for_class(LocatorBilling.billing_plan_basic, PageBilling.CLASS_ACTIVE_PLAN)

    def wait_premium_pan(self):
        return self._wait_for_class(LocatorBilling.billing_plan_premium, PageBilling.CLASS_ACTIVE_PLAN)

    def click_tad_payments_methods(self):
        self._click(LocatorBilling.billing_tab_methods)
        return self

    def click_update_premium(self):
        self._click(LocatorBilling.billing_update_premium)

    def click_mem_plan(self):
        self._click(LocatorBilling.billing_mem_plan)

    def wait_for_mem_plan(self):
        self._wait_for_visible(LocatorBilling.billing_mem_plan)

    def click_purchase(self):
        self._click(LocatorBilling.billing_purchase_order)

    def click_add_button_methods(self):
        self._click(LocatorBilling.billing_add_button)
        return self

    def click_add_input_methods(self):
        self._click(LocatorBilling.billing_input_card)
        return self

    def wait_tap_payments_methods(self):
        return self._wait_for_visible_element(LocatorBilling.billing_tab_methods)

    def wait_add_button_payments_methods(self):
        return self._wait_for_fully(LocatorBilling.billing_add_button)

    def wait_for_contact_us(self):
        return self._wait_for_visible(LocatorBilling.billing_contact_us_button)

    def wait_for_primary(self):
        return self._wait_for_enabled_text(LocatorBilling.billing_primary_span, 'PRIMARY')

    def wait_for_error_number(self):
        return self._wait_for_enabled_text(LocatorBilling.billing_cancel_error_number, 'Cancel')

    def wait_for_upgraded(self):
        return self._wait_for_enabled_text(LocatorBilling.billing_txt_upgraded, "YOU'RE UPGRADED TO PREMIUM!")

    def wait_for_update_problem(self):
        return self._wait_for_clickable(LocatorBilling.billing_update_problem)

    def click_problem(self):
        return self._click(LocatorBilling.billing_update_problem)

    def click_cancel_button_methods(self):
        self._click(LocatorBilling.billing_cancel_error_number)
        return self

    def click_plan_details(self):
        self._click(LocatorBilling.billing_plan_details)
        return self

    def click_contact_us(self):
        self._click(LocatorBilling.billing_contact_us_button)
        return self

    def click_back(self):
        self._click(LocatorBilling.billing_back)
        return self

    def add_number_valid(self):
        self._wait_for_present(LocatorBilling.billing_frame_pay)
        PageFactory.get_page_object(self.driver, "billing").click_tad_payments_methods()
        time.sleep(3)
        self.driver.switch_to.frame("paymentIframe")
        self._input(LocatorBilling.billing_number, '4111 1111 1111 1111')
        self._input(LocatorBilling.billing_month, '12')
        self._input(LocatorBilling.billing_year, '2029')
        self._input(LocatorBilling.billing_cvv, '123')

    def add_number_verification_error_card(self):
        self._wait_for_present(LocatorBilling.billing_frame_pay)
        PageFactory.get_page_object(self.driver, "billing").click_tad_payments_methods()
        time.sleep(3)
        self.driver.switch_to.frame("paymentIframe")
        self._input(LocatorBilling.billing_number, '4119 8627 6033 8320')
        self._input(LocatorBilling.billing_month, '12')
        self._input(LocatorBilling.billing_year, '2029')
        self._input(LocatorBilling.billing_cvv, '123')

    def add_number_transaction_error_card(self):
        self._wait_for_present(LocatorBilling.billing_frame_pay)
        PageFactory.get_page_object(self.driver, "billing").click_tad_payments_methods()
        time.sleep(3)
        self.driver.switch_to.frame("paymentIframe")
        self._input(LocatorBilling.billing_number, '4005 5192 0000 0004')
        self._input(LocatorBilling.billing_month, '12')
        self._input(LocatorBilling.billing_year, '2029')
        self._input(LocatorBilling.billing_cvv, '123')

    def click_back_error_update(self):
        self._click(LocatorBilling.login_back_problem_order)
