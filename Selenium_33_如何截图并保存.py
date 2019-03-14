# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)

driver.get_screenshot_as_file(r"C:\Users\Administrator\Desktop\baidu.png")  # 前面加上 r 就不用双\\ 推荐
driver.quit()
