# base_page.py 基类，init，
# 封装一些最基本的方法，便于后续维护
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(level=logging.INFO)


class BasePage:
    def __init__(self, driver: WebDriver = None):  # 在driver后加参数意思是给变量加一个类型提示
        self.driver = driver

    def find(self, by, value):
        logging.info(by)
        logging.info(value)
        # 查找元素
        return self.driver.find_element(by, value)

    def swip_find(self, text, num=5):
        # num 默认查找次数
        # 进入滑动查找，改变隐式等待时长，提高查找速度
        self.driver.implicitly_wait(2)
        # 滑动查找，通过外部传递的num次数，决定查找次数
        for i in range(0, num):

            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                # 如果找到了这个元素，则返回
                return element
            except NoSuchElementException:
                print("未找到，滑动")
                # 滑动一页，继续查找

                size = self.driver.get_window_size()  # 获取屏幕尺寸
                width = size['width']
                height = size['height']
                # return 'width', 'height'

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3
                duration = 2000  # ms
                # 完成滑动操作
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                # 如果达到 num-1次没有找到，则抛出这个异常
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{i}次，未找到")
