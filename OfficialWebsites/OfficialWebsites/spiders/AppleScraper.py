# from pydantic import PathNotExistsError
import scrapy
from ..items import OfficialwebsitesItem


class AppleSpider(scrapy.Spider):
    name = 'apple'
    start_urls = [
        'https://www.apple.com/sg/shop/buy-iphone'
    ]

    def parse(self, response):

        items = OfficialwebsitesItem()

        phones = response.css(
            'div.rf-hcard-copy')

        for phone in phones:
            name = phone.css(
                'div.rf-hcard-content-title::text').extract()[0].strip()
            price = phone.css('span.nowrap::text').extract()
            # print(name, price)

            items['name'] = name
            items['price'] = price

            yield items  # type 'scrapy crawl apple -o appleRaw.csv -t csv' in terminal to save it as csv
