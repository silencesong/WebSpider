import urllib.request
import re
import pymysql
import warnings

class MaoyanSpider:
    def __init__(self):
        self.baseurl="https://maoyan.com/board/4?offset="
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
        self.offset=0
        #创建数据库连接对象
        self.db=pymysql.connect("192.168.71.128","lion","123456","spiderdb",charset="utf8")
        #创建游标对象
        self.cursor=self.db.cursor()
        
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
        self.writeToMysql(rlist)
    
    #保存数据
    def writeToMysql(self,rlist):
        #忽略下面语句的所有警告
        warnings.filterwarnings("ignore")
        ins='insert into film(name,star,releasetime) values(%s,%s,%s)'
        for r in rlist:       
            L=[r[0].strip(),
               r[1].strip(),
               r[2].strip()[5:15]]
            #excute必须使用列表传参
            self.cursor.execute(ins,L)
            #提交到数据库执行
            self.db.commit()

    #主函数
    def workOn(self):
        while True:
            c=input("爬取y,退出q:")
            if c.strip().lower()=="y":
                url=self.baseurl+str(self.offset)
                self.getPage(url)
                self.offset+=10
            else:
                print("爬取结束")
                #必须等所有爬完之后再关闭
                self.cursor.close()
                self.db.close()
                break
                

if __name__=="__main__":
    spider=MaoyanSpider()
    spider.workOn()
    
    
    
    
    
    
    
    
    
    
    
