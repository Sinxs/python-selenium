from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)
driver.find_element_by_link_text("新闻").click()
time.sleep(1)
print(driver.title)
driver.quit()
