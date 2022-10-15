import time

from Locators.LocatorLeftMenu import LocatorLeftMenu
from Locators.LocatorRegistration import LocatorRegistration
from Pages.BasePage import BasePage


class PageUserRegistration(BasePage):
    # Register User Page

    def send_email(self, email):
        self._input(LocatorRegistration.registration_user_email, email)
        return self

    def click_button_next(self):
        # TODO
        time.sleep(2)
        self._click(LocatorRegistration.registration_user_button_next)
        return self

    def send_fullname(self, fullname):
        self._input(LocatorRegistration.registration_user_fullname, fullname)
        return self

    def send_name(self, name):
        self._input(LocatorRegistration.registration_user_name, name)
        return self

    def send_organization(self, organization):
        self._input(LocatorRegistration.registration_user_organization, organization)
        return self

    def send_password(self, password):
        self._input(LocatorRegistration.registration_user_password, password)
        return self

    def click_button_sign_up(self):
        # TODO
        time.sleep(2)
        self._click(LocatorRegistration.registration_user_button_sign_up)

    def click_button_sign_up_invitation(self):
        # TODO
        time.sleep(2)
        self._click(LocatorRegistration.registration_user_invitation_button_sign_up)

    def click_tetra_icon(self):
        self._click(LocatorRegistration.registration_user_tetra_icon)

    def wait_email_duplicate(self):
        self._wait_for_visible(LocatorRegistration.registration_user_error_duplicate)

    def exist_email_duplicate(self):
        return self._exist_element(LocatorRegistration.registration_user_error_duplicate)

    def is_enabled_registration(self):
        return self._element(LocatorRegistration.registration_user_button_next).is_enabled()

    def is_enabled_sign_up(self):
        return self._element(LocatorRegistration.registration_user_button_sign_up).is_enabled()

    def wait_organization_duplicate(self):
        self._wait_for_visible(LocatorRegistration.registration_user_msg_duplicate_organization)

    def exist_organization_duplicate(self):
        return self._exist_element(LocatorRegistration.registration_user_msg_duplicate_organization)

    def wait_error_pass(self):
        self._wait_for_visible(LocatorRegistration.registration_user_msg_bad_password)

    def exist_error_pass(self):
        return self._exist_element(LocatorRegistration.registration_user_msg_bad_password)

    def exist_error_pass(self):
        return self._exist_element(LocatorRegistration.registration_user_msg_bad_password)

    def wait_login(self):
        self._wait_for_visible(LocatorLeftMenu.nav_menu)

    def exist_login(self):
        return self._exist_element(LocatorLeftMenu.nav_menu)
