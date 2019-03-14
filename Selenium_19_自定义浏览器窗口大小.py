import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 全屏
driver.get('https://www.baidu.com')
time.sleep(1)
print(driver.get_window_size())
driver.set_window_size(1920,1080)
time.sleep(1)
print(driver.get_window_size())
driver.set_window_size(5,5)
time.sleep(1)
print(driver.get_window_size())