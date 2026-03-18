# Go to https://porter.in/
# enter city
# click on packers and movers
# enter pickup location
# enter drop location
# enter phone num
# enter shifting date
# check the price

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
wait_obj=WebDriverWait(driver,10)

driver.get("https://porter.in/")
time.sleep(2)
driver.find_element('xpath', '(//img[@alt="drop down"])[1]').click()
driver.find_element('xpath', '(//img[@alt="City Image"])[12]').click()
driver.find_element('xpath', '//img[@ alt="Pn"] ').click()
driver.find_element('id', "custom-autocomplete-pickup-address-0.9068221632898938").send_keys("XYZ")
time.sleep(2)
driver.find_element('id', "custom-autocomplete-drop-address-0.5869221806398074").send_keys("ABC")
time.sleep(2)
driver.find_element('xpath', '(//input[@type="tel"])[2]').send_keys("098765432")
time.sleep(2)
driver.find_element('xpath', '(//input[@class="MuiInputBase-input MuiInput-input"])[2]').click()
time.sleep(2)
driver.find_element('xpath', '(//button[@class="MuiButtonBase-root MuiIconButton-root MuiPickersDay-day"])[1]').click()
time.sleep(2)
driver.find_element('xpath', '(//button[@class="FormInput_submit__S9hw2 FormInput_submit-enabled__ead4D LeadFormSubmitButton_submit-container__pDSDv"])[2]').click()
time.sleep(2)