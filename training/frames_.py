'''
iframes :   The application present inide another application, we call it as iframe
            The tagname of an iframe is always iframe

            STEPS TO HANDLE IFRAMES
            *   Locate the frame
            *   Switch the driver from the parent frame to the child frame
                SYNTAX  :   driver.switch_to.frame(frame)
            *   Perform the operations in the frame
            *   Once we are done performing the operations inside the frame, we should switch back to the parent_frame

'''


import time

## EG1
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

ac = ActionChains(driver)

driver.get('https://www.linkedin.com')
time.sleep(2)

## locate the frame
google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')

## switch the driver to the frame
driver.switch_to.frame(google_frame)

## perform the operations inside the frame
driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
time.sleep(2)

## switch back to the parent frame
driver.switch_to.parent_frame()
time.sleep(2)

ref_ele = driver.find_element('xpath', '//h2[contains(text(), "Join your colleagues")]')
ac.scroll_to_element(ref_ele).perform()
time.sleep(2)

## locate the iframe
youtube_frame = driver.find_element('xpath', '//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')

## switch the driver to the iframe
driver.switch_to.frame(youtube_frame)

## perform the operations inside the frame
driver.find_element('xpath', '//button[@title="Play"]').click()


####################################################################################

## EG2
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(10)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_\iframe.html')
time.sleep(2)

## Locate the iframe
frame1 = driver.find_element('xpath', '//iframe[@id="FR1"]')

## switch the driver to the frame
driver.switch_to.frame(frame1)

## perform the operations inside the frame
driver.find_element('id', 'small-searchterms').send_keys('books')
time.sleep(2)

## switch back to the parent frame
driver.switch_to.parent_frame()

## locate the frame2
frame2 = driver.find_element('xpath', '//iframe[@id="FR2"]')

## switch the driver to frame2
driver.switch_to.frame(frame2)

## perform the operations inside the frame
driver.find_element('id', 'search_form').send_keys('vehicle insurance')

## switch back to the parent frame
driver.switch_to.parent_frame()
