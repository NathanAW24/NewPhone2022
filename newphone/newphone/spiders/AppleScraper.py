import scrapy


class AppleSpider(scrapy.Spider):
    name = 'apple'
    start_urls = [
        'link1',
        'link2'
    ]

    def parse(self, response):
        pass
