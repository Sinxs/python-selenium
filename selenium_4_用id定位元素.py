from selenium import webdriver
dirver = webdriver.Chrome()
dirver.maximize_window()
dirver.implicitly_wait(8)
dirver.get("http://www.baidu.com")
try:
    dirver.find_element_by_id("kw")
    print("test pass: ID found")
except Exception as e:
    print("excetption found",format(e))
dirver.quit()
