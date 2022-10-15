import time

from Locators.LocatorLeftMenu import LocatorLeftMenu
from Locators.LocatorLogin import LocatorLogin
from Locators.LocatorRegistration import LocatorRegistration
from Pages import PageFactory
from Pages.BasePage import BasePage
from Functions import readmail


class PageLogin(BasePage):

    def user_login(self):
        # Select create account
        b_result = PageFactory.get_page_object(self.driver, "registration").user_registration()

        if b_result:
            self.send_email(b_result[0]).send_password(b_result[1]).click_button_login()
            if self._wait_for_present(LocatorLogin.login_request_code):
                link = None
                i = 0
                # 10 times
                while link is None and i < 20:
                    link = readmail.read_two_step_mail()
                    i = i + 1
                if link is not None:
                    PageFactory.get_page_object(self.driver, "login").send_two_factor(link)
                    PageFactory.get_page_object(self.driver, "login").click_two_factor()
                    PageFactory.get_page_object(self.driver, "login").wait_login()
                    return True
                else:
                    return False
            else:
                self.wait_login()
                self._wait_for_visible(LocatorLeftMenu.nav_menu)
                return True
        else:
            return None

    # Profile, Plan, Teammates, Projects
    def user_login_parameters(self, profile='A', plan='Premium', teammates=0, projects=0, payment=0):
        # Select create account
        df = self.functions.get_account_created_from_file(profile)
        df_result = None
        i = 0
        if df[4] == plan and df[5] <= teammates and df[6] <= projects and df[7] == payment:
            df_result = df
        else:
            while i < 30:
                df = self.functions.get_account_created_from_file(profile)
                if df[4] == plan and df[5] <= teammates and df[6] <= projects and df[7] == payment:
                    df_result = df
                    break
                i = i + 1
        if df_result:
            self.send_email(df_result[0]).send_password(df_result[1]).click_button_login()
            self.wait_login()
            self._wait_for_visible(LocatorLeftMenu.nav_menu)
            df_result = [df_result[0], df_result[1], df_result[2], df_result[3], df_result[4], df_result[5],
                         df_result[6], df_result[7]]
        else:
            raise Exception("Sorry, account with the criteria has not been found")
        return df_result

    def user_login_more_projects(self, profile='A', plan='Premium', projects=0):
        # Select create account
        df = self.functions.get_account_created_from_file(profile)
        df_result = None
        i = 0
        if df[4] == plan and df[6] >= projects:
            df_result = df
        else:
            while i < 30:
                df = self.functions.get_account_created_from_file(profile)
                if df[4] == plan and df[6] >= projects:
                    df_result = df
                    break
                i = i + 1
        if df_result:
            self.send_email(df_result[0]).send_password(df_result[1]).click_button_login()
            self.wait_login()
            self._wait_for_visible(LocatorLeftMenu.nav_menu)
            df_result = [df_result[0], df_result[1], df_result[2], df_result[3], df_result[4], df_result[5],
                         df_result[6], df_result[7]]
        else:
            raise Exception("Sorry, account with the criteria has not been found")
        return df_result

    def user_login_more_teammates(self, profile='A', plan='Premium', teammates=1):
        # Select create account
        df = self.functions.get_account_created_from_file(profile)
        df_result = None
        i = 0
        if df[4] == plan and df[5] >= teammates:
            df_result = df
        else:
            while i < 30:
                df = self.functions.get_account_created_from_file(profile)
                if df[4] == plan and df[5] >= teammates:
                    df_result = df
                    break
                i = i + 1
        if df_result:
            self.send_email(df_result[0]).send_password(df_result[1]).click_button_login()
            self.wait_login()
            self._wait_for_visible(LocatorLeftMenu.nav_menu)
            df_result = [df_result[0], df_result[1], df_result[2], df_result[3], df_result[4], df_result[5],
                         df_result[6], df_result[7]]
        else:
            raise Exception("Sorry, account with the criteria has not been found")
        return df_result

    def user_login_less_teammates(self, profile='A', plan='Premium', teammates=9):
        # Select create account
        df = self.functions.get_account_created_from_file(profile)
        df_result = None
        i = 0
        if df[4] == plan and df[5] < teammates:
            df_result = df
        else:
            while i < 30:
                df = self.functions.get_account_created_from_file(profile)
                if df[4] == plan and df[5] < teammates:
                    df_result = df
                    break
                i = i + 1
        if df_result:
            self.send_email(df_result[0]).send_password(df_result[1]).click_button_login()
            self.wait_login()
            self._wait_for_visible(LocatorLeftMenu.nav_menu)
            df_result = [df_result[0], df_result[1], df_result[2], df_result[3], df_result[4], df_result[5],
                         df_result[6], df_result[7]]
        else:
            raise Exception("Sorry, account with the criteria has not been found")
        return df_result

    def user_login_by_email(self, email):
        # Select create account
        df = self.functions.get_account_from_file_by_login(email)
        self.send_email(df[0]).send_password(df[1]).click_button_login()
        self.wait_login()
        self._wait_for_visible(LocatorLeftMenu.nav_menu)
        result = [df[0], df[1], df[2], df[3], df[4], df[5], df[6], df[7]]
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
        self._wait_for_visible(LocatorRegistration.registration_user_button_next)
        self._wait_for_enabled(LocatorRegistration.registration_user_button_next)
        self._click(LocatorRegistration.registration_user_button_next)

    def click_forgot_password(self):
        self._wait_for_visible(LocatorRegistration.login_user_link_forgot_password)
        self._wait_for_enabled(LocatorRegistration.login_user_link_forgot_password)
        self._click(LocatorLogin.login_user_link_forgot_password)

    def click_create_account(self):
        time.sleep(3)
        self._wait_for_visible(LocatorLogin.login_user_link_create_account)
        self._click(LocatorLogin.login_user_link_create_account)
    def wait_nav_menu(self):
        return self._wait_for_visible(LocatorLeftMenu.nav_menu)

    def exist_nav_menu(self):
        self._exist_element(LocatorLeftMenu.nav_menu)

    def wait_error_pass(self):
        return self._wait_for_visible(LocatorLogin.login_message_bad_password)

    def exist_error_pass(self):
        self._exist_element(LocatorLogin.login_message_bad_password)

    def wait_login(self):
        self._wait_for_visible(LocatorLogin.login_notify)
        self._wait_for_invisibility(LocatorLogin.login_notify)

    def wait_first_login(self):
        self._wait_for_enabled_text(LocatorLogin.login_back_sign, 'Back to sign in')

    def click_back(self):
        time.sleep(2)
        self._wait_for_visible_element(LocatorLogin.login_back_sign)
        self._wait_for_clickable(LocatorLogin.login_back_sign)
        self._wait_for_enabled(LocatorLogin.login_back_sign)
        self._mouse_over(LocatorLogin.login_back_sign)
        self._click(LocatorLogin.login_back_sign)

    def send_two_factor(self, code):
        self._input(LocatorLogin.login_request_code, code)
        return self

    def click_two_factor(self):
        self._click(LocatorLogin.login_request_submit)

    def two_factor(self):
        self._exist_element(LocatorLeftMenu.login_request_code)
