import requests
import json
import unittest

class login_admin:
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def admin_login(self):
        self.content = {"fname":"admin","fpassword":"HGBnGUVR1HvaWkkniwVMvg=="}
        r=requests.post("http://120.76.94.241:3005/admin/login",data=content)
        print(r.status_code)
        print(r.text)
    admin_login()