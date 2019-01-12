# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Tengxun.items import TengxunItem


class TengxuncrawlSpider(CrawlSpider):
    name = 'tengxuncrawl'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = TengxunItem()
        baseList = response.xpath('// tr[@class ="even"] | // tr[@ class ="odd"]')
        for r in baseList:
            item['pname'] = r.xpath('./td[1]/a/text()').extract()[0]
            item['pclass'] = r.xpath('./td[2]/text()').extract()
            if item['pclass']:
                item['pclass'] = item['pclass'][0]
            else:
                item['pclass'] = "无"
            item['pnum'] = r.xpath('./td[3]/text()').extract()[0]
            item['padress'] = r.xpath('./td[4]/text()').extract()[0]
            item['ptime'] = r.xpath('./td[5]/text()').extract()[0]
            item['plink'] = r.xpath('./td[1]/a/@href').extract()[0]
            url = 'https://hr.tencent.com/' + item['plink']
            yield scrapy.Request(url,callback=self.parse_html,meta={'item':item})

    def parse_html(self,response):
        item = response.meta["item"]
        rList = response.xpath(r'//ul[@class="squareli"]')
        item["pres"] = ''.join(rList[0].xpath('./li/text()').extract())
        item["preq"] = ''.join(rList[1].xpath('./li/text()').extract())
        yield item
