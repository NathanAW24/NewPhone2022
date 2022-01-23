import scrapy
from ..items import SpecswebsitesItem


class gsmSpider(scrapy.Spider):
    name = 'gsm'
    start_urls = [
        'https://www.gsmarena.com/apple_iphone_13_pro-11102.php'
    ]

    def parse(self, response):
        items = SpecswebsitesItem()

        name = response.css('.specs-phone-name-title::text')
        print(name.extract())

        # this one just for parent direct
        # print(specTable.extract())
        # specTable = response.xpath('//td[@class="nfo"]')

        # dimensions field
        # dimensions = specTable.css('[data-spec="dimensions"]::text')
        # print(len(dimensions), dimensions.extract())
        # diagonal field
        # diagonal = response.css(
        #     '//*[contains(concat( " ", @class, " " ), concat( " ", "help-display", " " ))]//span/text()')
        # print(diagonal.extract())
