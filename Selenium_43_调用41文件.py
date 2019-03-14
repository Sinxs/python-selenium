from selenium1 import Selenium_41_二次封装Selenium中几个方法
from selenium import webdriver
import time
basepage = Selenium_41_二次封装Selenium中几个方法
class BaiduSearch(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(6)
    basepage = basepage.basepage(driver)

    def open_baidu(self,url):
        self.basepage.open_url(url)
        time.sleep(2)
        self.basepage.take_screenshot()
    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.basepage.take_screenshot()
        time.sleep(1)
        self.basepage.back()
        self.basepage.forward()

        # self.basepage.quit_browser()

    def test_take_screen(self):
        # self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)
        self.basepage.take_screenshot()
        self.basepage.quit_browser()


baidu = BaiduSearch()
baidu.open_baidu("https://www.baidu.com")
baidu.test_search()
baidu.test_take_screen()

