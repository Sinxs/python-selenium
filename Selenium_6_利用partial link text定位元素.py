from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("https://www.baidu.com")
try:
    driver.find_element_by_partial_link_text("主页")  # 取部分text来定位元素
    print('test pass: element found by partial link text')
except Exception as e:
    print("Exception found", format(e))