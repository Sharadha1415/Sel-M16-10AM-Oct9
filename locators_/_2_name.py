'''
name    :   "name" is an attribute which is also a locator.
            So, whenever we have "name" attribute, we will go for "name" locator

            DRAWBACKS
            *   name is not unique
                Multiple elements can have same name attribute and same value
                Incase of multiple occurances, name will always consider the first occurance


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
# driver.get('https://www.instagram.com/')
# time.sleep(2)
# driver.find_element('name', 'username').send_keys('likitha_12345')
# time.sleep(1)
# driver.find_element('name', 'password').send_keys('likitha@12345')

#############################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
# driver.find_element('name', 'firstname').send_keys('Renitha')
# time.sleep(1)
# driver.find_element('name', 'lastname').send_keys('Malepati')
# time.sleep(1)
# driver.find_element('name', 'reg_email__').send_keys('renitha@gmail.com')
# time.sleep(1)
# driver.find_element('name', 'reg_passwd__').send_keys('renitha@12345')

#############################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\sel-capg-oct16\files_\css_selector.html')
time.sleep(2)

driver.find_element('name', 'fname').send_keys('sameeksha')
time.sleep(1)
driver.find_element('name', 'fname').send_keys('gnanavi')

## Both username and password will be filled in the same textbox.
## Whenever there are multiple occurances, name locator will always consider the first occurance

















