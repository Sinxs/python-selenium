import time
import unittest
from selenium import webdriver
class BaiduSearch(unittest.TestCase):
    def setUp(self):
        """
        测试固件setUP()的代码，主要进行测试用例前的准备
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://www.baidu.com")
        print("测试固件setUP()的代码，主要进行测试用例前的准备\n")
    def tearDown(self):
        """
        测试固件tearDown的代码，主要是用例结束后运行
        :return:
        """
        self.driver.quit()
        print("测试固件tearDown的代码，主要是用例结束后运行\n")
    def test_baidu_search(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su")
        time.sleep(2)
        try:
            assert "AAAAAAAA" in self.driver.title
            print("test pass")
        except Exception as e:
            print("test fail",format(e))
    def test_A(self):
        print("下一个")

if __name__ == '__main__':
    unittest.main()

# coding=utf-8
# import time
# import unittest
# from selenium import webdriver
#
#
# class BaiduSearch(unittest.TestCase):
#
#     def setUp(self):
#         """
#         测试固件的setUp()的代码，主要是测试的前提准备工作
#         :return:
#         """
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(8)
#         self.driver.get("https://www.baidu.com")
#
#     def tearDown(self):
#         """
#         测试结束后的操作，这里基本上都是关闭浏览器
#         :return:
#         """
#         self.driver.quit()
#
#     def test_baidu_search(self):
#         """
#         这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
#         :return:
#         """
#         self.driver.find_element_by_id('kw').send_keys('selenium')
#         time.sleep(1)
#         try:
#             assert 'selenium' in self.driver.title
#             print('Test Pass.')
#         except Exception as e:
#             print('Test Fail.', format(e))
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
