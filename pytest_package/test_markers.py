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

@pytest.mark.skip
class TestSample:

    def test_login(self):
        print("login executing")

    def test_reg(self):
        print("reg executing")

    def test_signup(self):
        print("signup executing")

    def test_logout(self):
        print("logout executing")

## collected 4 items
## test_markers.py::TestSample::test_login     SKIPPED (unconditional skip)
## test_markers.py::TestSample::test_reg       SKIPPED (unconditional skip)
## test_markers.py::TestSample::test_signup    SKIPPED (unconditional skip)
## test_markers.py::TestSample::test_logout    SKIPPED (unconditional skip)



























