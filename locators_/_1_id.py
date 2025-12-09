'''
id  :   "id" is an attribute which is also a locator.
        So, whenever we have "id" attribute, we will go for "id" locator
        id is unique
'''

import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element("id", "user-name").send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(3)
# driver.find_element('id', 'react-burger-menu-btn').click()
# time.sleep(2)
# driver.find_element('id', 'logout_sidebar_link').click()

######################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('id', 'name').send_keys('Likitha')
time.sleep(1)
driver.find_element('id', 'email').send_keys('likitha@gmail.com')
time.sleep(1)
driver.find_element('id', 'phone').send_keys('9181716151')
time.sleep(1)
driver.find_element('id', 'textarea').send_keys('Mandya')
time.sleep(1)
driver.find_element('id', 'female').click()
time.sleep(1)
driver.find_element('id', 'thursday').click()































































