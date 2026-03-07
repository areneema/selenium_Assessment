import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver=webdriver.Chrome(opts)


# ##question:1
#
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(2)
# driver.find_element("xpath", "(//a[contains(text(), 'Books')])[3]").click()
# time.sleep(1)
# driver.find_element("xpath", "(//input[@value='Add to cart'])[1]").click()
# time.sleep(3)
# driver.find_element("xpath", "//span[text()='Shopping cart']").click()
# time.sleep(1)
#
# #verification
# product = driver.find_element("xpath","(//a[text()='Computing and Internet'])[2]").text
#
# if product:
#      print("Product present in cart:", product)

# ##question: 2
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(2)

# driver.find_element("xpath", "(//a[contains(text(), 'Electronics')])[3]").click()
# time.sleep(1)
# driver.find_element("xpath", "(//a[contains(text(), 'Cell phones')])[4]").click()
# time.sleep(1)

# ##question 3
#
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# time.sleep(2)
# driver.find_element('xpath', "//div[@id='start']").click()
# time.sleep(2)
# text = WebDriverWait(driver,10).until(EC.visibility_of_element_located("xpath","//h4[text()='Hello World!']"))
# print(text.text)


# ##question 4
#
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# driver.find_element('xpath', "//button[text()='Remove']").click()
# time.sleep(2)
#
# element= WebDriverWait(driver,10).until(EC.visibility_of_element_located(("xpath","//button[text()='Add']")))
# driver.find_element('xpath', "//button[text()='Add']").click()
# time.sleep(2)

# ##question 5
#
# driver.get("https://demoqa.com/select-menu")
# listbox = driver.find_element('xpath', '(//div[@class="css-19bb58m"])[1]')
# select_obj = Select(listbox)
#
# select_obj.select_by_visible_text("Group 2, option 1")
# time.sleep(1)
# selected = select_obj.first_selected_option.text
# print("Selected:",selected)
#
# ##question 6
# driver.get("https://demoqa.com/select-menu")
# time.sleep(3)
#
# multi = Select(driver.find_element("id","cars"))
# multi.select_by_visible_text("Volvo")
# multi.select_by_visible_text("Saab")
# multi.select_by_visible_text("Opel")
#
# options = multi.all_selected_options
#
# for i in options:
#     print(i.text)
#
# ##question 7
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/menu/")
#
# action = ActionChains(driver)
#
# main = driver.find_element("xpath","//a[text()='Main Item 2']")
# sub = driver.find_element("xpath","//a[text()='SUB SUB LIST']")
# item = driver.find_element("xpath","//a[text()='Sub Sub Item 1']")
#
# action.move_to_element(main).perform()
# action.move_to_element(sub).perform()
# item.click()
#
#
# ##question 8
#
# driver.get("https://demoqa.com/droppable")
#time.sleep(2)
#
# src = driver.find_element("id","draggable")
# tar = driver.find_element("id","droppable")
# time.sleep(2)
# ActionChains(driver).drag_and_drop(src,tar).perform()
# time.sleep(2)
#
# print(driver.find_element("id","droppable").text)

# ##question 9
#
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(2)
# driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()
# time.sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
#
# result = driver.find_element("id","result").text
# print(result)

# ##question 10
#
# driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(2)
# driver.find_element("id","file-upload").send_keys(r"C:\Users\KIIT\PycharmProjects\PythonProject\Selenium_Assessment\random")
# time.sleep(2)
# driver.find_element("id","file-submit").click()
# time.sleep(2)
# print(driver.find_element("id","uploaded-files").text)

#qyestion 14
# ##Write the steps to read the data from excel
# 1) pip install xlrd
# 2) first get the absolute path of the excel file and store it in a variabele (eg: path)
# 3) then we open the file using workbook =xlrd.open_workbook(path)
# 4) then we open the specific sheet using worksheet=workbook.sheet_by_name("Sheet_name")
# 5 )then finally we convert the sheet object into generator object to perform the python actions  rows= worksheet.get_rows()


#question 15
# ##Write the syntax for the xpath to locate the elements using
# 	*	attributes : //tag_name[@attribute_name="attribute_value"]
# 	*	text       : //tag_name[@text()="TEXT"]
# 	*	group indexing :(//tag_name[@attribute_name="attribute_value])[index]
# 	*	contains : //tag_name[contains(text(),"partial text")]








