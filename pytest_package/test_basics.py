# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()
# logout()
#
# ## To execute the function, we should give the function call

#################################################################################################

# class Sample:
#
#     def login(self):
#         print("login executing")
#
#     def logout(self):
#         print("logout executing")
#
# s = Sample()
# s.login()
# s.logout()
#
# ## To execute the class, we should create the object and call the attributes

#################################################################################################

'''
Pytest  :   It is a unit testing framework
            Testing the small unit of the entire program we call it as unit-testing
            To perform unit testing in selenium, we use pytest

            To install pytest
                Go to command prompt    -->     pip install pytest

            RULES
            *   The file name should always start with test_ or end with _test
                Eg  :   test_filename.py        OR          filename_test.py
            *   The functions name should start with test_
                Eg  :   def test_funcname():
                            pass
            *   The classname also should start with Test
                Eg  :   class TestClassName:
                            pass

            When we follow the rules, pytest will automatically recognize the files, functions and classes which are following the rules
            So, we can execute the functions without calling them and we can execute the classes without creating the objects

'''
import time

# def test_login():
#     print("login executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing     PASSED
# ## test_basics.py::test_logout     logout executing    PASSED


##############################################################################################

# def test_login():
#     print("login executing")
#
# def signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing     PASSED
# ## test_basics.py::test_logout     logout executing    PASSED

'''
signup function is not following pytest rules, so it is not recognized by pytest.
So signup will not execute.
Pytest will not recognize the functions which are not following the rules
'''

# ##############################################################################################
#
# def test_login():
#     print("login executing")
#     def test_signup():
#         print("signup executing")
#
# ## collected 1 item
# ## test_basics.py::test_login      login executing         PASSED

'''
Incase of nested test_functions, pytest cannot recognize the inner test_function.
Pytest recognizes and executes only outer test_function 
'''

##############################################################################################
#
# def test_login():
#     raise Exception
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::test_login                              FAILED
# ## test_basics.py::test_signup     signup executing        PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

'''
NOTE    :   Error in one testcase will not affect the execution of the other testcases 
'''

##############################################################################################

# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# test_login()
# test_signup()
# test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::test_login      login executing             PASSED
# ## test_basics.py::test_signup     signup executing            PASSED
# ## test_basics.py::test_logout     logout executing            PASSED

'''
NOTE    :   We dont have to give the function call for the test_functions  
            Suppose we give the function call, then the execution will happen twice. 
            One is function call execution and the other one is pytest execution
'''

##############################################################################################

# def test_add(a, b):
#     print(a + b)
#
# ## collected 1 item
# ## test_basics.py::test_add        ERROR
# ## fixture 'a' not found

'''
We should not pass formal parameters for the test_functions
'''
##############################################################################################

# def test_add(a, b):
#     print(a + b)
#
# test_add(1, 2)
#
# ## collecting ... 3
# ## collected 1 item
# ## test_basics.py::test_add        ERROR

##############################################################################################

# def test_login():
#     print("hello world")
#
# def test_login():
#     print("hello universe")
#
# ## collected 1 item
# ## test_basics.py::test_login      hello universe          PASSED

##############################################################################################

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
# ## test_basics.py::TestSample::test_login      login executing         PASSED
# ## test_basics.py::TestSample::test_signup     signup executing        PASSED
# ## test_basics.py::TestSample::test_logout     logout executing        PASSED

# ##############################################################################################
#
# class Sample:
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
# ## collected 0 items

'''
The class is not following the rules
'''

##############################################################################################

# class TestSample:
#
#     def login(self):
#         print("login executing")
#
#     def signup(self):
#         print("signup executing")
#
#     def logout(self):
#         print("logout executing")
#
# ## collected 0 items

'''
attributes are not following the rules
'''

##############################################################################################

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
# s = TestSample()
# s.test_login()
# s.test_signup()
# s.test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing         PASSED
# ## test_basics.py::TestSample::test_signup     signup executing        PASSED
# ## test_basics.py::TestSample::test_logout     logout executing        PASSED


##############################################################################################

# class TestSample:
#
#     def test_login(self, name):
#         print("login executing")
#
# ## collected 1 item
# ## test_basics.py::TestSample::test_login      ERROR

##############################################################################################

# class TestSample:
#
#     def __init__(self):
#         pass
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
# ## collected 0 items
# ## PytestCollectionWarning: cannot collect test class 'TestSample' because it has a __init__ constructor (from: test_basics.py)

##############################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

class TestRegister:

    def test_reg_link(self):
        driver.find_element('xpath', '//a[text()="Register"]').click()

    def test_gender_btn(self):
        driver.find_element('id', 'gender-male').click()

    def test_fname(self):
        driver.find_element('id', 'FirstName').send_keys('Abhishek')

    def test_lname(self):
        driver.find_element('id', 'LastName').send_keys('U')

    def test_reg_email(self):
        driver.find_element('id', 'Email').send_keys('abhi@gmail.com')

    def test_reg_pwd(self):
        driver.find_element('id', 'Password').send_keys('abhi@12345')

    def test_confirm_pwd(self):
        driver.find_element('id', 'ConfirmPassword').send_keys('abhi@12345')
        time.sleep(1)

class TestLogin:

    def test_login_link(self):
        driver.find_element('xpath', '//a[text()="Log in"]').click()

    def test_login_email(self):
        driver.find_element('id', 'Email').send_keys('abhi@gmail.com')

    def test_login_pwd(self):
        driver.find_element('id', 'Password').send_keys('abhi@12345')




'''
fixtures, cbt, conftest, generate reports = 3
markers = 2
parallel execution/dep = 1

POM = 5
'''




















