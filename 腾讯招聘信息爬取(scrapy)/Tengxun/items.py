# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunItem(scrapy.Item):
    # define the fields for your item here like:
    #职位名称
    zhName = scrapy.Field()
    # 职位类别
    zhType = scrapy.Field()
    #招聘人数
    zhNum = scrapy.Field()
    #工作地点
    zhAddress = scrapy.Field()
    #发布时间
    zhTime = scrapy.Field()
    #详情链接
    zhLink = scrapy.Field()
    #工作职责
    zhZhize=scrapy.Field()
    #工作要求
    zhYaoqiu=scrapy.Field()


