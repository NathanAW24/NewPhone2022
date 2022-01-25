# SpecsWebsites

## Overview
This repository helds the scrapy spider for scraping the website gsmarena.com to 

official websites of the companies to get the available products and prices. In the <a href='https://github.com/NathanAW24/NewPhone2022/tree/main/OfficialWebsites/OfficialWebsites/spiders'>spiders</a> folder there are three scrapers to respectively scrape for Apple, Asus, and Sony.

Go back from there one directory there is an <a href='https://github.com/NathanAW24/NewPhone2022/tree/main/OfficialWebsites/OfficialWebsites'>OfficialWebsites</a> folder which contains all the required support python codes for the scrapy spider to work. Specifically, the <a href='https://github.com/NathanAW24/NewPhone2022/blob/main/OfficialWebsites/OfficialWebsites/items.py'>items.py</a> file, is heavily required to create the fields/columns/features to store the scraped data.

## Instructions
Assuming that scrapy is already installed, the following code can be directly typed into the terminal.
```
scrapy startproject OfficialWebsites
```
The whole configuration files and support codes will be automatically created as a base template.

Specs to look for:
- Battery
- Memory
    - RAM
    - ROM
    - SD Card Storage (Have or not)
- Processor
- RAM
- Screen Size
    - Height
    - Width
    - Diagonal
- Operating System

(Unfinished)