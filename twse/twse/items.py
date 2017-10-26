# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    tradeTotalShare = scrapy.Field()
    tradeTotalCount = scrapy.Field()
    tradeTotalPrice = scrapy.Field()
    openPrice = scrapy.Field()
    heightPrice = scrapy.Field()
    lowPrice = scrapy.Field()
    closePrice = scrapy.Field()
    benefitRatio = scrapy.Field()
    pass
