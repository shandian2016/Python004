import scrapy
from scrapy.selector import Selector
from spider1.items import Spider1Item

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        #pass
        movie_list = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        print(movie_list)
        i = 0
        for movie in movie_list:

            dymc = movie.xpath('./div[1]/span/text()').extract_first()
            dylx = movie.xpath('./div[2]//text()').extract()[2].strip()
            dysj = movie.xpath('./div[4]//text()').extract()[2].strip()
            item = Spider1Item()
            item['dymc'] = dymc
            item['dylx'] = dylx
            item['dysj'] = dysj
            print(item)
            i += 1
            if i == 11:
                break
            yield item
