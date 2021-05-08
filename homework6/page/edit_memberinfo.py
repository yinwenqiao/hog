from appium.webdriver.common.mobileby import MobileBy

from test_appium424.page.base_page import BasePage
from test_selenium418.page.contact import ContactPage


class EditMemberInfoPage(BasePage):

    def edit_member_info(self):
        # from pages.contact_page import ContactPage
        delete_button = (MobileBy.XPATH, "//*[@text='删除成员']")
        confirm_button = (MobileBy.XPATH, "//*[@text='确定']")
        # 1.点击[删除成员]按钮
        self.swip_find(delete_button)
        # 2.点击[确定]按钮
        self.swip_find(confirm_button)
        # 3.删除成功，返回[通讯录]页面
        return ContactPage(self.driver)
