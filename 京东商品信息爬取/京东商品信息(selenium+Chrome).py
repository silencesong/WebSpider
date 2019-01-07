from selenium import webdriver
import time

class JDSpider:
    def __init__(self):
        self.url="https://www.jd.com/"
        #创建浏览器对象
        self.driver=webdriver.Chrome()

    def getPage(self):
        while True:
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            #提取数据
            rList=self.driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
            self.parsePage(rList)
            #点击下一页
            if self.driver.page_source.find('pn-next disabled')==-1:
                self.driver.find_element_by_class_name('pn-next').click()
                time.sleep(3)
            else:
                print("爬取结束")
                break

    def parsePage(self,rList):
        for r in rList:
            #print(r.text)
            contentList = r.text.split('\n')
            #print(contentList)
            price = contentList[0]
            name = contentList[1]
            commit = contentList[2]
            market = contentList[3]
            d={
	            "价格":price,
	            "名称":name,
	            "评论":commit,
	            "商店":market,
	        }
            self.writePage(d)
        
    def writePage(self,d):
        with open("jd.json","a",encoding="utf-8") as f:
            f.write(str(d)+"\n")

    def workOn(self):
        #发送请求，访问首页
        self.driver.get(self.url)
        #找到输入框对象
        text=self.driver.find_element_by_class_name("text")
        kw=input("请输入要搜索的内容：")
        text.send_keys(kw)
        #找到点击按钮对象
        button = self.driver.find_element_by_class_name('button')
        button.click()
        time.sleep(2)
        self.getPage()
        self.driver.quit()


if __name__=="__main__":
    spider=JDSpider()
    spider.workOn()
