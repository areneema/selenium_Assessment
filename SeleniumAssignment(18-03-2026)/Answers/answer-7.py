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

ac = ActionChains(driver)

driver.get("https://www.purplle.com/")
driver.maximize_window()
time.sleep(2)

brands = driver.find_element("xpath", "//a[text()='Brands']")
ac.move_to_element(brands).perform()
time.sleep(2)

driver.find_element("xpath", "//input[@placeholder='Search']").send_keys("lakme")
time.sleep(2)

driver.find_element("xpath", "//a[contains(text(),'Lakme')]").click()
time.sleep(3)

driver.find_element("class name", "product-card").click()
time.sleep(2)

driver.find_element("name", "pincode").send_keys("700001")

time.sleep(2)