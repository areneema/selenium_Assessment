# Go to https://www.netmeds.com/
# click on signin
# enter your valid mobile number
# click get otp
# enter the otp and validate the succesfull login

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
driver.get("https://www.netmeds.com/")
driver.maximize_window()

driver.find_element('xpath','//div[@class="position-relative profile-name"]').click()
time.sleep(2)

driver.find_element('xpath','//input[@name="mobile-number"]').send_keys("8340495052")
time.sleep(2)

driver.find_element('xpath','//button[contains(text(),"Get OTP")]').click()
time.sleep(10)

try:
    wait.until(EC.visibility_of_element_located(('xpath', '//button[contains(text()," Get started ")]')))
    print("Login Successful")
except:
    print("Login Failed")

time.sleep(2)


