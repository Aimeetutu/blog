#coding:utf-8
from selenium import webdriver
import unittest
import time


class bolg_detail(unittest.TestCase):
    u'''在初始化中通过cookies登录博客'''

    @classmethod
    def setUpClass(self):
        print("------测试初始化开始------")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.cnblogs.com/tuxiaomeng/")
        self.driver.implicitly_wait(5)

        c1 = {u'domain':u'.cnblogs.com',
            u'name':u'.CNBlogsCookie',
            u'value':u'9957FEC53AA558CA801E4C6BB64649D54E8814FE4DE18D0171BE162A84E5040F37214DE06FE0395B12FC41934153385E14B917CB825A09C14196DC9DDE2A3C6CAE8383531B645A0A5AD1C3EBBAD8035A97C2ADC5',
            u'expiry':1603527617,
            u'path':u'/',
            u'httpOnly':True,
            u'secure':False}

        c2 = {u'domain':u'.cnblogs.com',
                  u'name':u'.Cnblogs.AspNetCore.Cookies',
                  u'value':u'CfDJ8J0rgDI0eRtJkfTEZKR_e81ZcNz-7PPUItW1jve7ZNTUXUTHMcWKjs4WJqFoangpuT5UgMA0nYxPWnPzkf6xgXdgx4XR8WPSnNs2NqmYoc4d8qbp3hPFvK6MX9Oixef5d5NfoJQW3pElNDSPH8bttb9nVOX7_G-spSbZPEVQYIPWTsmjN8R1-YW4YQ7BAZvehSPZN5VlbuKwakp9F5yTFsV9CiRFdu-iD588h3QF75WQJhD2KhBe1qSbaLqXys7Unn0dHCk00dUw4xVkOnhoAd-3INRocYTsFMjEkp4c72NCFSii-2R3exV2Gpqendamaw',
                  u'expiry':1603527617,
                  u'path':u'/',
                  u'httpOnly':True,
                  u'secure':False}

        self.driver.add_cookie(c1)
        self.driver.add_cookie(c2)
        self.driver.implicitly_wait(5)
        self.driver.refresh()

    @classmethod
    def tearDownClass(self):
        print('------测试清除------')
        self.driver.quit()

    def test_is_nickname(self):
        u'''获取登录后的昵称是否一致'''
        self.driver.find_element_by_link_text("图小萌").click()
        self.driver.get_screenshot_as_base64()
        text = self.driver.find_element_by_class_name("display_name").text
        self.assertEqual(text,u'图小萌')
        print("昵称显示为：%s"%text)


    def test_is_bolg_status(self):
        u'''获取博客标签数量是否一致'''
        text = self.driver.find_element_by_id("blog_stats").text
        self.assertIn(u'随笔-5',text)
        print("博客状态显示为I：%s" % text)


