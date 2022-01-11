

import scrapy


class Lesson1(scrapy.Spider):
    name = "qo"
    start_urls = [
        "http://quotes.toscrape.com",
    ]
    custom_settings = {
        'FEED_FORMAT': "csv",
        'FEED_URI': "Hotels3.csv"
    }

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")

        for quote in quotes:
            yield {
                "Quote": quote.css('.text::text').get(),
                "Author": quote.css('.author::text').get(),
                "Tags": quote.css('.tag::text').getall(),
            }
            about = quote.css('.author + a::attr(href)').get()
            yield response.follow(about, callback=self.parse_author)

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        self.logger.info('get author page url')
        yield {
            'author_birthday': response.css('.author-born-date::text').get(),
            'author_bornlocation': response.css('.author-born-location::text').get(),
            'author_bio': response.css('.author-description::text').get(),
        }

        '''self.logger.info("Hello Scrapy Lesson1")
        hotels = response.xpath('//div[@class="i55ff1m dir dir-ltr"]').getall()
        for hotel in hotels:
            details = hotel.xpath('//span[@class="mvk3iwl dir dir-ltr"]').getall()
            yield {
                "Title": hotel.xpath('//div[@class="t1k09ieh dir dir-ltr"]/text()').get(),

            }
                            
                "Guests": hotels[0],
                "Num_of_rooms":details[1],
                "Num_of_beds":details[2],
                "Num_of_bathrooms":details[3],
                "bonus":list(details[4:])
                return response.follow('//a[@aria-label="Next"]')
                '''
