# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class Spider1Pipeline:
    # def process_item(self, item, spider):
    #     dymc = item['dymc']
    #     dylx = item['dylx']
    #     dysj = item['dysj']
    #     output = f'|{dymc}|\t|{dylx}|\t|{dysj}|\n\n'
    #     with open('./movies.csv', 'a+', encoding='utf_8_sig') as article:
    #         article.write(output)
    #     return item
    pass

class mysqlPipeline(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='localhost',port=3306,user='root',password='',db = 'maoyan',charset='utf8mb4')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
           self.cursor.execute('insert into maoyan values("%s","%s","%s")'%(item["dymc"],item["dylx"],item["dysj"]))
           self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()








