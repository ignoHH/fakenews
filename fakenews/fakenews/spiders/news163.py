# -*- coding: utf-8 -*-
import scrapy
from fakenews.items import FakenewsItem
from scrapy.linkextractors import LinkExtractor#链接提取器
from scrapy.spiders import CrawlSpider,Rule
#scrapy genspider news163 news.163.com ---genarate spider
class News163Spider(CrawlSpider):#类继承
	name = 'xinhuanet'
	allowed_domains = ['www.xinhuanet.com']
	#could add url that we want to spider
	start_urls = ['http://www.xinhuanet.com']
	#<a id="ne_article_source"></a>source url
	rules = (
		Rule(LinkExtractor(allow=r"/food/*"),#Regular expression检验字符串
			callback="parse_fakenews",
			follow=True),#是否继续
		)
	#callback 
	def parse_fakenews(self,response):
		item = FakenewsItem()
		item['news_thread'] = response.url.strip().split('/')[-1][:-5]
		#delete blank
		self.get_title(response,item)
		self.get_time(response,item)
		self.get_source(response,item)
		self.get_url(response,item)
		self.get_source_url(response,item)
		self.get_text(response,item)
		return item

	def get_title(self,response,item):
		title = response.css('title::text').extract()
		print('*'*20)
		if title:#list is not empty
			print('title:{}'.format(title[0][:-5]))
			item['news_title'] = title[0][:-5]

	def get_time(self,response,item):
		time = response.css('.h-time::text').extract()
		if time:
			print('time:{}'.format(time[0][:-5]))
			item['news_time'] = time[0][:-5]

	def get_source(self,response,item):
		source = response.css('#source::text').extract()
		if source:
			print('source:{}'.format(source[0]))
			item['news_source'] = source[0]

	def get_source_url(self,response,item):
		source_url = response.css('#ne_article_source::attr(href)').extract()
		if source_url:
			print('source_url:{}'.format(source_url[0]))
			item['source_url'] = source_url[0]

	def get_text(self,response,item):
		text = response.css('#endText p::text').extract()
		if text:
			print('text:{}'.format(text[0]))
			item['news_text'] = text

	def get_url(self,response,item):
		url = response.url
		if url:
			print('url:{}'.format(url))
			item['news_url'] = url
	#def parse(self, response):
	#	pass
