from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("https://www.baidu.com")

try:
    driver.find_element_by_link_text("新闻")
    #driver.find_element_by_xpath("//a[2][contains(@class, 'mnav')]").click()  # 也可以用元素索引进行定位 就像 //a [2]
    #driver.find_element_by_xpath("//a[contains(@class, 'mnav')][2]").click()  # 还可以这样用元素索引进行定位
    print('test pass: element found by link text')
except Exception as e:
    print("Exception found", format(e))

