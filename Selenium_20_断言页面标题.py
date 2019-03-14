import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(1)
print(driver.title)
# 两种方式，第一种使用assert
try:
    assert "百度一下，你就知道" == driver.title
    print("assert test find pass")
    driver.quit()
except Exception as e:
    print("assert test find false")
    driver.quit()
# 第二种 if 语句
if "百度一下，你就知道" == driver.title:
    print("assert test find pass")
    driver.quit()
else:
    print("assert test find false")
    driver.quit()