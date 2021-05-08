# app相关的操作，启动，关闭，重启
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from test_appium424.page.base_page import BasePage
from test_appium424.page.main_page import Mainpage


class App(BasePage):
    def start(self):
        if self.driver == None:
            print('self.driver==None,初始化driver')
            # 启动app
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "cathy"
            caps["settings[waitForIdleTimeout]"] = 0
            caps["noReset"] = "true"
            # caps["ensureWebviewsHavePages"] = True
            caps["skipDeviceInitialization"] = True
            # 客户端与服务端建立连接
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待，更智能，中间任何时间等到某个元素都停止查找，继续往后执行
            # 每次调用find_element的时候都会激活这种等待方式
            self.driver.implicitly_wait(5)
        else:
            print('复用driver')
            # 复用driver
            # start_activity 启动页面，可以运行过程中启动其他app或者
            # self.driver.start_activity(package_name,activity_name)
            self.driver.launch_app()
        return self

    def restart(self):
        # self.driver
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # quit(销毁这个driver)
        self.driver.quit()

    def goto_main(self):
        # 入口,进入企业微信主页面
        return Mainpage(self.driver)
