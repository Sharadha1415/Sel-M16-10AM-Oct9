'''
The operations performed using mouse/keyboard, we call them as low-level operations.
To perform low-level operations in selenium, we go for ActionChains

'''
import time



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

'''
Mouse hovering operations   :   move_to_element
'''

# ## Eg1

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# ac_obj.move_to_element(women).perform()
# time.sleep(2)
#
# home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# ac_obj.move_to_element(home).perform()
# time.sleep(2)
#
# genz = driver.find_element('xpath', '(//a[text()="Genz"])[1]')
# ac_obj.move_to_element(genz).perform()

# ##------------------------------------------------------------------------------------
# ## Eg2
#
# driver.get('https://www.kushals.com/')
# time.sleep(4)
#
# accessories = driver.find_element('xpath', '(//a[contains(text(), "Accessories")])[2]')
# ac_obj.move_to_element(accessories).perform()
# time.sleep(2)
#
# wedding_store = driver.find_element('xpath', '(//a[contains(text(), "Wedding Store")])[2]')
# ac_obj.move_to_element(wedding_store).perform()
#
# ##------------------------------------------------------------------------------------
#
# '''
# hover to all the elments present  in the navigation bar
# '''
#
# ## Solution1
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# navigation_elements = driver.find_elements('xpath', '//a[@class="desktop-main"]')    ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
# for ele in navigation_elements[:-1]:
#     ac_obj.move_to_element(ele).perform()
#     time.sleep(2)
#
# ##-------------------------------------------------------------------------------
# ## Solution2
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# navigation_elements = driver.find_elements('xpath', '//a[@class="desktop-main"]')    ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
# for ele in range(0, len(navigation_elements)-1):
#     ac_obj.move_to_element(navigation_elements[ele]).perform()
#     time.sleep(2)

#################################################################################################

'''
Double click
'''

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# copy_ele = driver.find_element('xpath', '//button[text()="Copy Text"]')
# ac_obj.double_click(copy_ele).perform()
# time.sleep(2)
#
# name = driver.find_element('xpath', '//label[text()="Name:"]')
# ac_obj.double_click(name).perform()


#################################################################################################

'''
Right click
'''

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# # ele = driver.find_element('xpath', '//h2[text()="Dynamic Button"]')
# # ac_obj.context_click(ele).perform()             ## will right click on the element specified
#
# ##
# ac_obj.context_click().perform()            ## will right click at the start of the application

#################################################################################################

'''
Scrolling
'''

'''Scrolling to a specific web-element'''
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//p[text()=" USEFUL LINKS "]')
# ac_obj.scroll_to_element(ref_ele).perform()

# ##--------------------------------------------------------------------------------------

'''         Using execute_script        '''
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ref_ele = driver.find_element('xpath', '//p[text()=" USEFUL LINKS "]')
# driver.execute_script("arguments[0].scrollIntoView();", ref_ele)

# ###################################################################################################
#
# ## Scrolling till the end of the application
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(3)
#
# ## To go back to the start of the application
# ac_obj.send_keys(Keys.HOME).perform()

##--------------------------------------------------------------------------------------
'''         Using execute_script        '''

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)
#
# ## To go back to the start of the application
# driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

# ###################################################################################################

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()

# ###################################################################################################
'''     Scroll Down and scroll up by Pixels      

        SYNTAX  :   driver.execute_script("window.scrollBy(horizontal, vertical);")  
'''
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.execute_script("window.scrollBy(0, 500);")       ## will scroll down by 500 pixels
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, -500);")      ## will scroll up by 500 pixels

# ###################################################################################################

'''
Drag and drop
'''

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
#
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()


# ###################################################################################################
'''     SLIDER      '''
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
# time.sleep(2)
#
# slider = driver.find_element('xpath', '(//div[@id="slider-range"]/span)[1]')
#
# ## Move the slider RIGHT by 100 pixels
# ac_obj.click_and_hold(slider).move_by_offset(100, 0).release().perform()
# time.sleep(2)
#
# ## Move the slider LEFT by 100 pixels
# ac_obj.click_and_hold(slider).move_by_offset(-100, 0).release().perform()


# ###################################################################################################
# ###################################################################################################

'''
ANALYZE THE BELOW CODE
'''

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('xpath', '//input[@name="firstname"]').send_keys('Harry')
time.sleep(1)

ac_obj.send_keys(Keys.TAB).perform()        ## The control will shift to the lastname
time.sleep(1)
ac_obj.send_keys('Potter').perform()
time.sleep(2)

ac_obj.send_keys(Keys.BACKSPACE).perform()
time.sleep(2)
ac_obj.send_keys(Keys.BACKSPACE).perform()

# ##-------------------------------------------------------------------

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

fname = driver.find_element('xpath', '//input[@name="firstname"]')
lname = driver.find_element('xpath', '//input[@name="lastname"]')

fname.send_keys('Harry')
time.sleep(2)

fname.send_keys(Keys.CONTROL + 'a')         ## select the data
fname.send_keys(Keys.CONTROL + 'c')         ## copy the data

ac_obj.send_keys(Keys.TAB).perform()        ## switching the control to last name
lname.send_keys(Keys.CONTROL + 'v')         ## paste the data

# ##-------------------------------------------------------------------

## ctrl + a
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
ac_obj.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

# ############################################################################################################

## ctrl + backspace
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
time.sleep(2)
ac_obj.key_down(Keys.CONTROL).send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()

# ##-------------------------------------------------------------------

## shift
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
driver.find_element('xpath', '//input[@id="name"]').send_keys('harry')
time.sleep(2)
ac_obj.key_down(Keys.SHIFT).send_keys('a').perform()

# ##-------------------------------------------------------------------

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('xpath', '//input[@id="name"]').send_keys('Harry Potter')
time.sleep(2)
ac_obj.send_keys(Keys.TAB).perform()
time.sleep(2)
ac_obj.send_keys('harry@gmail.com').perform()


'''
Go to https://crossbrowsertesting.github.io/drag-and-drop.html, perform drag and drop
'''





























