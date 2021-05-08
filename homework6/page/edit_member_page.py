from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium424.page.base_page import BasePage


class EditMemberPage(BasePage):
    def edit_menber(self, name, numbers):
        # input name
        # input phonenum
        # click 保存
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)  # 输入姓名

        # 输入手机号，以下两种定位都可以
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'手机')]/../"
                  "android.widget.RelativeLayout/android.widget.RelativeLayout/"
                  "android.widget.EditText").send_keys(
            numbers)
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'手机')]/..//android.widget.EditText")
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()  # 点击保存
        from test_appium424.page.add_menber_page import AddMenberPage
        return AddMenberPage(self.driver)
