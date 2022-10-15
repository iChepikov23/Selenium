import logging.handlers
import os
import time
from logging import handlers

logger = logging.getLogger('my_app')
logger.setLevel(logging.ERROR)
logHandler = handlers.TimedRotatingFileHandler('tetra_error.log', when='M', interval=1)
logHandler.setLevel(logging.ERROR)
logger.addHandler(logHandler)


def check_errors_console_log(driver):
    # TODO
    time.sleep(2)
    current_console_log_errors = []
    if "ie" not in str(driver):
        log_errors = []
        new_errors = []
        log = get_browser_console_log(driver)
        print("Console Log: ", log)
        for entry in log:
            if entry['level'] == 'SEVERE':
                log_errors.append(entry['message'])

        if current_console_log_errors != log_errors:
            new_errors = list(set(log_errors) - set(current_console_log_errors))
            current_console_log_errors = log_errors

        if len(new_errors) > 0:
            log_setup()
            logger.error("\nBrowser console error on url: %s\nConsole error(s):%s" % (
                driver.current_url, '\n----'.join(new_errors)))


def get_browser_console_log(driver):
    try:
        log = driver.get_log('browser')
        return log
    except Exception as e:
        print("Exception when reading Browser Console log")
        print(str(e))


def log_setup():
    directory = os.path.dirname(__file__)
    directory = directory.replace('Functions', 'data')
