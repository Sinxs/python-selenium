import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)
element = driver.find_element_by_xpath("//*[@id='lg']/img")
actionChains = ActionChains(driver)
# 这时只能操作右键第一个选项，如果想要是用按键来选中特定选项的话 需要引入 pywin32 模块 可以百度到
actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
# actionChains.context_click(element).send_keys("i").perform()
