# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FakenewsItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	news_thread = scrapy.Field()
	news_title = scrapy.Field()
	news_url = scrapy.Field()
	news_time = scrapy.Field()
	news_source = scrapy.Field()
	source_url = scrapy.Field()
	news_text = scrapy.Field()
	#pass
