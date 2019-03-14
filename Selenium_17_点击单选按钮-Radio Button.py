
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://news.baidu.com/")
# 实际上，勾选一个单选按钮，也就是调用元素方法click()我们利用for语句遍历这两个单选按钮，依次点击他们。
for i in driver.find_elements_by_xpath("//*/input[@type='radio']"):  # 找准元素 呵呵哒  @name='tn' 可用但是会报错
    i.click()
    print(i)

