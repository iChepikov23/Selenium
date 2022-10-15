import time

from Locators.LocatorLeftMenu import AccountSetting
from Locators.LocatorLeftMenu import InviteTeammate
from Locators.LocatorLeftMenu import LocatorLeftMenu
from Locators.LocatorLeftMenu import Settings
from Pages.BasePage import BasePage


class PageLeftMenu(BasePage):

    def mouse_over_left_menu(self):
        self._mouse_over(LocatorLeftMenu.nav_menu)
        return self

    def click_button_settings(self):
        self._click(LocatorLeftMenu.settings)
        return self

    def click_button_account_settings(self):
        self.driver.implicitly_wait(5)
        self._mouse_over(LocatorLeftMenu.nav_menu)
        self._click(Settings.account_settings)
        return self

    def click_button_teammate(self):
        self._wait_for_enabled(LocatorLeftMenu.invite_teammate)
        self._click(LocatorLeftMenu.invite_teammate)
        return self

    def click_billing(self):
        self._mouse_over(LocatorLeftMenu.nav_menu)
        self._click(Settings.billing)
        return self

    def wait_billings(self):
        return self._wait_for_visible(Settings.billing)

    def wait_account_settings(self):
        return self._wait_for_visible(Settings.account_settings)

    def click_account_settings(self):
        self._mouse_over(LocatorLeftMenu.nav_menu)
        self._click(Settings.account_settings)
        return self

    def click_team(self):
        self._click(AccountSetting.team)
        return self

    def get_new_teammate(self):
        self._get_element(AccountSetting.new_invite).text

    def exist_billings(self):
        self._exist_element(Settings.billing)
        return self

    def click_logout(self):
        self._click(Settings.logout)

    def send_teammate_mail(self, email):
        self._input(InviteTeammate.teammate_mail, email)

    def is_enabled_rol(self):
        return self._wait_for_enabled(InviteTeammate.invite_rol, None, 0, 3)

    def click_rol(self):
        self._click(InviteTeammate.invite_rol)
        return self

    def click_collaborator(self):
        self._click(InviteTeammate.rol_collaborator)

    def click_invite(self):
        self._wait_for_enabled(InviteTeammate.invite_btn)
        self._click(InviteTeammate.invite_btn)

    def wait_invite_enabled(self):
        return self._wait_for_enabled(InviteTeammate.invite_btn)

    def wait_for_setting(self):
        return self._wait_for_enabled(LocatorLeftMenu.settings)

    def wait_button_account_settings(self):
        return self._wait_for_enabled(Settings.account_settings)

    def wait_button_logout(self):
        return self._wait_for_enabled_text(Settings.logout, 'Log Out')

    def do_logout(self):
        PageLeftMenu(self.driver).wait_button_logout()
        PageLeftMenu(self.driver).mouse_over_left_menu()
        PageLeftMenu(self.driver).click_button_settings()
        # TODO
        time.sleep(2)
        PageLeftMenu(self.driver).click_logout()

    def wait_left_menu(self):
        return self._wait_for_visible(LocatorLeftMenu.nav_menu)
