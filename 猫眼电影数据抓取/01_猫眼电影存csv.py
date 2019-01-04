import urllib.request
import re
import csv

class MaoyanSpider:
    def __init__(self):
        self.baseurl="https://maoyan.com/board/4?offset="
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
        self.offset=0
        
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
        self.writeToCSV(rlist)
        
    def writeToCSV(self,rlist):
        for r in rlist:
            #r=list(r)
            r=[r[0].strip(),r[1].strip(),r[2].strip()]
            with open("猫眼.csv","a",newline="",encoding="gb18030") as f:
                #创建写入对象
                writer=csv.writer(f)
                #调用witerow()方法
                writer.writerow(r)
    
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
    
    
    
    
    
    
    
    
    
    
    
