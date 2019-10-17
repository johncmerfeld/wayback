from datetime import datetime as dt
import scrapy

class WGBHSpider(scrapy.Spider):
    name = 'wgbh'

    def start_requests(self):
        yield scrapy.Request('https://www.wgbh.org/news/local-news')

    def parse(self, response):
        items = []
        for trend in response.xpath('//div[@id="trending_bar_items"]/a[@class="trending_bar_item | color_black float_left"]'):
            try:
                topic = trend.xpath('text()').getall()
                link = trend.xpath('@href').extract()
                items.append({'topic': topic, 'link': link})
            except:
                pass

        if len(items) > 0:
            timestamp = response.meta['wayback_machine_time'].timestamp()
            return {'timestamp': timestamp, 'items': items}