import requests
from lxml import etree
import pymongo

class QiushiSpider:
    def __init__(self):
        self.baseurl="https://www.qiushibaike.com/text/page/"
        self.headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        #连接对象
        self.conn=pymongo.MongoClient("192.168.71.128",27017)
        #库对象
        self.db=self.conn["Qiushidb"]
        #集合对象
        self.myset=self.db["zhuanye"]
        
    #获取页面
    def getPage(self,url):
        res=requests.get(url,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        self.parsePage(html)
    
    #解析并写入数据库
    def parsePage(self,html):
        parseHtml=etree.HTML(html)
        #基准xpath，匹配每个段子的对象
        baseList=parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        #for循环遍历每个段子对象，一个一个提取
        for base in baseList:
            #用户昵称
            username=base.xpath('./div/a/h2')
            if username:
                username=username[0].text
            else:
                username="匿名用户"
            #段子内容
            content=base.xpath('./a/div[@class="content"]/span[1]/text()')
            content="".join(content)
            #好笑数量
            laughNum=base.xpath('.//i[@class="number"]')[0].text
            #评论数量
            pingNum=base.xpath('.//i[@class="number"]')[1].text
            #定义字典存mongo
            d={
                "username":username.strip(),
                "content":content.strip(),
                "laughNum":laughNum.strip(),
                "pingNum":pingNum.strip()
                    }
            self.myset.insert_one(d)
    
    #主函数
    def workOn(self):
        print("正在爬取...")
        for i in range(1,14):
            url=self.baseurl+str(i)
            self.getPage(url)
        print("爬取结束,存入Qiushidb库")
    
if __name__=="__main__":
    spider=QiushiSpider()
    spider.workOn()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    