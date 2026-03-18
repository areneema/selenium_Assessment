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
driver.get('https://www.myntra.com/')
driver.maximize_window()


search = driver.find_element("class name", "desktop-searchBar")
search.send_keys("puma")
time.sleep(2)

search.send_keys(Keys.ARROW_DOWN)
search.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element("class name", "product-base").click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])

driver.find_element("xpath", "//div[text()='ADD TO BAG']").click()
time.sleep(2)

