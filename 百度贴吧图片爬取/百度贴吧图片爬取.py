import requests
from lxml import etree

class BaiduImgSpider:
    def __init__(self):
        self.baseurl="http://tieba.baidu.com"
        self.mainurl="http://tieba.baidu.com/f?"
        self.headers={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
    
    #获取所有帖子的url列表
    def getPageUrl(self,params):
        res=requests.get(self.mainurl,params=params,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        #提取页面中url
        parseHtml=etree.HTML(html)
        tlist=parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        print(tlist)
        for t in tlist:
            tlink=self.baseurl+t
            self.getImgUrl(tlink)
            
    #获取1个帖子中所有图片的url列表
    def getImgUrl(self,tlink):
        #获取1个帖子的响应内容
        res=requests.get(tlink,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        #从帖子的html提取图片的src
        parseHtml=etree.HTML(html)
        imgList=parseHtml.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src')
        #print(imgList)
        #依次遍历图片链接调用写入函数
        for img in imgList:
            self.writeImage(img)
    
    #把图片保存到本地
    def writeImage(self,img):
        #对图片链接发请求，获取res.content
        res=requests.get(img,headers=self.headers)
        res.encoding="utf-8"
        html=res.content
        filename=img[-12:]
        with open(filename,"wb") as f:
            f.write(html)
            print("%s下载成功"%filename)
    
    #主函数
    def workOn(self):
        name=input("请输入贴吧名:")
        begin=int(input("请输入起始页:"))
        end=int(input("请输入终止页:"))
        for n in range(begin,end+1):
            pn=(n-1)*50
            params={
                    "kw":name,
                    "pn":pn
                    }
            self.getPageUrl(params)

if __name__=="__main__":
    spider=BaiduImgSpider()
    spider.workOn()