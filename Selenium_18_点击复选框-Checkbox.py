import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.implicitly_wait(8)
# 以百度举例，登录时，勾选下次自动登录：
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
driver.find_element_by_xpath("//*[@data-type='normal']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@type='checkbox']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@type='checkbox']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@type='checkbox']").click()