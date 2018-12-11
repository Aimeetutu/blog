from selenium import webdriver
import time




driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/tuxiaomeng/")
driver.implicitly_wait(5)


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

driver.add_cookie(c1)
driver.add_cookie(c2)
driver.implicitly_wait(5)
driver.refresh()


driver.find_element_by_link_text("图小萌").click()
text = driver.find_element_by_class_name("display_name").text
print(text)

# driver.quit()