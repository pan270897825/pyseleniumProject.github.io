#/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/13 2:39
# @Author  : Tomato
# @File    : browser_engine.py
# @Software: PyCharm
import configparser
import os

from selenium import webdriver

from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        # config.read(file_path,encoding='UTF-8'), 如果代码有中文注释，用这个，不然报解码错误

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()

