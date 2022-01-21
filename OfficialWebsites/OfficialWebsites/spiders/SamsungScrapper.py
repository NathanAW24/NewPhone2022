import scrapy
from ..items import OfficialwebsitesItem


class SamsungSpider(scrapy.Spider):
    name = 'samsung'
    start_urls = [
        'https://www.samsung.com/sg/smartphones/galaxy-s/'
    ]

    def parse(self, response):

        items = OfficialwebsitesItem()

        phones = response.css(
            'span.promotion-card-v2__sub-headline-text::text')
        print(phones)
