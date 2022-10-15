import os

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from Locators.LocatorLogin import LocatorLogin


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--so", "-S", action="store", default="windows",
                     help="choose your system operation (windows/linux)")
    parser.addoption("--ev", "-E", action="store", default="staging",
                     help="choose your system environment")


@pytest.fixture
def myDriver(request):
    browser_param = request.config.getoption("--browser")
    so_param = request.config.getoption("--so")
    ev_param = request.config.getoption("--ev")

    if browser_param == "chrome" and so_param == "windows":
        dc = DesiredCapabilities.CHROME
        dc['goog:loggingPrefs'] = {'browser': 'ALL',
                                   'driver': 'ALL',
                                   'client': 'ALL',
                                   'server': 'ALL'}
        driver = webdriver.Chrome(get_chrome_drive_locator(), desired_capabilities=dc)
    elif browser_param == "chromehidden" and so_param == "windows":
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        dc = DesiredCapabilities.CHROME
        dc['goog:loggingPrefs'] = {'browser': 'ALL'}
        dc["pageLoadStrategy"] = "normal"
        driver = webdriver.Chrome(get_chrome_drive_locator(), options=options, desired_capabilities=dc)
    elif so_param == "linux":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(
            '--no-sandbox')  # required when running as root user. otherwise you would get no sandbox errors.
        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
    elif browser_param == "firefox":
        driver = webdriver.Firefox(get_firefox_drive_locator())
    elif browser_param == "safari":
        driver = webdriver.Safari(get_safari_drive_locator())
    else:
        raise Exception(f"{request.param} is not supported!")

    # select environment
    if os.environ.get('python_local') == "local":
        driver.get(LocatorLogin.LOCAL_USER_LOGIN_URL)
    elif ev_param == "staging":
        driver.get(LocatorLogin.STAGING_USER_LOGIN_URL)
    elif ev_param == "ninja":
        driver.get(LocatorLogin.NINJA_USER_LOGIN_URL)
    elif ev_param == "test":
        driver.get(LocatorLogin.TEST_USER_LOGIN_URL)
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.execute_script("document.body.style.zoom='100 %'")
    driver.maximize_window()
    driver.implicitly_wait(15)
    request.addfinalizer(driver.close)
    request.cls.driver = driver
    return driver

@pytest.fixture
def myEnvironment(request):
    environment = request.config.getoption("--ev")
    if environment == "staging":
        environment = "staging"
    elif environment == "ninja":
        environment = "ninja"
    elif environment == "test":
        environment = "test"
    else:
        raise Exception(f"{request.param} is not supported!")
    return environment

@pytest.fixture(params=["chrome", "safari", "firefox"])
def parametrize_browser(request):
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    elif browser_param == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    request.cls.driver = driver
    return driver


def get_chrome_drive_locator():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Drivers/chromedriver.exe')
    return filename


def get_firefox_drive_locator():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Drivers/firefoxdriver.exe')
    return filename


def get_safari_drive_locator():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Drivers/safaridriver.exe')
    return filename
