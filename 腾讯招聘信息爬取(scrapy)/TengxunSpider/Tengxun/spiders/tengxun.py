# -*- coding: utf-8 -*-
import scrapy
from Tengxun.items import TengxunItem

class TengxunSpider(scrapy.Spider):
    name = "tengxun"
    allowed_domains = ["hr.tencent.com"]
    url='https://hr.tencent.com/position.php?start='
    start_urls = [url+str(0)]

    def parse(self, response):
        #把284页的url地址都给调度器入队列
        for i in range(0,431,10):
            url=self.url+str(i)
            #scrapy.Request()
            yield scrapy.Request(url,callback=self.parseHtml)

    def parseHtml(self,response):
        #创建item对象
        item=TengxunItem()
        #每个职位节点对象列表
        baseList=response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for base in baseList:
            item['zhName']=base.xpath('./td[1]/a/text()').extract()[0]
            item['zhType']=base.xpath('./td[2]/text()').extract()
            if item['zhType']:
                item['zhType']=item['zhType'][0]
            else:
                item['zhType']="无"
            item['zhNum']=base.xpath('./td[3]/text()').extract()[0]
            item['zhAddress']=base.xpath('./td[4]/text()').extract()[0]
            item['zhTime']=base.xpath('./td[5]/text()').extract()[0]
            item['zhLink']=base.xpath('./td[1]/a/@href').extract()[0]
            #拼接完整的职位链接
            url='https://hr.tencent.com/'+item['zhLink']
            yield scrapy.Request(url,callback=self.parseJob,meta={'item':item})

    def parseJob(self,response):
        #item为上个函数传递过来的item
        item=response.meta['item']
        #基准xpath,匹配出职责和要求两个对象
        baseList=response.xpath('//ul[@class="squareli"]')
        #岗位职责提取，拼接成字符串
        item['zhZhize']="".join(baseList[0].xpath('.//li/text()').extract())
        # 岗位要求提取，拼接成字符串
        item['zhYaoqiu'] = "".join(baseList[1].xpath('.//li/text()').extract())
        yield item


