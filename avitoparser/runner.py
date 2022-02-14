from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from avitoparser.spiders.avitoru import AvitoruSpider
from avitoparser.spiders.leroymerlinru import LeroymerlinruSpider
from avitoparser import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    # process.crawl(AvitoruSpider, search='гитары')
    process.crawl(LeroymerlinruSpider, search='электроинструменты')

    process.start()
