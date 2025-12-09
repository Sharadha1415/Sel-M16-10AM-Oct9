'''
In web automation, sometimes actions open a new browser window or tab (e.g., clicking a link, pop-up, advertisement, or login window).
Selenium initially controls only the main window where the driver started.
To interact with other windows/tabs, we need to switch between them.

Window Handles
    Every window or tab opened by the browser has a unique ID, called a window handle.
    Selenium provides methods to get and switch between these handles.
    handles = driver.window_handles     ## Returns a list of handles for all open windows/tabs.

    To switch the driver to the window
    driver.switch_to.window(handle)

'''

import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(10)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Google+"]').click()
# time.sleep(2)
#
#
# def handling_windows():
#     return driver.window_handles
#
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'googleblog' in driver.current_url:
#         driver.find_element('xpath', '//input[@class="header__search"]').send_keys('Google pixel9')
#         time.sleep(2)
#         driver.switch_to.window(handling_windows()[0])
#         time.sleep(1)
#
#
# driver.find_element('xpath', '//a[text()="Twitter"]').click()
# time.sleep(2)
# for handle in handling_windows():
#     driver.switch_to.window(handle)
#     if 'x.com' in driver.current_url:
#         driver.find_element('xpath', '//span[text()="Follow"]').click()

###################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

driver.get('https://www.flipkart.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@title="Search for Products, Brands and More"]').send_keys('phones under 30000')
time.sleep(2)
driver.find_element('xpath', '//button[@type="submit"]').click()
time.sleep(2)

driver.find_element('xpath', '//div[@class="KzDlHZ"]').click()
time.sleep(2)

def handle_windows():
    return driver.window_handles

## handle_windows() --> [parent, child,,..]

for handle in handle_windows():
    driver.switch_to.window(handle)
    if 'samsung-galaxy-f36-5g-red-128-gb' in driver.current_url:
        driver.find_element('xpath', '//button[text()="Add to cart"]').click()
        time.sleep(2)

driver.find_element('xpath', '//a[text()="Help Center"]').click()
time.sleep(2)

for handle in handle_windows():
    driver.switch_to.window(handle)
    if 'helpcentre' in driver.current_url:
        driver.find_element('xpath', '//a[text()="Know more"]').click()










