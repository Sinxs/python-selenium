from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待
driver.get("https://www.baidu.com/")
driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium官网")  # 搜索输入框输入Selenium
driver.find_element_by_xpath("//*[@id='su']").click()  #点击百度一下按钮
time.sleep(3)
# 第一种判断方法
print(driver.find_element_by_xpath("//div[@id='3']/h3[contains(@class, 't')]/a").is_displayed())
driver.quit()
# 第二种判断方法

# ele_string = driver.find_element_by_xpath("//div[@id='1']/h3[contains(@class, 't')]/a").txt
# if ele_string == u"Python--判断一个字符串是否包含某子串的几种方法":  # 填写自己的结果
#     print ("测试成功，结果和预期结果匹配！")

driver.quit()