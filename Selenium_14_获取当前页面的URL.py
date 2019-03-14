from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com/")
time.sleep(1)
driver.find_element_by_link_text("新闻").click()
print(driver.current_url)  # current_url方法可以获取到当前界面的url
time.sleep(2)
driver.quit()