# coding=utf-8
import time
from selenium import webdriver



# coding=utf-8


class BasePage(object):
    """
    主要是把常用的几个Selenium方法封装到BasePage这个类，我们这里演示以下几个方法
    back()
    forward()
    get()
    quit()
    """

    def __init__(self, driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver

    def back(self):
        """
        浏览器后退按钮
        :param none:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()

    def open_url(self, url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()
class BaiduSearch(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys("Selenium")
        time.sleep(1)
        self.basepage.back()
        self.basepage.forward()
        self.basepage.quit_browser()


baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()