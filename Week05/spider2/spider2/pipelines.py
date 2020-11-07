# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter

import pymysql

class Spider2Pipeline:
    # def process_item(self, item, spider):
    #     return item
    pass

class mysqlPipeline(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='localhost',port=3306,user='root',password='',db = 'maoyan',charset='utf8mb4')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        try:
           self.cursor.execute('insert into douban values("%s","%s")'%(item["comment"],item["star"]))
           self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
