from datetime import datetime as dt
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from pymongo import MongoClient

class MongoDB:
    """
    we need to create a single persistent connection to database.

    Everytime a client calls us, we can simply return the connection instead of creating
    it again and again.
    """
    def __init__(self):
        self.db = MongoClient("mongodb://localhost:27017/")

    def get_database(self):
        return self.db

    def get_client(self, db_name):
        return self.db[db_name]

class GlobeSpiderCrawler(CrawlSpider):
    name = 'globecrawler'

    db_client = MongoDB()

    allowed_domains = ["bostonglobe.com"]
    start_urls = ['https://www.bostonglobe.com/metro']

    custom_settings = {
        'DEPTH_LIMIT': 5
    }
    rules = (
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//div[@class="story"]')),
        callback = "parse_items",
        follow = True),
    )

    def parse_items(self, response):
        items = []

        for paragraph in response.xpath('//div[@class="article-text"]/p'):
            try:
                text = paragraph.xpath('text()').getall()
                items.append(text)
            except:
                pass
            
            

        if len(items) > 0:
            #db = self.db_client.get_client('globe_stories_db')
            db = self.db_client.get_client(self.db_name)
            #collection = db['globe_stories_collection']
            collection = db[self.collection_name]
            timestamp = response.meta['wayback_machine_time'].timestamp()
            document = {'timestamp': timestamp, 'items': items}
            result = collection.insert_one(document)
            return document
