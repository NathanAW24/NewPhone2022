# SpecsWebsites

## Overview
This repository helds the scrapy spider for scraping the website <a href='https://www.gsmarena.com/'>gsmarena</a> to get the detailed specifications for the available phones. In the <a href=https://github.com/NathanAW24/NewPhone2022/tree/main/SpecsWebsites/SpecsWebsites/spiders>spiders</a> folder there is one scraper which scrapes from <a href='https://www.gsmarena.com/'>gsmarena</a> directly.

Go back from there one directory there is an <a href='https://github.com/NathanAW24/NewPhone2022/tree/main/SpecsWebsites/SpecsWebsites'>SpecsWebsites</a> folder which contains all the required support python codes for the scrapy spider to work. Specifically, the <a href='https://github.com/NathanAW24/NewPhone2022/blob/main/OfficialWebsites/OfficialWebsites/items.py'>items.py</a> file, is heavily required to create the fields/columns/features to store the scraped data. I tried to include as many features as possible, but not all of them will be used directly. Some of them will just be additional information for the client to look at.

As specified previously, the required specifications are:
- Strong Battery (> 3500 mAh)
- Dual-SIM available
- Fast and responsive screen display (120 Hz)
- Relatively good price (< SG$1700)
- Earphone jack available
- Diagonal size (6.0 inches - 6.5 inches)

## Instructions
Assuming that scrapy is already installed, the following code can be directly typed into the terminal.
```
scrapy startproject OfficialWebsites
```
The whole configuration files and support codes will be automatically created as a base template.

However, due to the limits on <a href='https://www.gsmarena.com/'>gsmarena</a>, you are highly advised to lower down the requests number per time to not get your IP address blocked by the website.