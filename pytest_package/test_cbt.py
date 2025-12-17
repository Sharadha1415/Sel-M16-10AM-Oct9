import time
import pytest

from selenium import webdriver

@pytest.fixture(scope='class', params=['chrome', 'firefox', 'edge'])
def setup(request):
    parameter = request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome()
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    elif parameter == 'edge':
        driver = webdriver.Edge()

    driver.implicitly_wait(10)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()

## setup --> webdriver.Chrome()

class TestRegister:

    def test_reg_link(self, setup):     ## setup --> webdriver.Chrome()
        setup.find_element('xpath', '//a[text()="Register"]').click()

    def test_gender_btn(self, setup):
        setup.find_element('id', 'gender-male').click()

    def test_fname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('Abhishek')

    def test_lname(self, setup):
        setup.find_element('id', 'LastName').send_keys('U')

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('abhi@gmail.com')

    def test_reg_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('abhi@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('abhi@12345')
        time.sleep(1)

class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('abhi@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('abhi@12345')























