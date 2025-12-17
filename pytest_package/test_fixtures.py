'''Decorator'''
# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def add(a, b):
#     print(a + b)
#
# add(10, 20)
#

##############################################################################

# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def test_login():
#     print("login executing")
#
# @outer
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED

##############################################################################
'''
Fixtures    :   They are the functions which are used to perform setup and teardown operations
                setup       :   The set of operations which executes before the execution of the test_function
                teardown    :   The set of operations which executes afetr the execution of the test_function
                
                SYNTAX  :       @pytest.fixture()
                                def func():
                                    pass        ## setup
                                    yield
                                    pass        ## teardown
                                
                                def test_func(func):    
                                    pass


'''
import pytest
import time

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_logout(greet):
#     print("logout executing")

## collected 2 items
## test_fixtures.py::test_login        Good morning        login executing     PASSED
## test_fixtures.py::test_logout       Good morning        logout executing    PASSED


################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_signup                       signup executing    PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED

'''
Fixture is not applied for test_signup.
'''

################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning        signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSEDGood evening

'''
NOTE    :   The operations before yield will execute before the execution of the test_function
            The operations after yield will execute after the execution of the test_function
'''

################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login        Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup       Good morning        signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout       Good morning        logout executing    PASSEDGood evening
#
#
# ################################################################
#
# @pytest.fixture()
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self, greet):
#         print("login executing")
#
#     def test_signup(self, greet):
#         print("signup executing")
#
#     def test_logout(self, greet):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSEDGood evening
# ## test_fixtures.py::TestSample::test_signup   Good morning    signup executing    PASSEDGood evening
# ## test_fixtures.py::TestSample::test_logout   Good morning    logout executing    PASSEDGood evening


################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSEDGood evening
# ## test_fixtures.py::TestSample::test_signup   Good morning    signup executing    PASSEDGood evening
# ## test_fixtures.py::TestSample::test_logout   Good morning    logout executing    PASSEDGood evening

################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                       signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                       logout executing    PASSEDGood evening

'''
scope is the parameter of the fixture.
When we give scope='class', the fixture will be applied on a class level.
*   It will perform the setup operation.
*   It will execute all the attributes of the TestClass
*   It will perform the teardown operation
'''

################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
# class TestSpam:
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                   signup executing    PASSEDGood evening
# ## test_fixtures.py::TestSpam::test_reg        Good morning    reg executing       PASSED
# ## test_fixtures.py::TestSpam::test_logout                     logout executing    PASSEDGood evening

################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
#
# def test_gmail():
#     print("gmail executing")
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
# class TestSpam:
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 5 items
# ## test_fixtures.py::test_gmail                Good morning    gmail executing     PASSEDGood evening
# ## test_fixtures.py::TestSample::test_login    Good morning    login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                   signup executing    PASSEDGood evening
# ## test_fixtures.py::TestSpam::test_reg        Good morning    reg executing       PASSED
# ## test_fixtures.py::TestSpam::test_logout                     logout executing    PASSEDGood evening

################################################################

# @pytest.fixture(autouse=True, scope='module')
# def greet():
#     print("Good morning")               ## setup
#     yield
#     print("Good evening")               ## teardown
#
# def test_gmail():
#     print("gmail executing")
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
# class TestSpam:
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 5 items
# ## test_fixtures.py::test_gmail                Good morning        gmail executing     PASSED
# ## test_fixtures.py::TestSample::test_login                        login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                       signup executing    PASSED
# ## test_fixtures.py::TestSpam::test_reg                            reg executing       PASSED
# ## test_fixtures.py::TestSpam::test_logout                         logout executing    PASSEDGood evening

################################################################################################


from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(opts)
    driver.implicitly_wait(10)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()

## setup --> webdriver.Chrome()

class TestRegister:

    def test_reg_link(self, setup):     ## setup --> webdriver.Chrome()
        setup.find_element('xpath', '//a[text()="Register"]').click()

    def test_gender_btn(self, setup):
        setup.find_element('id', 'gender-male').click()

    def test_fname(self, setup):
        setup.find_element('id', 'FirstName').send_keys('Abhishek')

    def test_lname(self, setup):
        setup.find_element('id', 'LastName').send_keys('U')

    def test_reg_email(self, setup):
        setup.find_element('id', 'Email').send_keys('abhi@gmail.com')

    def test_reg_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('abhi@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('id', 'ConfirmPassword').send_keys('abhi@12345')
        time.sleep(1)

class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('abhi@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('abhi@12345')

































