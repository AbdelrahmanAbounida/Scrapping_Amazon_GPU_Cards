import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['Spider3']
    start_urls = ['http://Spider3/']

    def parse(self, response):
        pass
