from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium424.page.base_page import BasePage
from test_appium424.page.contactlist_page import ContactListPage


# 主页面
class Mainpage(BasePage):
    contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        # click 通讯录
        self.find(*self.contact_element).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()  # 点击通讯录
        return ContactListPage(self.driver)
