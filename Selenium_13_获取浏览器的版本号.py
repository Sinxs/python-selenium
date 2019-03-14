from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com/")
time.sleep(1)
print(driver.capabilities['version'])  # 打印浏览器version的版本  version 需要用[]
print(driver.capabilities['chrome']['chromedriverVersion'])  # 打印chromedriver的值版本
driver.quit()

