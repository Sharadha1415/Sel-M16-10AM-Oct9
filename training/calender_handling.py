import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.makemytrip.com/')
driver.maximize_window()
time.sleep(2)

driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
time.sleep(2)

driver.find_element('xpath', '//span[text()="Departure"]').click()
time.sleep(2)


def select_date(month, date):
    while True:
        try:
            driver.find_element('xpath', f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
            break
        except:
            driver.find_element('xpath', '//span[@class="DayPicker-NavButton DayPicker-NavButton--next"]').click()

select_date('September 2026', 25)

##############################################################################################################

# ## Solution2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')           ## login form will appear
# driver.maximize_window()
# time.sleep(2)
#
# ## closing the login form
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# time.sleep(2)
#
# ## click on departure
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# while True:
#     month = driver.find_element('xpath', '(//div[@class="DayPicker-Caption"])[1]')
#     print(month.text)
#
#     if month.text == 'July 2026':
#         driver.find_element('xpath', '(//p[text()="20"])[1]').click()
#         break
#     else:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()


'''
Go to https://www.irctc.co.in/nget/train-search, select the travel date
Go to https://www.redbus.in/, select the date of journey
Go to https://www.booking.com/, select the check-in date
'''


# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')           ## login form will appear
# driver.maximize_window()
# time.sleep(2)
#
# ## closing the login form
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# time.sleep(2)
#
# to = driver.find_element('xpath', '//input[@id="toCity"]')
# to.click()
# to.send_keys('Ranchi')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//p[@class="font12 greyText appendBottom3"]')
# print(ele.text)
#
# # driver.find_element('xpath', '//p[text()="Birsa Munda Airport"]').click()

































