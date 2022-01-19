import scrapy


class SamsungSpider(scrapy.Spider):
    name = 'samsung'
    start_urls = [
        'link1',
        'link2'
    ]

    def parse(self, response):
        pass
