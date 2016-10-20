# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PubmedItem(scrapy.Item):
    pmid = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    origin = scrapy.Field()
    date = scrapy.Field()
    abstract = scrapy.Field()
