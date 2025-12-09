import time

'''
text    :   It is a property of the web-element.
            It will give the text of the web-element
            SYNTAX  :   web_element.text
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# men = driver.find_element('xpath', '//a[@data-group="men"]')
# print(men.text)
#
# women = driver.find_element('xpath', '//a[@data-group="women"]')
# print(women.text)

##############################################################################################

'''
get_attribute   :   It is used to retrieve the full value of any attribute of a web-element
                    SYNTAX  :   web_element.get_attribute("attr_name")
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# # print(women.get_attribute('href'))
# # print(women.get_attribute('class'))
# # print(women.get_attribute('style'))
# # print(women.get_attribute('data-index'))
#
# # html_code = women.get_attribute("outerHTML")
# # print(html_code)      ## Gives the complete html of that web-element
#
# html_code = women.get_attribute("innerHTML")
# print(html_code)        ## Gives the data present between the open and close tag

# print(women.get_attribute('hrefffff'))        ## None
## If the attribute name doesnt exist, then it will give None

##############################################################################################

'''
get_dom_attribute   :   It retrieves the attribute value exactly as it is visible in the DOM 
                        SYNTAX  :   web_element.get_dom_attribute("attr_name")
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# print(women.get_attribute('href'))          ## https://www.myntra.com/shop/women
# print(women.get_dom_attribute('href'))      ## /shop/women

##############################################################################################

'''
is_enabled  :   It is used to check whether the element is enabled or disabled on the web-page
                If the element is enabled, then it will give True
                If the element is disabled, then it will give False.
                SYNTAX  :   web_element.is_enabled()
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/accounts/emailsignup/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//button[text()="Sign up"]')
# print(ele.is_enabled())         ## False
#
# ele2 = driver.find_element('xpath', '//button[text()="Log in with Facebook"]')
# print(ele2.is_enabled())
#

##############################################################################################

'''
assert  :   It is a keyword.
            It is used to validate the expected output with the actual output.
            assert will take a condition
            
            SYNTAX  :   assert condition
            
            If the condition is True, the test case passes and the execution will continue
            If the condition is False, then it will always give AssertionError
'''

assert 10%2==0
print("Hello world")

assert 11%2==0

#------------------------------------------------------------------------------------------------
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(2)

ele2 = driver.find_element('xpath', '//button[text()="Log in with Facebook"]')      ## True
assert ele2.is_enabled()
print("Login with facebook is enabled")

ele = driver.find_element('xpath', '//button[text()="Sign up"]')                    ## False
assert ele.is_enabled()             ## AssertionError

##------------------------------------------------------------------------------------------------

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
assert women.get_attribute('href') == 'Nandini', "The attribute value is not Nandini"

##############################################################################################

'''
tag_name    :   It is a property. It is used to get the tagname of a web_element.
                Eg  :   a, div, span, p, etc,...
                
aria-role   :   It is a property.
                This helps screen readers to understand what UI element it is.
                Eg  :   button, textbox, link etc,..

'''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# print(women.tag_name)
# print(women.aria_role)    ## link
#
# ele = driver.find_element('xpath', '//h4[text()="LUXE GRAND REDUCTION DEALS"]')
# # print(ele.tag_name)
# # print(ele.aria_role)              ## heading
#
# search_bar = driver.find_element('xpath', '//input[@class="desktop-searchBar"]')
# # print(search_bar.tag_name)
# # print(search_bar.aria_role)     ## textbox

##------------------------------------------------------------------------
'''
To Take the screenshot of a web-element, we have screenshot() attribute
    SYNTAX  :   web_element.screenshot("ss_name.png")
                By default the screenshot will be saved in the same location as our python file

To store the screenshot in different location
    SYNTAX  :   web_element.screenshot("location\ss_name.png")

'''

# women.screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\screenshots_\women.png')
# ele.screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\screenshots_\heading.png')
# search_bar.screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\screenshots_\searchbar.png')






















































