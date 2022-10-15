import os
import time

from selenium.common.exceptions import NoSuchWindowException

from Functions import readmail
from Locators.LocatorLeftMenu import LocatorLeftMenu
from Locators.LocatorLogin import LocatorLogin
from Locators.LocatorRegistration import LocatorRegistration
from Pages import PageFactory
from Pages.BasePage import BasePage

url_terms = 'https://www.tetrainsights.com/terms-and-conditions/';
url_policy = 'https://www.tetrainsights.com/privacy-policy/';


class PageRegistration(BasePage):

    #################################################################
    #                            Methods                            #
    #################################################################
    def user_registration_back_icon(self, myEnvironment):
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        PageFactory.get_page_object(self.driver, "login").exist_nav_menu()
        PageFactory.get_page_object(self.driver, "registration").click_tetra_icon()
        if myEnvironment == "staging":
            return self.driver.current_url == LocatorLogin.STAGING_USER_LOGIN_URL
        elif myEnvironment == "ninja":
            return self.driver.current_url == LocatorLogin.NINJA_USER_LOGIN_URL
        elif myEnvironment == "test":
            return self.driver.current_url == LocatorLogin.TEST_USER_LOGIN_URL
        return False

    def user_registration(self):
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        random = self.functions.generate_random()
        email = self.functions.generate_email(random)
        password = self.functions.generate_password()
        organization = self.functions.generate_organization(random)

        if PageFactory.get_page_object(self.driver, "registration").send_email(email).send_password(
                password).click_button_next():

            PageFactory.get_page_object(self.driver, "registration").wait_confirm_mail()
            link = None
            i = 0
            # 10 times
            while link is None and i < 20:
                link = readmail.read_confirm_mail()
                i = i + 1
            if link is not None:
                if os.environ.get('python_local') == "local":
                    link = link.replace("https://staging.tetrainsights.com/", "http://localhost:4200/")
                self.driver.get(link)
                PageFactory.get_page_object(self.driver, "registration").wait_for_fullname()
                PageFactory.get_page_object(self.driver, "registration").send_fullname(
                    self.functions.generate_full_name(random)) \
                    .send_name(self.functions.generate_name(random)) \
                    .send_organization(organization)
                PageFactory.get_page_object(self.driver, "registration").wait_resgistration_next()
                PageFactory.get_page_object(self.driver, "registration").click_button_sign_up()
                PageFactory.get_page_object(self.driver, "login").wait_first_login()
                PageFactory.get_page_object(self.driver, "login").click_back()
                row = (email, password, organization)
                return row
            else:
                return False
        else:
            return None

    def user_registration_duplicate_mail(self):
        b_result = PageFactory.get_page_object(self.driver, "registration").user_registration()
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        PageFactory.get_page_object(self.driver, "registration").send_email(b_result[0])
        # if no show error in 5 seg, error.
        # p = PageFactory.get_page_object(self.driver, "registration").wait_email_duplicate()
        return not PageFactory.get_page_object(self.driver, "registration").is_enabled_registration()

    def user_registration_error_mail(self):
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        PageFactory.get_page_object(self.driver, "registration").send_email(self.functions.generate_error_email())
        return not PageFactory.get_page_object(self.driver, "registration").is_enabled_registration()

    def sign_up_button_disable(self):
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        random = self.functions.generate_random()
        email = self.functions.generate_email(random)
        password = self.functions.generate_password()
        organization = self.functions.generate_organization(random)
        PageFactory.get_page_object(self.driver, "registration").send_email(email)
        # if when send email, singup is enabled > error
        if not PageFactory.get_page_object(self.driver, "registration").is_enabled_registration():
            PageFactory.get_page_object(self.driver, "registration").send_password(password).click_button_next()
            PageFactory.get_page_object(self.driver, "registration").wait_confirm_mail()
            link = None
            i = 0
            # 10 times
            while link is None and i < 20:
                link = readmail.read_confirm_mail()
                i = i + 1
            if link is not None:
                self.driver.get(link)
                PageFactory.get_page_object(self.driver, "registration").wait_for_fullname()
                PageFactory.get_page_object(self.driver, "registration").send_fullname(
                    self.functions.generate_full_name(random))
                if not PageFactory.get_page_object(self.driver, "registration").is_enabled_sign_up():
                    PageFactory.get_page_object(self.driver, "registration").send_name(
                        self.functions.generate_name(random))
                    if not PageFactory.get_page_object(self.driver, "registration").is_enabled_sign_up():
                        PageFactory.get_page_object(self.driver, "registration").send_organization(organization)
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

        random = self.functions.generate_random()
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        PageFactory.get_page_object(self.driver, "registration").send_email(self.functions.generate_email(random)) \
            .click_button_next()
        if not PageFactory.get_page_object(self.driver, "registration").is_enabled_sign_up():
            PageFactory.get_page_object(self.driver, "registration").send_fullname(
                self.functions.generate_full_name(random))
            if not PageFactory.get_page_object(self.driver, "registration").is_enabled_sign_up():
                PageFactory.get_page_object(self.driver, "registration").send_name(self.functions.generate_name(random))
                if not PageFactory.get_page_object(self.driver, "registration").is_enabled_sign_up():
                    PageFactory.get_page_object(self.driver, "registration").send_organization(
                        self.functions.generate_organization(random))
                    if PageFactory.get_page_object(self.driver, "registration").wait_disabled_sign_up():
                        PageFactory.get_page_object(self.driver, "registration").send_password(
                            self.functions.generate_password())
                        if not PageFactory.get_page_object(self.driver, "registration").is_enabled_sign_up():
                            return False
                        else:
                            return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def user_registration_duplicate_organization(self):
        b_result = PageFactory.get_page_object(self.driver, "registration").user_registration()

        PageFactory.get_page_object(self.driver, "login").click_create_account()
        random = self.functions.generate_random()
        email = self.functions.generate_email(random)
        password = self.functions.generate_password()
        organization = self.functions.generate_organization(random)
        if PageFactory.get_page_object(self.driver, "registration").send_email(email).send_password(
                password):
            time.sleep(2)
            PageFactory.get_page_object(self.driver, "registration").click_button_next()
            PageFactory.get_page_object(self.driver, "registration").wait_confirm_mail()
            link = None
            i = 0
            # 10 times
            while link is None and i < 20:
                link = readmail.read_confirm_mail()
                i = i + 1
            if link is not None:
                self.driver.get(link)
                PageFactory.get_page_object(self.driver, "registration").wait_for_fullname()
                PageFactory.get_page_object(self.driver, "registration").send_fullname(
                    self.functions.generate_full_name(random)) \
                    .send_name(self.functions.generate_name(random)) \
                    .send_organization(b_result[2])
                return PageFactory.get_page_object(self.driver, "registration").exist_organization_duplicate()
            else:
                return False
        else:
            return None

    def user_registration_error_password(self):
        # save accounts use to register
        random = self.functions.generate_random()
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        if PageFactory.get_page_object(self.driver, "registration").send_email(
                self.functions.generate_email(random)).click_button_next():
            PageFactory.get_page_object(self.driver, "registration").send_fullname(
                self.functions.generate_full_name(random)) \
                .send_name(self.functions.generate_name(random)) \
                .send_organization(self.functions.generate_organization(random)) \
                .send_password(self.functions.generate_bad_password())
            return PageFactory.get_page_object(self.driver, "registration").exist_error_pass()
        else:
            return False

    def user_registration_terms(self):
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        random = self.functions.generate_random()
        email = self.functions.generate_email(random)
        password = self.functions.generate_password()
        organization = self.functions.generate_organization(random)
        if PageFactory.get_page_object(self.driver, "registration").send_email(email).send_password(
                password).click_button_next():
            PageFactory.get_page_object(self.driver, "registration").wait_confirm_mail()
            link = None
            i = 0
            # 10 times
            while link is None and i < 20:
                link = readmail.read_confirm_mail()
                i = i + 1
            if link is not None:
                self.driver.get(link)
                PageFactory.get_page_object(self.driver, "registration").wait_for_terms()
                PageFactory.get_page_object(self.driver, "registration").click_terms()
                bReturn = False
                for handle in self.driver.window_handles:
                    self.driver.switch_to.window(handle)
                    if url_terms == self.driver.current_url:
                        bReturn = True
                        break
                return bReturn
            else:
                return False
        else:
            return False

    def user_registration_policy(self):
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        random = self.functions.generate_random()
        email = self.functions.generate_email(random)
        password = self.functions.generate_password()
        organization = self.functions.generate_organization(random)
        if PageFactory.get_page_object(self.driver, "registration").send_email(email).send_password(
                password).click_button_next():
            PageFactory.get_page_object(self.driver, "registration").wait_confirm_mail()
            link = None
            i = 0
            # 10 times
            while link is None and i < 20:
                link = readmail.read_confirm_mail()
                i = i + 1
            if link is not None:
                self.driver.get(link)
                PageFactory.get_page_object(self.driver, "registration").wait_for_terms()
                PageFactory.get_page_object(self.driver, "registration").click_policy()
                bReturn = False
                for handle in self.driver.window_handles:
                    self.driver.switch_to.window(handle)
                    if url_policy == self.driver.current_url:
                        bReturn = True
                        break
                return bReturn
            else:
                return False
        else:
            return False

    ###################################################
    #                   Actions                       #
    ###################################################
    def send_email(self, email):
        self._input(LocatorRegistration.registration_user_email, email)
        return self

    def click_button_next(self):
        if self.wait_for_enable_next():
            self._click(LocatorRegistration.registration_user_button_next)
            return True
        else:
            return False

    def send_fullname(self, fullname):
        self._wait_for_visible(LocatorRegistration.registration_user_fullname)
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
        time.sleep(3)
        self._wait_for_enabled(LocatorRegistration.registration_user_button_sign_up)
        self._click(LocatorRegistration.registration_user_button_sign_up)

    def click_button_sign_up_invitation(self):
        self.driver.implicitly_wait(2)
        self._wait_for_clickable(LocatorRegistration.registration_user_invitation_button_sign_up)
        self._click(LocatorRegistration.registration_user_invitation_button_sign_up)

    def click_button_ok_invitation(self):
        try:
            self._wait_for_visible(LocatorLogin.login_mate_accept)
            self.driver.switch_to.frame(
                self._get_element(LocatorLogin.login_iframe_track))
            if self._wait_for_visible(LocatorLogin.login_mate_accept):
                sign_in = self._get_element(LocatorLogin.login_mate_accept)
                self.driver.execute_script('arguments[0].click()', sign_in)
            else:
                return
        except NoSuchWindowException:
            return

    def user_registration_valid_pass(self, password):
        PageFactory.get_page_object(self.driver, "login").click_create_account()
        random = self.functions.generate_random()
        email = self.functions.generate_email(random)
        if PageFactory.get_page_object(self.driver, "registration").send_email(email).send_password(
                password).wait_enabled_sign_up():
            return True
        else:
            return None

    def click_tetra_icon(self):
        self._click(LocatorRegistration.registration_user_tetra_icon)

    def wait_email_duplicate(self):
        return self._wait_for_visible(LocatorRegistration.registration_user_error_duplicate)

    def exist_email_duplicate(self):
        return self._wait_for_visible(LocatorRegistration.registration_user_error_duplicate)

    def is_enabled_registration(self):
        return self._get_element(LocatorRegistration.registration_user_button_next).is_enabled()

    def is_enabled_sign_up(self):
        time.sleep(2)
        return self._get_element(LocatorRegistration.registration_user_button_sign_up).is_enabled()

    def wait_disabled_sign_up(self):
        return self._wait_for_disabled(LocatorRegistration.registration_user_button_next)

    def wait_enabled_sign_up(self):
        return self._wait_for_enabled(LocatorRegistration.registration_user_button_next)

    def wait_resgistration_next(self):
        self._wait_for_visible(LocatorRegistration.registration_user_ok)
        self._wait_for_clickable(LocatorRegistration.registration_user_button_sign_up)
        return self._wait_for_enabled(LocatorRegistration.registration_user_button_sign_up)

    def wait_organization_duplicate(self):
        return self._wait_for_visible(LocatorRegistration.registration_user_msg_duplicate_organization)

    def exist_organization_duplicate(self):
        return self._exist_element(LocatorRegistration.registration_user_msg_duplicate_organization)

    def wait_error_pass(self):
        return self._wait_for_visible(LocatorRegistration.registration_user_msg_bad_password)

    def exist_error_pass(self):
        return self._exist_element(LocatorRegistration.registration_user_msg_bad_password)

    def exist_error_pass(self):
        return self._exist_element(LocatorRegistration.registration_user_msg_bad_password)

    def wait_login(self):
        self._wait_for_visible(LocatorLogin.login_notify)
        return self._wait_for_invisibility(LocatorLogin.login_notify)

    def exist_login(self):
        self._wait_for_invisibility(LocatorLogin.login_notify)
        return self._exist_element(LocatorLeftMenu.nav_menu)

    def exist_login_teammate(self):
        return self._exist_element(LocatorLeftMenu.nav_menu)

    def wait_for_enable_next(self):
        return self._wait_for_enabled(LocatorRegistration.registration_user_button_next)

    def wait_for_fullname(self):
        return self._wait_for_visible(LocatorRegistration.registration_user_fullname)

    def click_terms(self):
        time.sleep(2)
        self._wait_for_clickable(LocatorRegistration.registration_privacy_policy)
        self._click(LocatorRegistration.registration_terms_conditions)

    def click_policy(self):
        time.sleep(2)
        self._wait_for_clickable(LocatorRegistration.registration_privacy_policy)
        self._click(LocatorRegistration.registration_privacy_policy)

    def wait_confirm_mail(self):
        self._wait_for_visible(LocatorRegistration.registration_confirm_mail_text)

    def wait_for_terms(self):
        return self._wait_for_visible(LocatorRegistration.registration_terms_conditions)
