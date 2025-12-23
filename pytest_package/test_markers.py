'''
Markers     :   To group the testcases, we use markers

There are 2 types of markers
    *   custom markers
    *   Inbuilt markers :   There are 4 types
                            *   skip
                            *   skipif
                            *   parametrize
                            *   xfail

'''

import time
import pytest


# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_marker.py -vs -m="sanity"        -->     test_reg and test_signup executed

##########################################################################################################
#
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_marker.py -vs -m="sanity"                --> test_login and test_signup will execute
# ## pytest test_marker.py -vs -m="smoke"                 --> test_reg will execute
# ## pytest test_marker.py -vs -m="regression"            --> test_logout will execute
# ## pytest test_marker.py -vs -m="smoke and sanity"      --> 0
# ## pytest test_marker.py -vs -m="regression and sanity" --> 0
# ## pytest test_marker.py -vs -m="regression and smoke"  --> 0
# ## pytest test_marker.py -vs -m="regression or sanity"  --> test_login, test_signup and test_logout will execute
# ## pytest test_marker.py -vs -m="smoke or sanity"       --> test_login, test_reg and test_signup will execute
# ## pytest test_marker.py -vs -m="regression or smoke"   --> test_reg and test_logout will execute
# ## pytest test_marker.py -vs -m="not smoke"             --> test_login, test_signup and test_logout
# ## pytest test_marker.py -vs -m="not sanity"            --> test_reg and test_logout will execute
# ## pytest test_marker.py -vs -m="not regression"        --> test_login, test_reg and test_signup will execute

##########################################################################################################

# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.regression
# @pytest.mark.smoke
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_marker.py -vs -m="sanity"                --> test_login and test_signup
# ## pytest test_marker.py -vs -m="smoke"                 --> test_login and test_reg and test_logout will execute
# ## pytest test_marker.py -vs -m="regression"            --> test_reg and test_logout will execute
# ## pytest test_marker.py -vs -m="smoke and sanity"      --> test_login will execute
# ## pytest test_marker.py -vs -m="sanity and regression" --> 0
# ## pytest test_marker.py -vs -m="smoke and regression"  --> test_reg and test_logout will execute
# ## pytest test_marker.py -vs -m="sanity or smoke"       --> All 4 will execute
# ## pytest test_marker.py -vs -m="sanity or regression"  --> All 4 will execute
# ## pytest test_marker.py -vs -m="smoke or regression"   --> test_login, test_reg and test_logout will execute
# ## pytest test_marker.py -vs -m="not sanity"            --> test_reg and test_logout will execute
# ## pytest test_marker.py -vs -m="not smoke"             --> test_signup will execute
# ## pytest test_marker.py -vs -m="not regression"        --> test_login and test_signup will execute

##########################################################################################################

# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login     login executing     PASSED
# ## test_markers.py::TestSample::test_reg       reg executing       PASSED
# ## test_markers.py::TestSample::test_signup    signup executing    PASSED
# ## test_markers.py::TestSample::test_logout    logout executing    PASSED

##########################################################################################################

# @pytest.mark.sanity
# class TestSample:
#
#     @pytest.mark.smoke
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.regression
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## In terminal
# ## pytest test_marker.py -vs -m="sanity"                --> All 4 will execute
# ## pytest test_marker.py -vs -m="smoke"                 --> test_login will execute
# ## pytest test_marker.py -vs -m="regression"            --> test_signup will execute
# ## pytest test_marker.py -vs -m="sanity and smoke"      --> test_login will execute
# ## pytest test_marker.py -vs -m="sanity and regression" --> test_signup will execute
# ## pytest test_marker.py -vs -m="smoke and regression"  --> 0
# ## pytest test_marker.py -vs -m="sanity or smoke"       --> All 4 will execute
# ## pytest test_marker.py -vs -m="sanity or regression"  --> All 4 will execute
# ## pytest test_marker.py -vs -m="smoke or regression"   --> test_login and test_signup will execute


##########################################################################################################

# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#
# @pytest.mark.regression
# class TestExample:
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

##########################################################################################################
'''
skip    :   To skip the execution of the testcases, we use skip marker
            It is an unconditional skip. To skip the testcases we dont have to pass any reason or condition.
            Reason is optional parameter.
            It will skip the testcases which are decorated with @pytest.mark.skip
            
            SYNTAX  :   @pytest.mark.skip
                        def test_case():
                            pass 
'''

# @pytest.mark.skip
# def test_login():
#     print("login executing")
#
# def test_reg():
#     print("reg executing")
#
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login                             SKIPPED (unconditional skip)
# ## test_markers.py::test_reg           reg executing       PASSED
# ## test_markers.py::test_signup        signup executing    PASSED
# ## test_markers.py::test_logout                            SKIPPED (unconditional skip)


###############################################################################################

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip(reason="reg already done")
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.skip(reason="signup already done")
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login                 login executing     PASSED
# ## test_markers.py::test_reg                                       SKIPPED (reg already done)
# ## test_markers.py::test_signup                                    SKIPPED (signup already done)
# ## test_markers.py::test_logout                logout executing    PASSED

###############################################################################################

# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login     SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_reg       SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup    SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout    SKIPPED (unconditional skip)

###############################################################################################
'''
skipif  :   skipif is also used to skip the execution of the testcases, but the skip is based on a condition.
            It takes two parameters, condition and reason.
            condition is the first parameter, reason is the second parameter.
            Both are mandatory parameters
            
            SYNTAX  :   @pytest.mark.skipif(condition, reason)
                        def test_case():
                            pass
                        
                        If the condition is True, it will skip the execution of the testcase
                        If the condition is False, it will execute the testcase 
            
'''


# @pytest.mark.skipif(True, reason='login already done')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login         SKIPPED (login already done)

# ##---------------------------------------------------------------------------------------------
#
# @pytest.mark.skipif(False, reason='login already done')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     login executing         PASSED

##---------------------------------------------------------------------------------------------

# @pytest.mark.skipif(False)
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login         ERROR
#
# ## In the above testcase, reason is not specified, thats why its giving error.
# ## reason is the mandatory parameter

##---------------------------------------------------------------------------------------------

# @pytest.mark.skipif(reason="login already completed")
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     SKIPPED (login already completed)
#
# ## When the condition is not gives, by default it will be considered as True.
# ## That's why the testcase is skipped when no conditions are given

# ##---------------------------------------------------------------------------------------------
'''
skip    :
'''
# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# def test_login():
#     driver.find_element("id", "user-name").send_keys('standard_user')
#     time.sleep(1)
#     driver.find_element('id', 'password').send_keys('secret_sauce')
#     time.sleep(1)
#     driver.find_element('id', 'login-button').click()
#     time.sleep(3)
#
# def test_logout():
#     if 'inventory' not in driver.current_url:
#         pytest.skip("login is unsuccessfull")
#
#     driver.find_element('id', 'react-burger-menu-btn').click()
#     time.sleep(2)
#     driver.find_element('id', 'logout_sidebar_link').click()

###################################################################################################

'''
xfail   :   This is an expected failure

            SYNTAX  :   @pytest.mark.xfail
                        def test_func():
                            pass  
                        
                        We are expecting the test_func to fail.
                        If the testcase is failed, then the output will be XFAIL
                        If the testcase is passed, then the output will be XPASS
'''


# @pytest.mark.xfail
# def test_login():               ## expected failure
#     raise Exception
#
# def test_signup():
#     print("signup executing")
#
# def test_reg():
#     prt("reg executing")
#
# ## collected 3 items
# ## test_markers.py::test_login                             XFAIL
# ## test_markers.py::test_signup        signup executing    PASSED
# ## test_markers.py::test_reg                               FAILED
#
############################################################################################

# @pytest.mark.xfail
# def test_login():               ## expected failure
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_reg():
#     prt("reg executing")
#
# ## collected 3 items
# ## test_markers.py::test_login     login executing     XPASS
# ## test_markers.py::test_signup    signup executing    PASSED
# ## test_markers.py::test_reg                           FAILED

############################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
#
# @pytest.mark.xfail
# def test_login():
#     driver.find_element("id", "user-name").send_keys('standard_user')
#     time.sleep(1)
#     driver.find_element('id', 'password').send_keys('secret_sauceee')
#     time.sleep(1)
#     driver.find_element('id', 'login-button').click()
#     time.sleep(3)
#
#     assert 'inventory' in driver.current_url

############################################################################################

'''
parametrize     :   
'''


# @pytest.mark.parametrize("a, b", [(10, 20)])
# def test_add(a, b):
#     print(a + b)
#
# ## a, b --> (10,20)
# ## a-->10,  b-->20
#
# ## collected 1 item
# ## test_markers.py::test_add[10-20]    30      PASSED


###########################################################################################

# @pytest.mark.parametrize("a, b", [(10, 20), 30])
# def test_add(a, b):
#     print(a + b)
#
# ## a,b --> (10, 20)
# ## a,b --> 30
#
# ## collected 0 items / 1 error


###########################################################################################

# @pytest.mark.parametrize("a, b", [(10, 20), (30, 40), (-10, 10), (1, 1), (10, -10)])
# def test_add(a, b):
#     print(a + b)
#
# ## collected 5 items
# ## test_markers.py::test_add[10-20]    30      PASSED
# ## test_markers.py::test_add[30-40]    70      PASSED
# ## test_markers.py::test_add[-10-10]   0       PASSED
# ## test_markers.py::test_add[1-1]      2       PASSED
# ## test_markers.py::test_add[10--10]   0       PASSED

###########################################################################################

# @pytest.mark.parametrize("a, b", [(10, 20)])
# def test_add(a, b, c):
#     print(a + b + c)
#
# ## ERROR
# ## Formal and actual arguments are not matching

# #################################################################################
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.get('https://www.saucedemo.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()
#
#
# @pytest.mark.parametrize("username, pwd", [("standard_user", "secret_sauce"),
#                                            ("standard_user", "invalid"),
#                                            ("abcdefgh", "standard_user"),
#                                            ("standard_user", "secret_sauce")])
# def test_login(username, pwd, setup):
#     setup.find_element("id", "user-name").send_keys(username)
#     time.sleep(1)
#     setup.find_element('id', 'password').send_keys(pwd)
#     time.sleep(1)
#     setup.find_element('id', 'login-button').click()
#     time.sleep(3)
#
#     try:
#         assert 'inventory' in setup.current_url
#         print("successfull login")
#     except:
#         print("unsuccessfull login")

#################################################################################


## Stored the login credentials in an excel file(ddt\login_credentials.xlsx)
## reading the login credentials(ddt\read_login_data.py)

from selenium import webdriver
from ddt.read_login_data import read_login_credentials

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

login_data = read_login_credentials()

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(opts)
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    yield driver
    driver.close()


@pytest.mark.parametrize("username, pwd", login_data)
def test_login(username, pwd, setup):
    setup.find_element("id", "user-name").send_keys(username)
    time.sleep(1)
    setup.find_element('id', 'password').send_keys(pwd)
    time.sleep(1)
    setup.find_element('id', 'login-button').click()
    time.sleep(3)

    try:
        assert 'inventory' in setup.current_url
        print("successfull login")
    except:
        print("unsuccessfull login")

















































