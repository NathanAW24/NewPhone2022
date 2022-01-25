from re import L
from numpy import NaN, disp, extract
from pygame import display
import scrapy
from ..items import SpecswebsitesItem


class gsmSpider(scrapy.Spider):
    name = 'gsm'
    start_urls = [
        'https://www.gsmarena.com/apple_iphone_13_pro-11102.php',
        'https://www.gsmarena.com/apple_iphone_13-11103.php',
        'https://www.gsmarena.com/apple_iphone_12-10509.php',
        'https://www.gsmarena.com/apple_iphone_se_(2020)-10170.php',
        'https://www.gsmarena.com/apple_iphone_11-9848.php',
        'https://www.gsmarena.com/asus_zenfone_8-10893.php',
        'https://www.gsmarena.com/asus_rog_phone_5s-11054.php',
        'https://www.gsmarena.com/asus_rog_phone_5s_pro-11053.php',
        'https://www.gsmarena.com/sony_xperia_pro_i-11174.php',
        'https://www.gsmarena.com/sony_xperia_1_iii-10712.php',
        'https://www.gsmarena.com/sony_xperia_5_iii-10851.php',
        'https://www.gsmarena.com/sony_xperia_10_iii-10698.php',
        'https://www.gsmarena.com/sony_xperia_5_ii-10396.php',
        'https://www.gsmarena.com/sony_xperia_1_ii-10096.php',
        'https://www.gsmarena.com/sony_xperia_10_ii-10095.php'
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
        # print(specHeading.extract())

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

        # format into a kind of dictionary
        items['name'] = name.extract()[0] if (
            len(name.extract()) > 0) else NaN

        items['dimensions'] = dimensions.extract()[0] if (
            len(dimensions.extract()) > 0) else NaN
        items['diagonal'] = diagonal.extract()[0] if len(
            diagonal.extract()) > 0 else NaN
        items['weight'] = weight.extract()[0] if len(
            weight.extract()) > 0 else NaN
        items['build'] = build.extract()[0] if len(
            build.extract()) > 0 else NaN
        items['SIM'] = SIM.extract()[0] if len(SIM.extract()) > 0 else NaN

        items['displayType'] = displayType.extract()[0] if len(
            displayType.extract()) > 0 else NaN
        items['size'] = size.extract()[0] if len(
            size.extract()) > 0 else NaN
        items['resolution'] = resolution.extract()[0] if len(
            resolution.extract()) > 0 else NaN

        items['OS'] = OS.extract()[0] if len(OS.extract()) > 0 else NaN
        items['chipset'] = chipset.extract()[0] if len(
            chipset.extract()) > 0 else NaN
        items['CPU'] = CPU.extract()[0] if len(CPU.extract()) > 0 else NaN
        items['GPU'] = GPU.extract()[0] if len(GPU.extract()) > 0 else NaN

        items['SDCard'] = SDCard.extract()[0] if len(
            SDCard.extract()) > 0 else NaN
        items['internalMemory'] = internalMemory.extract()[0] if len(
            internalMemory.extract()) > 0 else NaN
        items['RAM'] = RAM.extract()[0] + 'GB' if len(RAM.extract()) > 0 else NaN

        items['earphoneJack'] = earphoneJack.extract()[0] if len(
            earphoneJack.extract()) > 0 else NaN

        items['sensors'] = sensors.extract()[0] if len(
            sensors.extract()) else NaN

        items['WLAN'] = WLAN.extract()[0] if len(
            WLAN.extract()) > 0 else NaN
        items['bluetooth'] = bluetooh.extract()[0] if len(
            bluetooh.extract()) > 0 else NaN
        items['NFC'] = NFC.extract()[0] if len(NFC.extract()) > 0 else NaN
        items['USB'] = USB.extract()[0] if len(USB.extract()) > 0 else NaN

        items['batteryType'] = batteryType.extract()[0] if len(
            batteryType.extract()) > 0 else NaN
        items['batteryCapacity'] = batteryCapacity.extract(
        )[0] + 'mAH' if len(batteryCapacity.extract()) > 0 else NaN
        items['batteryLife'] = batteryLife.extract()[0] if len(
            batteryLife.extract()) > 0 else NaN

        items['sourceInfo'] = 'gsmarena'

        yield items

    def itemsError(self):
        pass
