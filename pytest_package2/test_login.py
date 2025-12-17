import time

class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('abhi@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('abhi@12345')
