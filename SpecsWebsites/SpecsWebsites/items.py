# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpecswebsitesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()

    dimensions = scrapy.Field()
    diagonal = scrapy.Field()
    weight = scrapy.Field()
    build = scrapy.Field()
    SIM = scrapy.Field()

    displayType = scrapy.Field()  # Hz included in here
    size = scrapy.Field()  # contains diagonal also but also area
    resolution = scrapy.Field()

    OS = scrapy.Field()
    chipset = scrapy.Field()
    CPU = scrapy.Field()
    GPU = scrapy.Field()

    SDCard = scrapy.Field()  # have or not
    internalMemory = scrapy.Field()  # RAM included in here
    RAM = scrapy.Field()  # just add one more to specify RAM

    earphoneJack = scrapy.Field()  # have or not

    sensors = scrapy.Field()

    WLAN = scrapy.Field()
    bluetooth = scrapy.Field()
    NFC = scrapy.Field()
    USB = scrapy.Field()

    batteryType = scrapy.Field()
    batteryCapacity = scrapy.Field()
    batteryLife = scrapy.Field()

    sourceInfo = scrapy.Field()
    pass
