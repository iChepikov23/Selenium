from Locators.LocatorLeftMenu import LocatorLeftMenu
from Locators.LocatorLogin import LocatorLogin
from Pages.BasePage import BasePage


class PageUserLogin(BasePage):

    def user_login(self, profile):
        # Select create account
        df = self.functions.get_account_created_from_file(profile)
        self.send_email(df[0]).send_password(df[1]).click_button_login()
        self._wait_for_visible(LocatorLeftMenu.nav_menu)
        result = [df[0], df[1], df[2]]
        return result

    def send_email(self, email):
        self._input(LocatorLogin.login_user_email, email)
        return self

    def send_password(self, password):
        self._input(LocatorLogin.login_user_password, password)
        return self

    def click_button_login(self):
        self._click(LocatorLogin.login_user_button_login)

    def click_button_next(self):
        self._click(LocatorLogin.registration_user_button_next)

    def click_forgot_password(self):
        self._click(LocatorLogin.login_user_link_forgot_password)

    def click_create_account(self):
        self._click(LocatorLogin.login_user_link_create_account)

    def wait_nav_menu(self):
        self._wait_for_visible(LocatorLeftMenu.nav_menu)

    def exist_nav_menu(self):
        self._exist_element(LocatorLeftMenu.nav_menu)

    def wait_error_pass(self):
        self._wait_for_visible(LocatorLogin.login_message_bad_password)

    def exist_error_pass(self):
        self._exist_element(LocatorLogin.login_message_bad_password)
