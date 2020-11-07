# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spider2.items import Spider2Item

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/subject/26754233/comments?sort=new_score&status=P']

    def parse(self, response):
        #pass
        movie_list = Selector(response=response).xpath('//div[@class="comment-item "]')              #定位到具体短评
        print(movie_list)
        for movie in movie_list[:20]:
            comment1 = movie.xpath('./div[2]/p/span/text()').extract()                   #取短评内容
            star1 = movie.xpath('./div[2]/h3/span[2]/span[2]/@class').extract()                  #取短评评分
            #print(star1)
            comment1=str(comment1)
            comment = comment1.replace('[','').replace(']','').replace("'","").replace("'","")
            if star1[0] == "allstar50 rating":
               star = 5
            elif star1[0] == "allstar40 rating":
                star = 4
            elif star1[0] == "allstar30 rating":
                star = 3
            elif star1[0] == "allstar20 rating":
                star = 2
            elif star1[0] == "allstar10 rating":
                star = 1
            else:
                star = 0
            print(star)
            print(comment)

            item = Spider2Item()
            item['comment'] = comment
            item['star'] = star

            yield item
