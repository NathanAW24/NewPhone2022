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

        # this one just for parent directory
        specTable = response.xpath('//td[@class="nfo"]')
        # print(specTable.extract())

        # this one for another parent directory
        specHeading = response.css('.accent span')
        print(specHeading.extract())

        # dimensions field
        dimensions = specTable.css('[data-spec="dimensions"]::text')
        print(len(dimensions), dimensions.extract())
        # diagonal field
        diagonal = specHeading.css('[data-spec="displaysize-hl"]::text')
        print(diagonal.extract())
        # weight field
        weight = specTable.css('[data-spec="weight"]::text')
        print(weight.extract())
        # build field
        build = specTable.css('[data-spec="build"]::text')
        print(build.extract())
        # SIM field
        SIM = specTable.css('[data-spec="sim"]::text')
        print(SIM.extract())

        # displayType field
        displayType = specTable.css('[data-spec="displaytype"]::text')
        print(displayType.extract())
        # size field
        size = specTable.css('[data-spec="displaysize"]::text')
        print(size.extract())
        # resolution field
        resolution = specTable.css('[data-spec="displayresolution"]::text')
        print(resolution.extract())

        # OS field
        OS = specTable.css('[data-spec="os"]::text')
        print(OS.extract())

        # chipset field
        chipset = specTable.css('[data-spec="chipset"]::text')
        print(chipset.extract())
        # CPU field
        CPU = specTable.css('[data-spec="cpu"]::text')
        print(CPU.extract())
        # GPU field
        GPU = specTable.css('[data-spec="gpu"]::text')
        print(GPU.extract())

        # SDCard field
        SDCard = specTable.css('[data-spec="memoryslot"]::text')
        print(SDCard.extract())
        # internalMemory field
        internalMemory = specTable.css('[data-spec="internalmemory"]::text')
        print(internalMemory.extract())
        # RAM field
        RAM = specHeading.css('[data-spec="ramsize-hl"]::text')
        print(RAM.extract())

        # earphoneJack field
        earphoneJack = response.xpath(
            '//table[(((count(preceding-sibling::*) + 1) = 12) and parent::*)]//tr[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "nfo", " " ))]/text()')
        print(earphoneJack.extract())

        # sensors field
        sensors = specTable.css('[data-spec="sensors"]::text')
        print(sensors.extract())

        # WLAN field
        WLAN = specTable.css('[data-spec="wlan"]::text')
        print(WLAN.extract())
        # bluetooh field
        bluetooh = specTable.css('[data-spec="bluetooth"]::text')
        print(bluetooh.extract())
        # NFC field
        NFC = specTable.css('[data-spec="nfc"]::text')
        print(NFC.extract())
        # USB field
        USB = specTable.css('[data-spec="usb"]::text')
        print(USB.extract())

        # batteryType field
        batteryType = specTable.css('[data-spec="batdescription1"]::text')
        print(batteryType.extract())
        # batteryCapacity field
        batteryCapacity = specHeading.css('[data-spec="batsize-hl"]::text')
        print(batteryCapacity.extract())
        # batteryLife field
        batteryLife = specTable.css(
            '[onclick="showBatteryPopup(event, 11102); "]::text')
        print(batteryLife.extract())
