# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .settings import *
import pymongo
import pymysql

class TengxunPipeline(object):
    def process_item(self, item, spider):
        print("====================")
        print(item['pname'])
        print(item['pclass'])
        print(item['pnum'])
        print(item['padress'])
        print(item['ptime'])
        print(item['plink'])
        print(item['preq'])
        print(item['pres'])
        return item

class TengxunMongoPipeline(object):
    def __init__(self):
        self.conn=pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
        self.db=self.conn[MONGODB_DB]
        self.myset=self.db[MONGODB_SET]

    def process_item(self, item, spider):
        d=dict(item)
        self.myset.insert_one(d)
        return item

class TengxunMysqlPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host=MYSQL_HOST,user=MYSQL_USER,password=MYSQL_PWD,database=MYSQL_DB,charset="utf8")
        self.cursor=self.db.cursor()

    def process_item(self, item, spider):
        ins="insert into tx values (%s,%s,%s,%s,%s,%s,%s,%s)"
        L=[
            item['pname'].strip(),
            item['pclass'].strip(),
            int(item['pnum'].strip()),
            item['padress'].strip(),
            item['ptime'].strip(),
            item['plink'].strip(),
            item['preq'].strip(),
            item['pres'].strip()
        ]
        self.cursor.execute(ins,L)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print("over")
