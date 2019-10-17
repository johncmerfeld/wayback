from datetime import datetime as dt
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.db = MongoClient("mongodb://localhost:27017/")

    def get_database(self):
        return self.db

    def get_client(self, db_name):
        return self.db[db_name]

class WGBHCrawler(CrawlSpider):
    name = 'wgbhcrawler'

    custom_settings = {
        'DEPTH_LIMIT': 5
    }

    start_urls = ['https://www.wgbh.org/news/local-news']
    allowed_domains = ["wgbh.org"]

    db_client = MongoDB()

    rules = (
          Rule(LinkExtractor(allow = (), restrict_xpaths = ('//ul[@class="FourUp-Items-Item"]')),
          callback = "parse_items",
          follow = True),
    )

    def parse_items(self, response):
        items = []

        for paragraph in response.xpath('//div[@class="RichTextArticleBody-body"]/p'):
                try:
                    text = paragraph.xpath('text()').getall()
                    items.append(text)

                except:
                    pass

        # we'd probably want to add some information to this object, like the article title, author, etc.

        if len(items) > 0:
              db = self.db_client.get_client(self.db_name)
              collection = db[self.collection_name]
              timestamp = response.meta['wayback_machine_time'].timestamp()

              document = {'timestamp': timestamp, 'items': items}
              result = collection.insert_one(document)
