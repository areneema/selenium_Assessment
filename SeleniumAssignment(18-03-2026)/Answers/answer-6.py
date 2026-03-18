# Go to https://www.irctc.co.in/nget/train-search
# enter from, to, select the date, handle the dropdowns and click on search trains
# try to book a train

import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 10)

driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
time.sleep(2)

driver.find_element('xpath','//input[@ aria-label="Enter From station. Input is Mandatory."]').send_keys("BBS")
time.sleep(1)
driver.find_element('xpath','//li[@ id="p-highlighted-option"]').click()

driver.find_element('xpath','//input[@ aria-label="Enter To station. Input is Mandatory."]').send_keys("KOL")
time.sleep(1)
driver.find_element('xpath','//li[@ id="p-highlighted-option"]').click()

driver.find_element('xpath','//input[@ class="ng-tns-c69-9 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]').click()
driver.find_element('xpath','(//td[@ class="ng-tns-c69-9 ng-star-inserted"])[20]').click()
time.sleep(1)

driver.find_element('xpath','//div[@ class="ng-tns-c76-10 ui-dropdown ui-widget ui-state-default ui-corner-all"]').click()
time.sleep(1)
driver.find_element('xpath','//li[@ aria-label="AC First Class (1A) "]').click()

driver.find_element('xpath','//div[@ class="ng-tns-c76-11 ui-dropdown ui-widget ui-state-default ui-corner-all"]').click()
time.sleep(1)
driver.find_element('xpath','//li[@ aria-label="TATKAL"]').click()
time.sleep(5)
driver.find_element('xpath','//button[contains(text()," Search Trains ")]').click()