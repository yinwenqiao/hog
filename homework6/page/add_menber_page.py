from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium424.page.base_page import BasePage


class AddMenberPage(BasePage):

    def addmenber_bymenual(self):
        # click 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()  # 点击手动输入添加
        from test_appium424.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

    def find_toat(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")  # 检查是否有'保存成功提示'

        # return True
