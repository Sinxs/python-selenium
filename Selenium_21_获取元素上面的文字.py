import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com/")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@data-type='normal']").click()
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
# 第一种断言方法
try:
    error_messge = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error' and text()='请您输入手机/邮箱/用户名']").is_displayed()
    print("test pass")
except Exception as e:
    print("test fail",format(e))

# 第二种断言方法  推荐
error_messg = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error']").text

try:
    assert error_messg == "请您输入手机/邮箱/用户名"
    print("test pass")
except Exception as e:
    print("test fail",format(e))