# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from lxml.html.clean import unicode

from scrapy.loader import ItemLoader
from itemloaders.processors import Join,Compose,MapCompose,TakeFirst

def remove_currency(x):
    x.replace('€','')
    return x


class LearnItem(scrapy.Item):
    # Primary fields
    title = scrapy.Field()

    '''  
    details = scrapy.Field(output_processor= MapCompose(Join))
    price = scrapy.Field(input_processor=MapCompose(remove_currency),output_processor= unicode.strip)
    rate = scrapy.Field()
    
    
    Location = scrapy.Field()
    Bedrooms = scrapy.Field()
    Beds = scrapy.Field()
    Bathrooms = scrapy.Field()
    Extra = scrapy.Field()
    Price = scrapy.Field()

    #calculated Fields
    Image = scrapy.Field()
    Rate = scrapy.Field()
    RareFind = scrapy.Field()

    # Housekeeping fields
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()
    '''
    pass



