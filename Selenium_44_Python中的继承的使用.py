from selenium import webdriver
import time

class ClassA(object):
    def open_baidu(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.baidu.com")
        time.sleep(2)
        driver.quit()


class ClassB(ClassA):
    def test_inherit(self):
        self.open_baidu()

ClassB().test_inherit()
