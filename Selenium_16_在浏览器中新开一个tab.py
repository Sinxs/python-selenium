import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://www.baidu.com/")
time.sleep(2)
"""很郁闷，打不开新的页签  暂时忽略以后再研究"""
driver.find_element_by_link_text("新闻").send_keys(Keys.CONTROL + 't')  # 很郁闷，打不开新的页签  暂时忽略以后再研究

time.sleep(2)
