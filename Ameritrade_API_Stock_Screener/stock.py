# python3 -m pip list


from keys import consumer_key
import requests
import time # Need to pause due to fast computer time as the file name
import re # Regular Expressions to change all of the problem expressions
import pickle as pkl
import pandas as pd

url = 'https://api.tdameritrade.com/v1/instruments/'

df = pd.read_excel('/Users/siddharthsen/Desktop/Dev_Notes/Ameritrade_API_Stock_Screener/company_list.xlsx')

# Grab only the symbols
symbols = df['Symbol'].values.tolist()

# Way to bypass 500 requests at a time limit
start,end = 0,500
while start < len(symbols):
    tickers = symbols[start:end]

    payload = { 'apikey': consumer_key,
                'symbol': tickers,
                'projection':'fundamental'}

    results = requests.get(url,params=payload)
    data = results.json()
    f_name = time.asctime() + '.pkl'
    # Fix Colon and space b/w time
    f_name = re.sub('[ :]','_',f_name)
    # Create file and dump the data
    with open(f_name,'wb') as file:
        pkl.dump(data,file)

    start,end = end,end+500
    time.sleep(1)


