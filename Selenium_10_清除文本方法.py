from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
try:
    driver.find_element_by_id("kw").clear()  # 调用clear方法去清除已经输入的selenium
    time.sleep(2)
    print('test pass: clean successful')
except Exception as e:
    print("Exception found", format(e))

driver.quit()