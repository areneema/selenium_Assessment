# Go to https://www.apollopharmacy.in/
# click on find doctors
# click on general physician
# click on the first doctor available
# select the date
# select the time
# click on continue


import time
from selenium import webdriver

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 10)

driver.get("https://www.apollopharmacy.in/")
driver.maximize_window()

time.sleep(5) #close all popups manually

driver.find_element('xpath','//a[text()="Find Doctors"]').click()
time.sleep(2)
driver.find_element('xpath','//p[text()="General Physician/ Internal Medicine"]').click()
time.sleep(2)
visit_doctor = WebDriverWait(driver,15).until(
    EC.element_to_be_clickable(("xpath","//span[contains(text(),'Visit Doctor')]"))
)
visit_doctor.click()
time.sleep(2)
driver.find_element('xpath','//p[text()="19"]').click()
time.sleep(2)
driver.find_element('xpath','//div[text()="11:30 AM"]').click()
time.sleep(2)
driver.find_element('xpath','//span[text()="Continue"]').click()
time.sleep(2)

print("Appointment flow executed")