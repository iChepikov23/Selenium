import random
import time

from selenium.webdriver.common.by import By

from Functions import logger
from Functions import readmail
from Locators.LocatorProjects import LocatorProjects
from Pages import PageFactory
from Pages.BasePage import BasePage


class PageProjects(BasePage):

    def create_new_public_project(self):
        PageFactory.get_page_object(self.driver, "projects").click_create_project() \
            .send_name_project(self.functions.generate_project_name(self.functions.generate_random())) \
            .send_desc_project('Test Project').click_create_button_project()
        test = PageFactory.get_page_object(self.driver, "projects").wait_for_notify_created().text == 'SUCCESS'
        #logger.check_errors_console_log(self.driver)
        return test

    def create_new_private_project(self, login):
        PageFactory.get_page_object(self.driver, "projects").click_create_project() \
            .send_name_project(self.functions.generate_project_name(self.functions.generate_random())) \
            .send_desc_project('Test Project').click_private_project_on_create().click_create_button_project()
        test = PageFactory.get_page_object(self.driver, "projects").wait_for_notify_created().text == 'SUCCESS'
        self.functions.update_projects_account_created(login)
        return test

    def delete_project(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver,
                                    "projects").click_options_project().click_delete_project().click_delete_confirm()
        return PageFactory.get_page_object(self.driver, "projects").wait_for_notify_created().text == 'SUCCESS'

    def basic_project(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        name = PageFactory.get_page_object(self.driver, "projects").get_name_row_project('css', 1)
        if (name == 'Super tester'):
            PageFactory.get_page_object(self.driver, "projects").click_basic_project()
            return PageFactory.get_page_object(self.driver, "projects").click_basic_project()
        else:
            return False

    def edit_project(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        name = PageFactory.get_page_object(self.driver, "projects").get_name_row_project('css', 1)
        PageFactory.get_page_object(self.driver, "projects").click_options_project().click_edit_project()
        next_name = self.functions.generate_project_name(self.functions.generate_random())
        PageFactory.get_page_object(self.driver, "projects").send_name_project(next_name).click_update_project()
        if PageFactory.get_page_object(self.driver, "projects").wait_for_notify_created().text == 'SUCCESS':
            if PageFactory.get_page_object(self.driver, "projects").get_name_row_project('css', 1) == name:
                return False
            else:
                return True
        else:
            return False

    def add_teammate_show_project(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login_more_teammates('A', 'Premium', 1)
        self.create_new_private_project(login[0])
        name_project_invite = PageFactory.get_page_object(self.driver, "projects").get_name_row_project('css', 1)
        PageFactory.get_page_object(self.driver,
                                    "projects").click_options_project().click_edit_project().click_add_teammates()
        teammate = PageFactory.get_page_object(self.driver, "projects").click_add_first_teammates()
        PageFactory.get_page_object(self.driver, "projects").click_update_project()
        PageFactory.get_page_object(self.driver, "leftmenu").do_logout()
        teammate_name = teammate[:6] + '+regression' + teammate[6:] + '@tetra.team'
        PageFactory.get_page_object(self.driver, "login").wait_login()
        PageFactory.get_page_object(self.driver, "login").user_login_by_email(teammate_name)
        name_project = PageFactory.get_page_object(self.driver, "projects").get_name_row_project('css', 1)
        if name_project_invite == name_project:
            return True
        else:
            return False

    def search_project(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        PageFactory.get_page_object(self.driver, "projects").create_new_public_project()
        rows = PageFactory.get_page_object(self.driver, "projects").get_rows_projects()
        name = PageFactory.get_page_object(self.driver, "projects").get_name_random_from_project_by_css(rows)
        PageFactory.get_page_object(self.driver, "projects").send_search_project(name)
        rows = PageFactory.get_page_object(self.driver, "projects").get_rows_projects()
        return len(rows) == 1

    def super_test_project(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        # Invite team mate
        PageFactory.get_page_object(self.driver, "leftmenu").click_button_teammate()
        random = self.functions.generate_random()
        mail = self.functions.generate_email_invite(random)
        password = self.functions.generate_password()
        PageFactory.get_page_object(self.driver, "leftmenu").send_teammate_mail(mail)
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
                PageFactory.get_page_object(self.driver, "registration").click_button_ok_invitation()
                # TODO
                time.sleep(5)
                self.functions.save_user_account_to_file(mail, password, organization_u, 'U',
                                                         'Basic')
                self.functions.update_team_mates_account_created(email_u)
                # PageFactory.get_page_object(self.driver, "registration").wait_login()
                # show tester project
                # TODO
                time.sleep(10)
                PageFactory.get_page_object(self.driver, "leftmenu").do_logout()
                PageFactory.get_page_object(self.driver, "login").send_email(email_u).send_password(
                    password_u).click_button_login()

                PageFactory.get_page_object(self.driver, "login").wait_login()
                PageFactory.get_page_object(self.driver,
                                            "projects").click_options_project().click_delete_project(

                ).click_delete_confirm()
                PageFactory.get_page_object(self.driver, "leftmenu").do_logout()
                PageFactory.get_page_object(self.driver, "login").send_email(mail).send_password(
                    password).click_button_login()
                PageFactory.get_page_object(self.driver, "login").wait_login()
                rows = PageFactory.get_page_object(self.driver, "projects").get_rows_projects()
                return len(rows) == 1
            else:
                return False
        else:
            return False

    def change_privacy_project(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login_less_teammates('A')
        self.create_new_public_project(login[0])
        name_project_invite = PageFactory.get_page_object(self.driver, "projects").get_name_row_project('css', 1)
        # Invite team mate
        PageFactory.get_page_object(self.driver, "leftmenu").click_button_teammate()
        random = self.functions.generate_random()
        mail = self.functions.generate_email_invite(random)
        password = self.functions.generate_password()
        PageFactory.get_page_object(self.driver, "leftmenu").send_teammate_mail(mail)
        if PageFactory.get_page_object(self.driver, "leftmenu").is_enabled_rol():
            PageFactory.get_page_object(self.driver, "leftmenu").click_rol().click_collaborator()

        if PageFactory.get_page_object(self.driver, "leftmenu").wait_invite_enabled():
            # TODO
            time.sleep(2)
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
                PageFactory.get_page_object(self.driver, "registration").click_button_ok_invitation()
                # TODO
                time.sleep(5)
                self.functions.save_user_account_to_file(mail, password, login[2], 'U',
                                                         'Basic')
                self.functions.update_team_mates_account_created(login[0])
                # PageFactory.get_page_object(self.driver, "registration").wait_login()

                exist = False
                for x in range(0, 20):
                    if PageFactory.get_page_object(self.driver, "projects").exist_row_project('css', x):
                        name_project = PageFactory.get_page_object(self.driver, "projects").get_name_row_project('css',
                                                                                                                 x)
                        if name_project_invite == name_project:
                            exist = True
                            break
                # teammate can see project public
                if exist:
                    PageFactory.get_page_object(self.driver, "leftmenu").do_logout()
                    PageFactory.get_page_object(self.driver, "login").send_email(login[0]).send_password(
                        login[1]).click_button_login()
                    PageFactory.get_page_object(self.driver, "login").wait_login()
                    PageFactory.get_page_object(self.driver, "projects").click_options_project().click_edit_project()
                    PageFactory.get_page_object(self.driver,
                                                "projects").wait_for_private().click_private_project(

                    ).click_update_project()
                    PageFactory.get_page_object(self.driver, "leftmenu").do_logout()
                    PageFactory.get_page_object(self.driver, "login").user_login_by_email(mail)
                    PageFactory.get_page_object(self.driver, "login").wait_login()
                    exist = False
                    for x in range(0, 20):
                        if PageFactory.get_page_object(self.driver, "projects").exist_row_project('css', x):
                            name_project = PageFactory.get_page_object(self.driver, "projects").get_name_row_project(
                                'css', x)
                            if name_project_invite == name_project:
                                exist = True
                                break
                    if exist:
                        return False
                    else:
                        return True
                else:
                    return False

    def wait_table_projects_empty(self):
        return self._wait_for_visible(LocatorProjects.projects_table_empty)

    def exist_table_projects_empty(self):
        self._exist_element(LocatorProjects.projects_table_empty)
        return self

    def click_create_project(self):
        self._click(LocatorProjects.projects_create_project)
        return self

    def send_name_project(self, name):
        self._input(LocatorProjects.projects_name_project, name)
        return self

    def send_desc_project(self, name):
        self._input(LocatorProjects.projects_desc_project, name)
        return self

    def click_public_project(self):
        self._click(LocatorProjects.project_select_public)
        return self

    def click_private_project(self):
        self._click(LocatorProjects.project_select_private)
        return self

    def click_private_project_on_create(self):
        self._click(LocatorProjects.project_select_private_on_create)
        return self

    def wait_for_private(self):
        self._wait_for_visible(LocatorProjects.project_select_private)
        return self

    def click_create_button_project(self):
        self._click(LocatorProjects.project_create_button)
        return self

    def wait_for_notify_created(self):
        return self._wait_for_visible_element(LocatorProjects.project_create_notify)

    def click_options_project(self):
        self._click(LocatorProjects.project_options)
        return self

    def click_basic_project(self):
        self._click(LocatorProjects.project_first_rows_name_project)
        return self

    def click_delete_project(self):
        self._click(LocatorProjects.project_delete)
        return self

    def click_delete_confirm(self):
        self._click(LocatorProjects.project_delete_confirm)
        return self

    def click_edit_project(self):
        self._click(LocatorProjects.project_edit)
        return self

    def get_name_row_project(self, selector, row):
        locator = LocatorProjects.project_names.copy()
        selector_txt = LocatorProjects.project_names[selector]
        selector_txt = selector_txt.replace("$number", str(row))
        locator[selector] = selector_txt
        return self._get_element(locator).text

    def click_update_project(self):
        self._click(LocatorProjects.project_update)

    def send_search_project(self, search):
        self._wait_for_visible(LocatorProjects.project_search)
        self._input(LocatorProjects.project_search, search)

    def get_table_project(self):
        return self._get_element(LocatorProjects.project_table_container)

    def get_rows_projects(self):
        self._wait_for_one_row(LocatorProjects.project_rows)
        return self._get_elements(LocatorProjects.project_rows)

    def get_name_random_from_project_by_css(self, rows):
        p = random.randint(0, len(rows) - 1)
        return rows[p].find_elements(By.CSS_SELECTOR, LocatorProjects.project_first_rows_name_project['css'])[0].text

    def click_add_teammates(self):
        self._click(LocatorProjects.project_edit_add_teammates)
        return self

    def click_add_first_teammates(self):
        teammate = self._get_element(LocatorProjects.project_add_first_teammate).text
        self._click(LocatorProjects.project_add_first_teammate)
        return teammate

    def exist_row_project(self, selector, row):
        locator = LocatorProjects.project_names.copy()
        selector_txt = LocatorProjects.project_names[selector]
        selector_txt = selector_txt.replace("$number", str(row))
        locator[selector] = selector_txt
        # TODO
        time.sleep(3)
        return self._exist_element(locator)

    def wait_for_project_info(self):
        return self._wait_for_visible(LocatorProjects.project_info)
