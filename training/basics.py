import time

'''     Initializing Chrome browser     '''

from selenium import webdriver
c_driver = webdriver.Chrome()
time.sleep(20)

## The above command will close the browser automatically

##-------------------------------------------------------------------------------------------------

## To prevent the browser from automatically closing

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

c_driver = webdriver.Chrome(opts)

###################################################################################################

'''     Initialize Firefox browser      '''

# from selenium import webdriver
# f_driver = webdriver.Firefox()


## Firefox will not close automatically.
## So no need to consider FirefoxOptions and add_experimental_option

###################################################################################################

'''     Initialize Edge browser         '''

from selenium import webdriver
e_driver = webdriver.Edge()

## The above command will close the browser automatically

##-------------------------------------------------------------------------------------------------

## To prevent the browser from automatically closing

from selenium import webdriver

opts = webdriver.EdgeOptions()
opts.add_experimental_option("detach", True)

c_driver = webdriver.Edge(opts)

























































































