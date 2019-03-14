# coding=utf-8
import configparser
import os
# class TestReadConfigFile(object):
#
#     def get_value(self):
#         # root_dir = os.path.dirname(os.path.abspath('.'))  # 获取项目根目录的相对路径
#         # print(root_dir)
#
#         config = configparser.ConfigParser()
#         file_path = os.path.abspath('.') + '\config\config.ini'
#         print(file_path)
#         config.read(file_path)
#
#         browser = config.get("browserType", "browserName")
#         url = config.get("testServer", "URL")
#
#         return (browser, url)  # 返回的是一个元组
# trcf = TestReadConfigFile()
# print(trcf.get_value())


# import configparser
# import os
class TestReadConfigFile(object):
    def get_value(self):
        config = configparser.ConfigParser()
        root_dir = os.path.abspath('.') + '\config\config.ini' # 获取项目根目录的相对路径+ini文件路径
        config.read(root_dir)
        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")
        return (browser, url)  # 返回的是一个元组
trcf = TestReadConfigFile()
print(trcf.get_value())




