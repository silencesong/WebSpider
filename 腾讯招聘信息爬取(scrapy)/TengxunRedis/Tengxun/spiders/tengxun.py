# -*- coding: utf-8 -*-
import scrapy
from Tengxun.items import TengxunItem
from scrapy_redis.spiders import RedisSpider

class TengxunSpider(RedisSpider):
    name = 'tengxun'
    allowed_domains = ['hr.tencent.com']
    #定义rediskey
    redis_key="tengxunspider:start_urls"

    def parse(self, response):
        main_url = 'https://hr.tencent.com/position.php?start='
        for i in range(0, 1001, 10):
            url = main_url + str(i)
            yield scrapy.Request(url, callback=self.parseHtml)

    def parseHtml(self, response):
        item=TengxunItem()
        baseList=response.xpath('// tr[@class ="even"] | // tr[@ class ="odd"]')
        for r in baseList:
            item['pname']=r.xpath('./td[1]/a/text()').extract()[0]
            item['pclass']=r.xpath('./td[2]/text()').extract()
            if item['pclass']:
                item['pclass']=item['pclass'][0]
            else:
                item['pclass']="无"
            item['pnum']=r.xpath('./td[3]/text()').extract()[0]
            item['padress'] = r.xpath('./td[4]/text()').extract()[0]
            item['ptime'] = r.xpath('./td[5]/text()').extract()[0]
            item['plink']=r.xpath('./td[1]/a/@href').extract()[0]
            url='https://hr.tencent.com/'+item['plink']
            yield scrapy.Request(url,callback=self.parseHtml2,meta={"item":item})

    def parseHtml2(self,response):
        item=response.meta["item"]
        rList=response.xpath(r'//ul[@class="squareli"]')
        item["pres"]=''.join(rList[0].xpath('./li/text()').extract())
        item["preq"]=''.join(rList[1].xpath('./li/text()').extract())
        yield item



