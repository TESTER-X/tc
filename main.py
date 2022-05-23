import os
import time

from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\Desktop\selenium\geckodriver.exe')

driver.get("https://www.google.com/")
print('Test completed')

