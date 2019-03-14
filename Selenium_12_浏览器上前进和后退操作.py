import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
time.sleep(2)

elem_news = driver.find_element_by_link_text("新闻")
elem_news.click()  # 界面进入百度新闻
time.sleep(2)
driver.back()  # 界面回到首页
time.sleep(2)
driver.forward()  # 界面在次进入百度新闻
time.sleep(2)
driver.quit()