# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline


class AvitoparserPipeline:
    def process_item(self, item, spider):
        print()
        return item


class AvitoImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        item['photos'] = [itm[1] for itm in results if itm[0]]
        return item

    # def file_path(self, request, response=None, info=None, *, item=None):
    #     return ''


class LeroymerlinPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.lm

    def process_item(self, item, spider):
        collection = self.mongobase['goods']
        collection.insert_one(dict(item))
        return item


class LeroymerlinImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        print(results)
        item['photos'] = [itm[1] for itm in results if itm[0]]
        print(item['photos'])
        return item
