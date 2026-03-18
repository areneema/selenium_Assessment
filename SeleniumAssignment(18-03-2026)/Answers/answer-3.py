# Go to myntra
# search for puma
# select any option from the auto-suggestions and click on it
# select the product(will open in new tab)
# handle the new tab
# add product to cart

import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option('Detach', True)

driver = webdriver.Chrome(opts)

driver.get("https://www.icici.bank.in/")
driver.maximize_window()
time.sleep(2)

driver.find_element("xpath", "//span[contains(text(),' Accounts')]").click()
time.sleep(2)

driver.find_element("xpath", '(//a[@data-itm="nli_savingsAccount_accounts_savingsAccount_productPageHeroBanner_1CTA_CMS_apply_CAMPAIGNS"])[2]').click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])

driver.find_element("xpath", '//input[@id="name"]').send_keys("Neema")
driver.find_element("xpath", '//input[@id="mobile_number"]').send_keys("8340495052")

driver.find_element("xpath", "//button[contains(text(),'Apply')]").click()
time.sleep(2)

print("Validation message displayed")