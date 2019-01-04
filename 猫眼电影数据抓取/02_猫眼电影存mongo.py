import urllib.request
import re
import pymongo

class MaoyanSpider:
    def __init__(self):
        self.baseurl="https://maoyan.com/board/4?offset="
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
        self.offset=0
        #创建连接对象
        self.conn=pymongo.MongoClient("192.168.71.128",27017)
        #库对象
        self.db=self.conn["MaoDB"]
        #集合对象
        self.myset=self.db["film"]

        
    def getPage(self,url):
        req=urllib.request.Request(url,headers=self.headers)
        res=urllib.request.urlopen(req)
        html=res.read().decode("utf-8")
        self.parsePage(html)
        
    def parsePage(self,html):
        #创建编译对象
        p=re.compile(r'<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        rlist=p.findall(html)
        #rlist:[("","",""),()]
        self.writeToMongo(rlist)
        
    def writeToMongo(self,rlist):
        for r in rlist:
            d={"name":r[0].strip(),"star":r[1].strip(),"releasetime":r[2].strip()}
            self.myset.insert_one(d)
        print("成功存入MaoDB库")
    
    def workOn(self):
        while True:
            c=input("爬取y,退出q:")
            if c.strip().lower()=="y":
                url=self.baseurl+str(self.offset)
                self.getPage(url)
                self.offset+=10
            else:
                print("爬取结束")
                break
                

if __name__=="__main__":
    spider=MaoyanSpider()
    spider.workOn()
    
    
    
    
    
    
    
    
    
    
    
