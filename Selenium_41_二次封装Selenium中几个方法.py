import os
import time
from selenium1 import Selenium_40_Python自定义封装一个简单的Log类
logger = Selenium_40_Python自定义封装一个简单的Log类
mylog = logger.Logger(logger="basepage").getlog()

class basepage(object):
    """ 主要是把常用的几个Selenium方法封装到BasePage这个类，我们这里演示以下几个方法
    back()
    forward()
    get()
"""
    def __init__(self,driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver
    def back(self):
        """
        浏览器后退按钮
        :return:
        """
        self.driver.back()
    def forward(self):
        """
        浏览器的前进按钮
        :return:
        """
        self.driver.forward()
    def open_url(self,url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :return:
        """
        self.driver.quit()

    def take_screenshot(self):
        """
        截图并把图片放在Screenshot文件
        :return:
        """
        file_path = os.path.dirname(os.getcwd()) + "\\selenium1\\selenium测试框架\\screenshots\\"
        rq = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        screen_name =  file_path +rq + ".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylog.info("截图保存成功")
        except Exception as e:
            mylog.error("出现异常",format(e))
