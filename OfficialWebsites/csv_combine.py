import pandas as pd


df = pd.concat(
    map(pd.read_csv, ['appleRaw.csv', 'asusRaw.csv', 'sonyRaw.csv']), ignore_index=True)
df.to_csv('OfficialWeb_Phones.csv', index=False)
