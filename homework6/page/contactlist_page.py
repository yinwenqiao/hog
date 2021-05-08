from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium424.page.add_menber_page import AddMenberPage
from test_appium424.page.base_page import BasePage
from test_appium424.page.personal_info import MemberInfoPage


class ContactListPage(BasePage):

    def goto_addmenber(self):
        # click添加成员
        self.swip_find('添加成员').click()
        return AddMenberPage(self.driver)

    def goto_member_info_page(self, name):
        # 点击要删除的成员姓名
        member_button = (MobileBy.XPATH, f"//*[@resource-id ='com.tencent.wework:id/dyi']//*[@text='{name}']")
        self.swip_find(member_button)
        return MemberInfoPage(self.driver)

    def get_memberlist(self):
        sleep(3)
        # 加入显示等待，等到'通讯录'可点击时，才可获取通讯录成员列表
        contact_button = (MobileBy.XPATH, "//*[@text='通讯录']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(contact_button))
        # 获取成员列表
        datas = self.driver.find_elements(MobileBy.CLASS_NAME, "android.widget.TextView")
        memberlist = [data.text for data in datas]
        print(memberlist)
        return memberlist
