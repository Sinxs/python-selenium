from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(7)
driver.get("https://www.baidu.com")
try:
    driver.find_element_by_class_name("s_ipt")
    print('test pass: find s_ipt')
except Exception as e:
    print("Exception found", format(e))
  