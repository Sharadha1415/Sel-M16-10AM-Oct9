import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/login')
time.sleep(1)


class DemoLogin:

    def email(self):
        driver.find_element('id', 'Email').send_keys('ganga@gmail.com')

    def pwd(self):
        driver.find_element('id', 'Password').send_keys('ganga@12345')

log = DemoLogin()
log.email()
log.pwd()


