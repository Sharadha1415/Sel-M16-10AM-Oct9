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
# footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# print(footer_elements)          ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7, wb8, wb8,....wb22]
#
# for ele in footer_elements:
#     print(ele.text)

############################################################################

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
# categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
# print(categories)       ## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
#
# for ele in categories:
#     print(ele.text)

############################################################################

'''
1.  wap to fetch all the popular searches from https://www.myntra.com/
2.  wap to print all the colors available for adidas original shoes in https://www.myntra.com/
3.  Go to https://www.zomato.com/Bengaluru/, search for pizza, select pizza-delivery, select any cafe/restraunt which serves pizza,
    wap to print the name and price of each food item in available
4.  Go to https://in.bookmyshow.com/, select the location. Print all the movie names available.
'''

# ## Eg3
#
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
# driver.find_element('xpath', '//input[@class="desktop-searchBar"]').send_keys('adidas')
# time.sleep(2)
#
# driver.find_element('xpath', '//li[text()="Adidas Originals Shoes"]').click()
# time.sleep(2)
#
# adidas_shoes = driver.find_elements('xpath', '//h4[@class="product-product"]')      ## [wb1, wb2, wb3,..wb50]
# shoes_prices = driver.find_elements('xpath', '//div[@class="product-price"]')       ## [wb1, wb2, wb3,..wb50]
#
# for shoe, price in zip(adidas_shoes, shoes_prices):
#     print(shoe.text, "=", price.text)


##################################################################################

# ## Eg4
#
# data_list = eval(input('Enter the movies : '))
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
# all_textboxes = driver.find_elements('xpath', '//input[@name="fname"]')
# # list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7, wb8, wb9]
# # data_list = ['KGF', 'Devil', 'Friends', 'Sherlock', 'Kantara', 'The 100', 'Harry Potter', 'GOT', 'One piece']
#
# for textbox, data in zip(all_textboxes, data_list):
#     textbox.send_keys(data)

##################################################################################

# ## Eg5
#
# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# '''
# all links --> href --> <a>
# '''
#
# all_links = driver.find_elements('tag name', 'a')       ## list of web-elements     ## [a1, a2, a3, a4, a5, a6, a7, a8,...]
#
# for link in all_links:
#     print(link.get_attribute('href'))


###############################################################################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac = ActionChains(driver)

driver.get('https://www.myntra.com/')
time.sleep(2)

mens = driver.find_element('xpath', '//a[text()="Men"]')
ac.move_to_element(mens).perform()
time.sleep(2)

mens_section = driver.find_elements('xpath', '(//div[@class="desktop-paneContent"])[1]//a')

for ele in mens_section:
    print(ele.text)

























