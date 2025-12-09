'''
Alerts  :   Alerts are not inspectable.
            Suppose if we are able to inspect, then it is not an alert.

            To handle the alerts, we will switch the driver to the alert
            SYNTAX  :   alert_obj = driver.switch_to.alert
                        alert_obj has two attributes to handle the alert
                        *   accept()    :   To accept the alert, we use alert_obj.accept()
                        *   dismiss()   :   To dismiss the alert, we use alert_obj.dismiss()

            There are different types alerts
            *   simple alert    :   If the alert is having only one option, then it is a simple alert.
                                    To handle the simple alert, first switch the driver to the alert
                                    Now we can either use accept or dismiss.
                                    alert_obj.accept()  or      alert_obj.dismiss()

            *   confirmation alert  :   If the alert is having two options, then it is a confirmation alert.
                                    To handle the confirmation alert, first switch the driver to the alert
                                    To click on OK/YES/AGREE,.. we give alert_obj.accept()
                                    To click on CANCEL/NO/DISAGREE,.. we give alert_obj.dismiss()

            *   Prompt alert    :   Here the alert will take the data from the user.
                                    To handle the prompt alert, first switch the driver to the alert
                                    alert_obj.send_keys("data")
                                    alert_obj.accept()

'''
import time


'''     confirmation alert      '''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

#########################################################################################################

'''     Simple alert      '''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

#########################################################################################################

'''     prompt alert      '''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Prompt Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
# alert_obj.send_keys('Soumya')
# alert_obj.accept()

#########################################################################################################

'''         authentication popup            '''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://the-internet.herokuapp.com/basic_auth')
#
# ## the above url will ask for the username and password to launch the application
# ## The pop-up is not inspectable and we cant switch the driver to the alert.

##-----------------------------------------------------------------------------------

# ## To handle such pop-ups, we will give the username and pwd while launching the application
# ## SYNTAX   :   https://username:pwd@url
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

#########################################################################################################

'''         push notifications          '''

'''     Disable push notifications in Chrome       '''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')

# ##-----------------------------------------------------------------------
#
'''     Disable push notifications in Firefox       '''
# from selenium import webdriver
#
# opts = webdriver.FirefoxOptions()
#
# opts.set_preference("dom.webnotifications.enabled", False)
# opts.set_preference("dom.push.enabled", False)
#
# driver = webdriver.Firefox(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
#
# ##-----------------------------------------------------------------------
#
'''     Disable push notifications in Edge       '''
# from selenium import webdriver
#
# opts = webdriver.EdgeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Edge(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')

##-----------------------------------------------------------------------

'''     Allow push notifications in Chrome       '''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

prefs = {
    "profile.default_content_setting_values.notifications":2            ## 2 --> disable, 1--> allow notifications , 0--> will give the pop-up
}

opts.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(opts)

driver.get('https://www.irctc.co.in/nget/train-search')

##-----------------------------------------------------------------------

'''     Allow push notifications in Firefox       '''

from selenium import webdriver

opts = webdriver.FirefoxOptions()

opts.set_preference("permissions.default.desktop-notification", 1)      ## 2 --> disable, 1--> allow notifications , 0--> will give the pop-up

driver = webdriver.Firefox(opts)
driver.get('https://www.irctc.co.in/nget/train-search')




