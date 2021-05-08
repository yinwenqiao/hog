from faker import Faker

from test_appium424.page.app import App
from test_appium424.utils.contact_info import ContactInfo


class TestContact:
    def setup_class(self):
        self.contactinfo = ContactInfo()
        self.app = App()

    def setup(self):
        # 启动app
        self.main = self.app.start().goto_main()

    def teardowm(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        name = self.contactinfo.get_name()
        numbers = self.contactinfo.get_phonenum()
        self.main.goto_contactlist(). \
            goto_addmenber().addmenber_bymenual(). \
            edit_menber(name, numbers).find_toat()

    def test_delete_member(self, name):
        memberlist = self.main.goto_contact_page(). \
            goto_member_info_page(name). \
            goto_set_member_info_page(). \
            goto_edit_member_info_page(). \
            edit_member_info(). \
            get_memberlist()
        assert name not in memberlist

    # def test_addcontact1(self):
    #     name = self.contactinfo.get_name()
    #     numbers = self.contactinfo.get_phonenum()
    #     self.main.goto_contactlist().\
    #         goto_addmenber().addmenber_bymenual().\
    #         edit_menber(name,numbers).find_toat()

    def test_delcontact(self):
        if __name__ == '__main__':
            self.main.goto_contactlist()
