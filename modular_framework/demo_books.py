import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/books')
time.sleep(1)

class Books:

    def sort_books(self):
        sortby = driver.find_element('xpath', '//select[@id="products-orderby"]')
        select_sort = Select(sortby)
        select_sort.select_by_visible_text('Price: Low to High')
        time.sleep(2)

    def view_books(self):
        viewas = driver.find_element('xpath', '//select[@id="products-viewmode"]')
        select_view = Select(viewas)
        select_view.select_by_visible_text('List')

books = Books()
books.sort_books()
books.view_books()







