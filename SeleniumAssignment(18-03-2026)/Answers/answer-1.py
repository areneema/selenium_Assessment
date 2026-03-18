# Go to Facebook
# Enter username & password
# Wait for login button to be clickable
# Click login
# Validate login success

import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=opts)
wait_obj=WebDriverWait(driver,10)

driver.get("https://www.facebook.com/")
time.sleep(2)
driver.find_element('xpath', '//input[@id="_R_1h6kqsqppb6amH1_"]').send_keys("ArunimaMohanty")
time.sleep(2)
driver.find_element('xpath','//input[@id="_R_1hmkqsqppb6amH1_"]').send_keys("Arunima@1234")
time.sleep(2)

# try:
#     button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable('xpath', '//div[@class="x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np x972fbf x10w94by x1qhh985 x14e42zd x9f619 xtvsq51 xqbgfmv xbe3n85 x7a1id4 x1d9i5bo x1xila8y x1bumbmr xc8cyl1"]')
#     )
#     print("Button is clickable")
# except TimeoutException:
#     print("Button is NOT clickable")


driver.find_element('xpath', '//div[@class="x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np x972fbf x10w94by x1qhh985 x14e42zd x9f619 xtvsq51 xqbgfmv xbe3n85 x7a1id4 x1d9i5bo x1xila8y x1bumbmr xc8cyl1"]').click()
time.sleep(2)

try:
    wait_obj.until(EC.visibility_of_element_located(('xpath', '//div[@class="x1ja2u2z x78zum5 x2lah0s x1n2onr6 xl56j7k x6s0dn4 xozqiw3 x1q0g3np x972fbf x10w94by x1qhh985 x14e42zd x9f619 xtvsq51 xqbgfmv xbe3n85 x7a1id4 x1d9i5bo x1xila8y x1bumbmr xc8cyl1"]')))
    print("Valid credentials. Successfull login")
except:
    print("Invalid credentials. Unsuccessfull login")
