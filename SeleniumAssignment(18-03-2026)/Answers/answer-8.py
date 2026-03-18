# Go to https://www.purplle.com/
# hover to brands
# search for lakme and click on it
# scroll until the first item is visible
# click on first product
# Enter pincode and check if it is available


import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from general_utilities.excel import excel_dt
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 10)

ac = ActionChains(driver)


data = excel_dt()
driver.get('https://lifeinsurance.adityabirlacapital.com/')
driver.implicitly_wait(10)
driver.find_element('xpath','(//a[text()="Her Insurance"])[2]').click()
time.sleep(2)
driver.find_element('id','firstName').send_keys(data['fname'])
driver.find_element('id','lastName').send_keys(data['lname'])
driver.find_element('id','email').send_keys(data['email'])
driver.find_element('id','phonenumber').send_keys(data['ph'])
