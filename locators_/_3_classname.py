'''
class name  :   If we have "class" attribute, we can go for "class name" locator

                DRAWBACKS
                *   class is not unique.
                    We can have multiple web-elements with the same class attribute and the value.
                    Incase of multiple occurances, "class name" locator will always consider the first occurance

                *   class name locator cannot recognize the spaces
                    If there are spaces in the value of the class attribute, we should replace the space with dot(.)


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
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('class name', 'ico-register').click()
# time.sleep(2)
# driver.find_element('class name', 'ico-login').click()
# time.sleep(2)
# driver.find_element('class name', 'ico-cart').click()

#######################################################################################

## Eg2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('class name', 'inputtext _58mg _5dba _2ph-').send_keys('Harry')

## NoSuchElementException
## class name locator cannot identify the spaces

##-----------------------------------------------------------------------------------

## To overcome the error, we will replace the space with dot(.)

#######################################################################################
#
# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('class name', 'inputtext._58mg._5dba._2ph-').send_keys('Harry')

#######################################################################################

# ## Eg3
#
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
# driver.find_element('class name', 'input_error.form_input').send_keys('standard_user')

#######################################################################################

## Eg4

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\sel-capg-oct16\files_\css_selector.html')
time.sleep(2)

driver.find_element('class name', 'first_row').send_keys('python')
time.sleep(1)
driver.find_element('class name', 'first_row').send_keys('selenium')

## both the values will be filled in the first textbox only


















