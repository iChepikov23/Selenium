import time

from selenium.common.exceptions import TimeoutException

from Functions import readmail
from Locators.LocatorSettings import LocatorSettings
from Pages import PageFactory
from Pages.BasePage import BasePage

ROLE_ADMIN = 'Organization admin'


class PageSetting(BasePage):

    def user_role_admin(self):
        PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
            .click_button_settings() \
            .click_button_account_settings()
        if PageSetting(self.driver).wait_for_role():
            return PageSetting(self.driver).get_role() == ROLE_ADMIN
        else:
            return False

    def change_avatar(self):
        PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver,
                                    "leftmenu").mouse_over_left_menu().click_button_settings(

        ).click_button_account_settings()
        PageFactory.get_page_object(self.driver, "setting").change_image_profile().wait_for_click_image()
        PageFactory.get_page_object(self.driver, "setting").click_save_selected_image()
        if PageFactory.get_page_object(self.driver, "setting").wait_for_notify():
            return PageFactory.get_page_object(self.driver, "setting").get_notify_status().find("success") != -1
        else:
            return False

    def change_password(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        password = self.functions.generate_password()
        PageFactory.get_page_object(self.driver,
                                    "leftmenu").mouse_over_left_menu().click_button_settings(

        ).click_button_account_settings()
        PageFactory.get_page_object(self.driver, "setting").send_current_pass(login[1]).send_new_pass(
            password).send_confirm_pass(password) \
            .send_click_confirm_pass()
        PageFactory.get_page_object(self.driver, "leftmenu").do_logout()
        PageFactory.get_page_object(self.driver, "login").send_email(login[0]).send_password(
            login[1]).click_button_login()
        if PageFactory.get_page_object(self.driver, "login").exist_error_pass():
            return False
        PageFactory.get_page_object(self.driver, "login").send_email(login[0]).send_password(
            password).click_button_login()

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

        try:
            PageFactory.get_page_object(self.driver, "login").wait_nav_menu()
            return True
        except TimeoutException:
            return False

    def change_invalid_password(self, password):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver,
                                    "leftmenu").mouse_over_left_menu().click_button_settings(

        ).click_button_account_settings()
        PageFactory.get_page_object(self.driver, "setting").send_current_pass(login[1]).send_new_pass(
            password).send_confirm_pass(password) \
            .send_click_confirm_pass()
        return PageFactory.get_page_object(self.driver, "setting").wait_for_message_error_password()

    def change_invalid_password_similar(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        password = self.functions.generate_password()
        PageFactory.get_page_object(self.driver,
                                    "leftmenu").mouse_over_left_menu().click_button_settings(

        ).click_button_account_settings()
        PageFactory.get_page_object(self.driver, "setting").send_current_pass(login[1]).send_new_pass(
            password).send_confirm_pass(password + '2') \
            .send_click_confirm_pass()
        return PageFactory.get_page_object(self.driver, "setting").wait_for_message_error_password_similar()

    def send_fullname(self, fullname):
        self._input(LocatorSettings.settings_user_full_name, fullname)
        return self

    def send_username(self, username):
        self._input(LocatorSettings.settings_user_username, username)
        return self

    def click_update_profile(self):
        self._click(LocatorSettings.setting_update_profile_btn)
        return self

    def click_team_tab(self):
        self._click(LocatorSettings.team_tab_btn)

    def send_current_pass(self, password):
        # TODO
        time.sleep(1)
        self._input(LocatorSettings.user_current_pass, password)
        return self

    def send_new_pass(self, new_pass):
        self._input(LocatorSettings.user_new_pass, new_pass)
        return self

    def send_confirm_pass(self, new_pass):
        self._input(LocatorSettings.user_confirm_pass, new_pass)
        return self

    def send_click_confirm_pass(self):
        self._click(LocatorSettings.button_update_pass)
        return self

    def change_image_profile(self):
        self._upload(LocatorSettings.image_profile, self.functions.get_profile_photo())
        return self

    def click_save_selected_image(self):
        self._click(LocatorSettings.button_upload_image)
        return self

    def get_notify_status(self):
        if self.wait_for_role():
            return self._get_element(LocatorSettings.notify_message).get_attribute('innerHTML')
        else:
            return False

    def get_role(self):
        return self._get_element_attribute(LocatorSettings.user_role, 'value')

    def wait_for_role(self):
        return self._wait_for_visible(LocatorSettings.user_role)

    def wait_for_notify(self):
        return self._wait_for_visible(LocatorSettings.notify_message)

    def wait_for_click_image(self):
        return self._wait_for_enabled(LocatorSettings.button_upload_image)

    def wait_for_message_error_password(self):
        return self._wait_for_visible(LocatorSettings.message_password_invalid)

    def wait_for_message_error_password_similar(self):
        return self._wait_for_visible(LocatorSettings.message_password_no_similar)
