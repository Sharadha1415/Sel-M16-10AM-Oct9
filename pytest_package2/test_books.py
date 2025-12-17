import time

class TestBooks:
    def test_click_books(self, setup):
        setup.find_element('xpath', '(//a[contains(text(), "Books")])[3]').click()
        time.sleep(2)

    def test_add_to_cart(self, setup):
        setup.find_element('xpath', '(//input[@value="Add to cart"])[1]').click()




















