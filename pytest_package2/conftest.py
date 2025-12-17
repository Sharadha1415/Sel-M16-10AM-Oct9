# import time
# import pytest
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class')
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.implicitly_wait(10)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# ## setup --> webdriver.Chrome()

###########################################################################

import time
import pytest

from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action='store',
        default="chrome",
        help="Browser to run tests : chrome/firefox/edge"
    )

@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()





















