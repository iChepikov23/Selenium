from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Functions.functions import FunctionsUtils


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.functions = FunctionsUtils()

    # Get element
    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)[index]

    # Click Element
    def _click(self, selector, index=0):
        self._wait_for_clickable(selector)
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _clickXpath(self, selector, index=0):
        elem = self.driver.find_element_by_xpath('/html/body/appcues/cue/div/div/a')
        actions = ActionChains(self.driver)
        actions.click(elem).perform()

    # Send Key to Input
    def _input(self, selector, value, index=0):
        self._wait_for_visible(selector)
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    # Wait for element visible and return True if is visible un 5 seg
    def _wait_for_visible(self, selector, link_text=None, index=0, wait=10):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
            try:
                WebDriverWait(self.driver, wait).until(
                    EC.visibility_of_element_located((by, selector))
                )
                return True
            except TimeoutException:
                return False

    # Wait for element visible and return True if is visible un 5 seg
    def _wait_for_visible_element(self, selector, link_text=None, index=0, wait=10):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector_locator = selector['css']
            try:
                WebDriverWait(self.driver, wait).until(
                    EC.visibility_of_element_located((by, selector_locator))
                )
                return self.__element(selector, index)
            except TimeoutException:
                return None

    # Get Attribute of Element
    def _get_element_attribute(self, selector, attribute, index=0):
        self._wait_for_present(selector)
        return self.__element(selector, index).get_attribute(attribute)

    # Get element
    def _get_element(self, selector, index=0):
        return self.__element(selector, index)

    # Upload to Element
    def _upload(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.send_keys(value)

    # Simulate Mouse Over On Element
    def _mouse_over(self, selector, index=0):
        ActionChains(self.driver) \
            .move_to_element(self.__element(selector, index)).perform()

    # Get Current URL
    def _get_current_url(self):
        return self.driver.current_url

    # Return If An Element Exist
    def _exist_element(self, selector: dict, link_text: str = None):
        self.driver.implicitly_wait(10)
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        s = len(self.driver.find_elements(by, selector))
        if s > 0:
            return True
        else:
            return False

    # Wait for Element Enabled
    def _wait_for_clickable(self, selector, link_text=None, index=0, wait=10):
        self.driver.implicitly_wait(wait)
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
            try:
                WebDriverWait(self.driver, wait).until(
                    EC.element_to_be_clickable((by, selector))
                )
                return True
            except TimeoutException:
                return False

    # Wait until Element Disabled
    def _wait_for_disabled(self, selector, link_text=None, index=0, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(lambda x: not self.__element(selector, index).is_enabled())
            return True
        except TimeoutException:
            return False

        # Wait for Element Disabled

    # Wait until element is enablec
    def _wait_for_enabled(self, selector, link_text=None, index=0, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(lambda x: self.__element(selector, index).is_enabled())
            return True
        except TimeoutException:
            return False

    # Wait until element is enablec
    def _wait_for_enabled_text(self, selector, textFind, link_text=None, index=0, wait=10):
        try:
            WebDriverWait(self.driver, wait).until(lambda x: self.__element(selector, index).text == textFind)
            return True
        except TimeoutException:
            return False

    # Wait until element is not displayed
    def _wait_for_invisibility(self, selector, link_text=None, index=0, wait=10):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
            try:
                WebDriverWait(self.driver, wait).until(
                    EC.invisibility_of_element_located((by, selector))
                )
                return True
            except TimeoutException:
                return False

    # Wait until element has the class
    def _wait_for_class(self, selector, select_class, link_text=None, index=0, wait=10):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda x: self._get_element_attribute(selector, 'class', index) == select_class)
            return True
        except TimeoutException:
            return False

    # Get all elements
    def _get_elements(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)

    # Wait until element has the class
    def _wait_for_one_row(self, selector, link_text=None, index=0, wait=10):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda x: len(self._get_elements(selector)) == 1)
            return True
        except TimeoutException:
            return False

    def _wait_for_present(self, selector, link_text=None, index=0, wait=10):
        self.driver.implicitly_wait(wait)
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))
                return True
            except TimeoutException:
                return False
