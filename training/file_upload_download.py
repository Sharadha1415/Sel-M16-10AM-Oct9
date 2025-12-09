import time


'''         Upload single file          '''
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# # file_path = r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_\demo.html'
# file_path = r"C:\Users\Ramya\OneDrive\Desktop\qoutation.pdf"
# driver.find_element('xpath', '//input[@id="singleFileInput"]').send_keys(file_path)


###################################################################################################

'''         Upload multiple files          '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# file1 = r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_\demo.html'
# file2 = r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_\myntra.png'
# file3 = r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\screenshots_\heading.png'
#
# driver.find_element('xpath', '//input[@id="multipleFilesInput"]').send_keys(f'{file1}\n{file2}\n{file3}')

###################################################################################################

'''         download files          '''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demoqa.com/upload-download')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Download"]').click()      ## The file will be downloded in the Downloads folder

##----------------------------------------------------------------------------
#
## Chrome
from selenium import webdriver
#
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

prefs = {
    "download.default_directory" : r"C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_",
    "download.prompt_for_download":False,
    "safebrowsing.enabled":True,
    "plugins.always_open_pdf_externally":True
}

opts.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(opts)

driver.get('https://demoqa.com/upload-download')
time.sleep(2)

driver.find_element('xpath', '//a[text()="Download"]').click()


'''
download.default_directory  -->     Sets the folder where the downloaded files will be stored
download.prompt_for_download    --> 
safebrowsing.enabled    -->     Enables Chromes's safe browsing so it doesnt block the download
'''

##----------------------------------------------------------------------------

## Firefox

from selenium import webdriver

opts = webdriver.FirefoxOptions()

opts.set_preference("browser.download.folderList", 2)
opts.set_preference("browser.download.dir", r'C:\Users\Ramya\PycharmProjects\Sel-Oct9-M16-10AM\files_')
opts.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(opts)

driver.get('https://demoqa.com/upload-download')
time.sleep(2)

driver.find_element('xpath', '//a[text()="Download"]').click()























