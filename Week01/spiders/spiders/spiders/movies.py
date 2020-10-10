import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']

    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        # movie_list = response.xpath('//div[@class="movie-hover-info"]')
        # print(movie_list)
        movie_list = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        #print(movie_list)
        i = 0
        for movie in movie_list:
            #i = 0
            dymc = movie.xpath('./div[1]/span/text()').extract_first()
            dylx = movie.xpath('./div[2]//text()').extract()[2].strip()
            dysj = movie.xpath('./div[4]//text()').extract()[2].strip()
            item = SpidersItem()
            item['dymc'] = dymc
            item['dylx'] = dylx
            item['dysj'] = dysj
            i += 1
            if i == 11:
                break
            yield item








