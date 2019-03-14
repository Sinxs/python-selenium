from selenium import webdriver
import re
driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待
driver.get("http://home.baidu.com/contact.html")
doc = driver.page_source
emails = re.findall("[\w]+@[\w\.-]+",doc)
for email in emails:
    print(email)
    