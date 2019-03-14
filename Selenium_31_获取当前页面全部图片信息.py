import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0")
time.sleep(1)
for image in driver.find_elements_by_tag_name("img"):
    print(image.size)
    print(image.text)
    print(image.tag_name)
driver.quit()
