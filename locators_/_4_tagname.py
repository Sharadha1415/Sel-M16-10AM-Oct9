'''
tag name    :   We can locate the web-elements using tagname.
                tag name is not unique.
                tag name will always consider the first occurance

'''

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\sel-capg-oct16\files_\css_selector.html')
time.sleep(2)

driver.find_element('tag name', 'input').send_keys('harry')
time.sleep(1)
driver.find_element('tag name', 'input').send_keys('potter')














