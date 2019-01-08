from selenium import webdriver
from lxml import etree
import csv

# 创建浏览器对象,发请求
driver = webdriver.Chrome()
driver.get("https://www.douyu.com/directory/all")

class DouyuSpider:
    def __init__(self):
        self.n = 0
        self.page = 1
    
    # 获取主播名称、观众数量
    def getData(self):
        # 创建xpath的解析对象
        parseHtml = etree.HTML(driver.page_source)
        names = parseHtml.xpath('//div[@id="live-list-content"]//span[@class="dy-name ellipsis fl"]/text()')
        numbers = parseHtml.xpath('//div[@id="live-list-content"]//span[@class="dy-num fr"]/text()')
        # names : ["主播1","主播2",....] 
        # numbers:["90.8万","90万",...]
        # zip(L1,L2) : [(1,"A"),(2,"B"),(3,"C")]
        
        for name,number in zip(names,numbers):
            L = [name.strip(),number.strip()]
            self.writeData(L)
            self.n += 1
    # 保存到csv文件
    def writeData(self,L):
        with open("斗鱼直播.csv","a",newline="",encoding="gb18030") as f:
            writer = csv.writer(f)
            writer.writerow(L)
            
    # 主函数
    def workOn(self):
        for i in range(1,11):
            self.getData()
            print("第%d页爬取成功" % i)
            # 如果找不到不能点的下一页的class,去点击下一页
            if driver.page_source.find("shark-pager-next shark-pager-disable shark-pager-disable-next") == -1:
                driver.find_element_by_class_name("shark-pager-next").click()
            else:
                print("爬取完成")
                break
        print("一共有%d个主播" % self.n)
            
if __name__ == "__main__":
    spider = DouyuSpider()
    spider.workOn()
    
    
    
    
















