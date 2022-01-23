import scrapy
from ..items import SpecswebsitesItem


class gsmSpider(scrapy.Spider):
    name = 'gsm'
    start_urls = [
        'ddd'
    ]

    def parse(self, response):
        pass
