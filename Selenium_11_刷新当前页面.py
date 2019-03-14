from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
time.sleep(3)
try:
    driver.refresh()  # 刷新界面的方法
    time.sleep(3)
    print('test pass: refresh successful')
except Exception as e:
    print("Exception found", format(e))
driver.quit()