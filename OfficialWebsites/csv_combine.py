import pandas as pd

# this code is used to combine the three different csv obtained from scraping
df = pd.concat(
    map(pd.read_csv, ['appleRaw.csv', 'asusRaw.csv', 'sonyRaw.csv']), ignore_index=True)
df.to_csv('OfficialWeb_Phones.csv', index=False)
