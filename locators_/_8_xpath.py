'''
text    :   //tagname[text()="text"]

'''
import time


# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="TVs & Appliances"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Become a Seller"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Start Selling"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@name="mobileNumber"]').send_keys('9080706050')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="email"]').send_keys('ganga@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="gst"]').send_keys('0000000000')
# time.sleep(1)
# driver.find_element('xpath', '//span[text()="Register & Continue"]').click()
#
#
# #######################################################################
# text    :   //tagname[text()="text"]

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)

# driver.get('https://www.amazon.in/')
# time.sleep(4)
#
# # driver.find_element('xpath', '//a[text()="Bestsellers"]').click()
# # time.sleep(2)
# # driver.find_element('xpath', '//a[text()="Most Gifted"]').click()
# # time.sleep(2)
# # driver.find_element('xpath', '//a[text()="Amazon Launchpad"]').click()
# # time.sleep(2)
#
# driver.find_element('xpath', '''//a[text()="Today's Deals"]''').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Coupons"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Appliances"]').click()

#################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://blinkit.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Detect my location"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//div[text()="Login"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@class="login-phone__input input"]').send_keys('9080706050')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Continue"]').click()


#################################################

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
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Ram')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('Kumar')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[5]').send_keys('ram@gmail.com')


#################################################

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
# driver.find_element('xpath', '(//a[@class="desktop-main"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[4]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[5]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[6]').click()
# time.sleep(2)

#################################################

'''
contains    :   To locate the partial text of any tagname, we use xpath using contains
                SYNTAX  :   //tagname[contains(text(), "partial_text")]

'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.giva.co/')
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Card")]').click()
# time.sleep(2)


####################################################################################

'''
Dependent independent xpath
    *   Identify the dependent-independent elements
    *   Write the xpath of the independent element   
    *   Traverse back until we get the common match for dependent independent element
    *   Continue writing the xpath of the dependent element
    
'''

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()

###############################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()

###############################################################################################

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Downloads"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Python 3.12.12"]/../..//a[text()="Release Notes"]/../..//a[text()="Release Notes"]').click()


###############################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.tradingview.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Search"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="query"]').send_keys('HAL')
# time.sleep(2)
#
# driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
# time.sleep(2)
#
# hal_price = driver.find_element('xpath', '//span[text()="HAL"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(hal_price.text)

###############################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(2)
#
# driver.find_element('xpath', '(//div[@id="ai-chat-bubble-close"])[2]').click()
# time.sleep(3)
#
# gold_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# gold_buyprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
#
# print(f"The sellprice of gold is {gold_sellprice.text}")
# print(f"The buyprice of gold is {gold_buyprice.text}")

###############################################################################################
















