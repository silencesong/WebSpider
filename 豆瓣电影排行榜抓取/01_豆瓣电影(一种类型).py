import requests
import json
import pymysql

class DoubanSpider:
    def __init__(self):
        self.url="https://movie.douban.com/j/chart/top_list?"
        self.headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        self.db=pymysql.connect("192.168.71.128","lion","123456","spiderdb",charset="utf8")
        self.cursor=self.db.cursor()
        
    def getPage(self,params):
        res=requests.get(self.url,params=params,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        #html为[{一个电影信息},{}...]
        self.parsePage(html)
    
    def parsePage(self,html):
        ins='insert into movie values(%s,%s)'
        rList=json.loads(html)
        for rDict in rList:
            name=rDict["title"]
            score=rDict["score"]
            L=[name.strip(),float(score.strip())]
            self.cursor.execute(ins,L)
            self.db.commit()
    
    def workOn(self):
        num=input("请输入要爬取的数量：")
        params={
            "type":"11",
            "interval_id":"100:90",
            "action":"",
            "start":"0",
            "limit":num,
            }
        self.getPage(params)
        

if __name__=="__main__":
    spider=DoubanSpider()
    spider.workOn()


