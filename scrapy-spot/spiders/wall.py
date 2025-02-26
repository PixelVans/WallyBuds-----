import scrapy
from basic_scrapy_spider.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'wallbuds'
    allowed_domains = ['']
    start_urls = ['']

    def parse(self, response):
        pass
