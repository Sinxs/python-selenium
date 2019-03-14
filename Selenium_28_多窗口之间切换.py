# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
time.sleep(1)

# driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a").click()
# print(driver.current_window_handle)  # 输出当前窗口句柄
# handles = driver.window_handles  # 获取当前全部窗口句柄集合
# print(handles)  # 输出句柄集合
#
# for handle in handles:  # 切换窗口
#     if handle != driver.current_window_handle:
#         print('switch to second window', handle)
#         driver.close()  # 关闭第一个窗口
#         driver.switch_to.window(handle)  # 切换到第二个窗口
news_link = driver.find_element_by_xpath("//li[contains(@class, 'hdline0')]/strong/a[contains(@class, 'a3')]")
page1_title_string = news_link.text
news_link.click()
time.sleep(2)
print(driver.current_window_handle) # 输出当前窗口句柄
handles = driver.window_handles  # 获取当前全部窗口句柄集合
for handle in handles:  # 循环遍历当前所有窗口的句柄
    print(driver.current_window_handle) 
    if handle != driver.current_window_handle:  # 判断所希望的句柄
        print('switch to second window', handle)
        driver.close() # 关闭当前窗口
        print(handle)
        time.sleep(2)
        driver.switch_to.window(handle) # 切换窗口句柄
print(handle)
page2_title_string = driver.find_element_by_xpath("//h1").text
# 使用title判断是否切换成功
try: 
    assert page1_title_string in page2_title_string
    print("test pass")
    driver.quit()
except Exception as e:
    print("test fail",format(e))
    driver.quit()

