import scrapy
from ..items import OfficialwebsitesItem


class SonySpider(scrapy.Spider):
    name = 'sony'
    start_urls = [
        'https://www.sony.com.sg/electronics/phones/t/smartphones'
    ]

    def parse(self, response):
        items = OfficialwebsitesItem()

        names = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "product-model", " " ))]/text()')
        prices = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "price", " " ))]//strong/text()')

        names_ls = names.extract()
        prices_ls = prices.extract()

        for i in range(len(prices_ls)):
            price = prices_ls[i]
            name = names_ls[2*i]

            items['name'] = name
            items['price'] = price

            yield items
