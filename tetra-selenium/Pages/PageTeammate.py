import time

from Functions import readmail
from Pages import PageFactory
from Pages.BasePage import BasePage


class PageTeammate(BasePage):

    def invite_teammate(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").click_button_teammate()
        random = self.functions.generate_random()
        mail = self.functions.generate_email_invite(random)
        password = self.functions.generate_password()
        PageFactory.get_page_object(self.driver, "leftmenu").send_teammate_mail(mail)

        if PageFactory.get_page_object(self.driver, "leftmenu").is_enabled_rol():
            PageFactory.get_page_object(self.driver, "leftmenu").click_rol().click_collaborator()

        if PageFactory.get_page_object(self.driver, "leftmenu").wait_invite_enabled():
            PageFactory.get_page_object(self.driver, "leftmenu").click_invite()
            # get link
            link = None
            i = 0
            # 10 times
            while link is None and i < 10:
                link = readmail.read_mail()
                i = i + 1
            if link is not None:
                self.driver.get(link)
                PageFactory.get_page_object(self.driver, "registration").wait_for_fullname()
                PageFactory.get_page_object(self.driver, "registration").send_fullname(
                    self.functions.generate_full_name(random)) \
                    .send_name(self.functions.generate_name(random)) \
                    .send_password(password) \
                    .click_button_sign_up_invitation()
                #PageFactory.get_page_object(self.driver, "registration").click_button_ok_invitation()
                # TODO
                time.sleep(5)
                return PageFactory.get_page_object(self.driver, "registration").exist_login_teammate()
            else:
                return False
        else:
            return False

    def show_teammate(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "leftmenu").click_button_teammate()
        random = self.functions.generate_random()
        mail = self.functions.generate_email_invite(random)
        password = self.functions.generate_password()
        PageFactory.get_page_object(self.driver, "leftmenu").send_teammate_mail(mail)

        if PageFactory.get_page_object(self.driver, "leftmenu").is_enabled_rol():
            PageFactory.get_page_object(self.driver, "leftmenu").click_rol().click_collaborator()

        if PageFactory.get_page_object(self.driver, "leftmenu").wait_invite_enabled():
            PageFactory.get_page_object(self.driver, "leftmenu").click_invite()
            # TODO
            time.sleep(5)
            PageFactory.get_page_object(self.driver, "leftmenu").wait_left_menu()
            PageFactory.get_page_object(self.driver, "leftmenu").mouse_over_left_menu() \
                .click_button_settings() \
                .wait_account_settings()
            PageFactory.get_page_object(self.driver, "leftmenu").click_account_settings()
            PageFactory.get_page_object(self.driver, "leftmenu").click_team()
            if PageFactory.get_page_object(self.driver, "leftmenu").get_new_teammate() == mail:
                return True
            else:
                return False

        else:
            return False
