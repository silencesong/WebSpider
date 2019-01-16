from selenium import webdriver
from lxml import etree
import time
import requests
from YDM import *

#访问网站得到html
url="https://www.douban.com/"
headers={"User-Agent":"Mozilla/5.0"}
driver=webdriver.Chrome()
driver.get(url)
time.sleep(1)

#把验证码图片的链接提取出来，并发请求，保存到本地
parseHtml=etree.HTML(driver.page_source)
rLink=parseHtml.xpath("//img[@id='captcha_image']/@src")[0]
res=requests.get(rLink,headers=headers)
res.encoding="utf-8"
html=res.content
with open("yzm.jpg","wb") as f:
    f.write(html)

#通过打码平台识别验证码
cid, result = yundama.decode(filename, codetype, timeout)
print(result)

#用户名，密码，验证码，登录豆瓣
uname=driver.find_element_by_name('form_email')
uname.send_keys('#此处输入用户名')
pwd=driver.find_element_by_name('form_password')
pwd.send_keys('#此处输入密码')
yzm=driver.find_element_by_id('captcha_field')
yzm.send_keys(result)
time.sleep(3)
login=driver.find_element_by_class_name('bn-submit')
login.click()
time.sleep(3)
driver.quit()