import scrapy


class AvitoruSpider(scrapy.Spider):
    name = 'avitoru'
    allowed_domains = ['avito.ru']
    start_urls = ['http://avito.ru/']

    def parse(self, response):
        pass
