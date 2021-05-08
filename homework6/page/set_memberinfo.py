from appium.webdriver.common.mobileby import MobileBy

from test_appium424.page.base_page import BasePage
from test_appium424.page.edit_memberinfo import EditMemberInfoPage


class SetMemberInfoPage(BasePage):

    def goto_edit_member_info_page(self):
        # 点击[编辑成员]按钮
        edit_button = (MobileBy.XPATH, "//*[@text='编辑成员']")
        self.find(edit_button).click()
        return EditMemberInfoPage(self.driver)
