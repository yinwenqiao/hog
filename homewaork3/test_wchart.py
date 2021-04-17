#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from time import sleep

import yaml
from selenium import webdriver


class TestDemo:
    def setup(self):
        # 实例化 driver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_Wework(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        # 在当前页面点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # 获取cookie信息
        cookie = self.driver.get_cookies()
        # 把cookie存入yaml文件中
        with open("data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)
        sleep(3)

    def test_add_newnumber(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # 读取cookie
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            print(yaml_data)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        # 访问首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()
        # 点击通讯录
        self.driver.find_element_by_id("menu_contacts").click()
        # 点击添加成员
        self.driver.find_element_by_link_text("添加成员").click()
        # 添加成员
        self.driver.find_element_by_id("username").send_keys("cathy")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("123456")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13312341234")
        # 取消通过邮件或短信发送企业邀请
        self.driver.find_element_by_name("sendInvite").click()
        self.driver.find_element_by_link_text("保存").click()
        sleep(5)
