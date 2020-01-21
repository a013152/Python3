# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockSpider1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class StockItem(scrapy.Item):
    # define the fields for your item here like:
    names = scrapy.Field()
    sexes = scrapy.Field()
    codes = scrapy.Field()
    ages = scrapy.Field()
    leaders = scrapy.Field()
    pass