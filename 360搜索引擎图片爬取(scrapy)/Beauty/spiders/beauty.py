# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import json
from Beauty.items import BeautyItem

class BeautySpider(scrapy.Spider):
    name = 'beauty'
    allowed_domains = ['image.so.com']
    #把start_urls去掉，重写start_requests()方法,自己指定要爬取的起始的url地址
    def start_requests(self):
        baseurl='http://image.so.com/zj?'
        for pg in range(0,61,30):
            params={
            'ch':'beauty',
            'sn':str(pg),
            'listtype': 'new',
            'temp': '1'
            }
            #给params编码
            params=urlencode(params)
            fullurl=baseurl+params
            yield scrapy.Request(fullurl,callback=self.parse)

    def parse(self, response):
        item=BeautyItem()
        #response.text是json格式字符串->字典
        imgList=json.loads(response.text)['list']
        #imgList:[{美女1},{},]
        for img in imgList:
            item['imgUrl']=img['qhimg_url']
            yield item

