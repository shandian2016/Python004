# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class SpidersPipeline:
    def process_item(self, item, spider):
        dymc = item['dymc']
        dylx = item['dylx']
        dysj = item['dysj']
        output = f'{dymc},{dylx},{dysj}\n'
        with open('./movies.csv','a+',encoding='utf_8_sig') as article:
            article.write(output)
        return item
    # pass
