# Go to https://www.netmeds.com/
# hover to medicines using ActionChains
# click on order online
# Go to order using prescription
# upload some text file using file upload popup


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
wait_obj=WebDriverWait(driver,10)
ac = ActionChains(driver)
driver.get("https://www.netmeds.com/")

driver.maximize_window()

driver.get("https://www.netmeds.com/")
time.sleep(2)

actions = ActionChains(driver)

medicines = driver.find_element("xpath", "//a[contains(text(),'Medicine')]")
actions.move_to_element(medicines).perform()
time.sleep(2)

driver.find_element("xpath", "(//a[contains(text(),'Order Online')])[1]").click()
time.sleep(2)

driver.find_element("xpath", "//button[text()=' Upload Prescription ']").click()
time.sleep(2)


