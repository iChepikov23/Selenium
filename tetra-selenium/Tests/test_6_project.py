import allure
import pytest

from Pages import PageFactory


@pytest.mark.usefixtures("myDriver")
class TestProject:

    @allure.feature('Project')
    @allure.story('XRAY-4 - Basic project is created')
    @pytest.mark.flaky(reruns=3)
    def test_basic_project_created(self):
        assert PageFactory.get_page_object(self.driver, "projects").basic_project()

    @allure.feature('Project')
    @allure.story('Create New Public Project')
    @pytest.mark.flaky(reruns=3)
    def test_create_new_public_project(self):
        login = PageFactory.get_page_object(self.driver, "login").user_login()
        assert PageFactory.get_page_object(self.driver, "projects").create_new_public_project()

    @allure.feature('Project')
    @allure.story('Delete First Project')
    @pytest.mark.flaky(reruns=3)
    def test_delete_public_project(self):
        assert PageFactory.get_page_object(self.driver, "projects").delete_project()

    @allure.feature('Project')
    @allure.story('Edit Project')
    @pytest.mark.flaky(reruns=3)
    def test_edit_project(self):
        assert PageFactory.get_page_object(self.driver, "projects").edit_project()

    @allure.feature('Project')
    @allure.story('Search Project')
    @pytest.mark.flaky(reruns=3)
    def test_search_project(self):
        assert PageFactory.get_page_object(self.driver, "projects").search_project()
