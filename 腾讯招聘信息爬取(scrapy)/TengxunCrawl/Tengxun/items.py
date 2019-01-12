# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunItem(scrapy.Item):
    # define the fields for your item here like:
    pname=scrapy.Field()
    pclass=scrapy.Field()
    pnum=scrapy.Field()
    padress=scrapy.Field()
    ptime=scrapy.Field()
    plink=scrapy.Field()
    pres=scrapy.Field()
    preq=scrapy.Field()

