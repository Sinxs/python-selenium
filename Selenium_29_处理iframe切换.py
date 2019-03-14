import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.126.com")
time.sleep(3)
# 因为没有测试条件 故未来再研究
for link in driver.find_elements_by_xpath("//*[@id]"):
    if "x-URS-iframe" in link.get_attribute("id"):  # 遍历所有id  找到匹配的
        print(link.get_attribute("id"))
        driver.switch_to.frame(link.get_attribute("id"))
        driver.find_element_by_xpath("//*[@class='j-inputtext dlemail']").send_keys("selenium switch test")  # 在帐号输入框内输入

time.sleep(2)
driver.switch_to.default_content()
driver.quit()

# driver.switch_to.frame("x-URS-iframe")  # 切换到iframe，若无此行代码，则找不到帐号输入框
# driver.find_element_by_xpath("//*[@class='j-inputtext dlemail']").send_keys("selenium switch test")  # 在帐号输入框内输入
#
# time.sleep(2)
# driver.quit()

# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.maximize_window()
#
# driver.get('https://music.163.com/')
#
# #driver.switch_to.frame('g_iframe')
#
# driver.find_element_by_link_text('华语').click()