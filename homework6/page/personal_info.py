from appium.webdriver.common.mobileby import MobileBy

from test_appium424.page.base_page import BasePage
from test_appium424.page.set_memberinfo import SetMemberInfoPage


class MemberInfoPage(BasePage):

    def goto_set_member_info_page(self):
        # 点击右上角的[...]
        set_button = (MobileBy.ID, "com.tencent.wework:id/h8g")
        self.find(set_button).click()
        return SetMemberInfoPage(self.driver)
