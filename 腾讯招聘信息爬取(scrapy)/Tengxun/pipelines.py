# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .settings import *
import pymongo,pymysql

class TengxunPipeline(object):
    def process_item(self, item, spider):
        print("=============")
        print(item['zhName'])
        print(item['zhType'])
        print(item['zhNum'])
        print(item['zhAddress'])
        print(item['zhTime'])
        print(item['zhLink'])
        print(item['zhZhize'])
        print(item['zhYaoqiu'])
        print("=============")
        return item

class MongoPipeline(object):
    def __init__(self):
        #创建连接对象
        self.conn=pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
        #创建库对象
        self.db=self.conn[MONGODB_DB]
        #创建集合对象
        self.myset=self.db[MONGODB_SET]
    def process_item(self,item,spider):
        #把item转为字典数据类型,利用dict方法
        d=dict(item)
        self.myset.insert_one(d)
        #一定要返回item
        return item

class MysqlPipeline(object):
    def __init__(self):
        #创建数据库连接对象
        self.db=pymysql.connect(host=MYSQL_HOST,user=MYSQL_USER,password=MYSQL_PWD,database=MYSQL_DB,charset="utf8")
        #创建游标对象
        self.cursor=self.db.cursor()
    def process_item(self,item,spider):
        ins='insert into jobs values(%s,%s,%s,%s,%s,%s,%s,%s)'
        L=[item['zhName'].strip(),
           item['zhType'].strip(),
           int(item['zhNum'].strip()),
           item['zhAddress'].strip(),
           item['zhTime'].strip(),
           item['zhLink'].strip(),
           item['zhZhize'].strip(),
           item['zhYaoqiu'].strip(),
        ]
        self.cursor.execute(ins,L)
        #一定要提交到数据库执行
        self.db.commit()
        return item
    #process_item处理完成后会执行此方法
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print("MySQL数据库断开连接")
