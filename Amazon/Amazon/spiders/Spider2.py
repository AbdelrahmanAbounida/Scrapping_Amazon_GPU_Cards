import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import Request

from ..items import LearnItem


class Hotels(scrapy.Spider):
    name = "cards"
    start_urls = [
        "https://www.amazon.de/-/en/s?k=Graphics+Cards&i=computers&rh=n%3A430161031&language=en&_encoding=UTF8&c=ts&qid=1641291203&ts_id=430161031&ref=sr_pg_1"]
    custom_settings = {
        'FEED_FORMAT': "json",
        'FEED_URI': "cards.json",

    }

    # contract , multiple pages #
    # from scrapy.http import Request
    def parse(self, response):

        """ This function parses a property page.
         @url https://www.amazon.de/-/en/Graphics-Cards/b?ie=UTF8&node=430161031
         @returns items
         @scrapes title price description address image_urls
         """
        titles = response.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()').getall()
        prices = response.xpath('//span[@class="a-price-whole"]/text()').getall()
        cardDetails = response.xpath('//div[@class="sg-col sg-col-4-of-12 sg-col-4-of-16 sg-col-8-of-20"]/div/div/div')
        images = response.xpath('//img[@class="s-image"]/@src')

        for title in titles:
            # items['title'] = t.strip()
            yield {
                'Title': title.strip()
            }

        for price in prices:
            yield {
                'Price': price
            }

        for detail in cardDetails:
            yield {
                'Ram Size': detail.xpath('.//div[1]/div/span[@class="a-text-bold"]/text()').get(),
                'RAM Type': detail.xpath('.//div[2]/div/span[@class="a-text-bold"]/text()').get(),
                'Graphics Card': detail.xpath('.//div[3]/div/span[@class="a-text-bold"]/text()').get(),
                'Memory Clock Speed': detail.xpath('.//div[4]/div/span[@class="a-text-bold"]/text()').get(),
            }

        for image in images:
            yield {
                'Image': image.get()
            }

        next = response.xpath('//li[@class="a-last"]/a/@href').get()
        if next is not None:
            yield response.follow(next, callback=self.parse)
