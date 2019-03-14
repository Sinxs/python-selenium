from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("https://www.baidu.com")
try:
    driver.find_element_by_tag_name("from")  # 可能是界面改版 这样定位不到  郁闷
    print("test pass:tag name found")
except Exception as e:
    print("Exception found:", format(e))