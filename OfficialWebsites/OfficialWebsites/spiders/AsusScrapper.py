import scrapy
from ..items import OfficialwebsitesItem
import time


class AsusSpider(scrapy.Spider):
    name = 'asus'
    start_urls = [
        'https://sg.store.asus.com/phone.html'
    ]

    def parse(self, response):
        items = OfficialwebsitesItem()

        # names = response.xpath(
        #     "//strong[@class='product name product-item-name']")
        # print(names)

        # prices = response.css('span.price::text')

        names = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "product-item-link", " " ))]/text()')

        prices = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "price-wrapper", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "price", " " ))]/text()')

        # print(len(prices), prices.extract())
        # print(len(names), names.extract())

        names_ls = names.extract()
        prices_ls = prices.extract()

        for i in range(8):
            name = names_ls[i].strip()
            price = prices_ls[2*i]
            items['price'] = price
            items['name'] = name
            yield items

        # for b in range(len(prices)):
        #     # name = a.extract().strip()  # lstrip().rstrip()
        #     price = prices[b].extract()
        #     # items['name'] = name
        #     items['price'] = price
        #     b += 2
        #     yield items

        # for phone in names:
        #     name = phone.css("a.product-item-link::text").extract()[0].strip()
        #     items['name'] = name

        # for phone in prices:
        #     price = phone.extract()
        #     items['price'] = price
