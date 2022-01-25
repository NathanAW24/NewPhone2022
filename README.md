# NewPhone2022

## Overview
This project is made to help a client decide on which is the most worth phone with as little relative judgement as possible. The client specified that the phone brand should be in between apple, asus, and sony.

From online research through multiple websites, the recommended specifications are as follows.
- Strong Battery (> 3500 mAh)
- Dual-SIM available
- Fast and responsive screen display (120 Hz)
- Relatively good price (< SG$1700)
- Earphone jack available
- Diagonal size (6.0 inches - 6.5 inches)

By scraping through the official websites of apple, asus, and sony, I am able to see the models they are currently selling and their respective prices. After getting data on the phones they are selling, I also scraped gsmarena.com to get the specs for each model. Then, after compilling the two available dataset, I am able to continue cleaning and filtering the data based on the recommended specifications.

## Structure
This repository consists of two folders, <a href='https://github.com/NathanAW24/NewPhone2022/tree/nathan-commits/OfficialWebsites'>OfficialWebsites</a> and <a href='https://github.com/NathanAW24/NewPhone2022/tree/nathan-commits/SpecsWebsites'>SpecsWebsites</a>. OfficialWebsites is created to scrape for the available phones and their pricings while SpecsWebsites is created to scrape for the specifications from gsmarena.

There is also a <a href='https://github.com/NathanAW24/NewPhone2022/blob/nathan-commits/cleanData.ipynb'>cleanData.ipynb</a> file which contains the code for cleaning and filtering the phone options.

Required Python Libraries:
- Scrapy
- pandas

## Installation
If you have git, type this code in your terminal (bash/cmd/powershell) to clone the repository in your preferred location.
```
git clone https://github.com/NathanAW24/NewPhone2022.git
```
Otherwise, you can try to download this manually by zip.