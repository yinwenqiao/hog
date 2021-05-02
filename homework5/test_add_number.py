# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWx():
    def setup(self):
        # 初始化
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "cathy"
        caps["settings[waitForIdleTimeout]"] = 0
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 客户端与服务端建立连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待，更智能，中间任何时间等到某个元素都停止查找，继续往后执行
        # 每次调用find_element的时候都会激活这种等待方式
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 资源销毁
        self.driver.quit()

    def test_case(self):
        # 测试用例
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click(),
        # uiaotomator的定位方式，Android原生的定位方式，滚动查找某个文字
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 点击姓名输入框
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ays']").click()
        # 输入姓名
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ays']").send_keys('小贝壳')
        # 点击手机输入框
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/f4m']").click()
        # 输入手机号
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/f4m']").send_keys(
            '13312341234')
        # 点击保存
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ac9']").click()
