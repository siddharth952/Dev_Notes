# python3 -m pip list


from keys import consumer_key
import requests
import pandas

url = 'https://api.tdameritrade.com/v1/instruments/'

df = pd.read_excel('company_List.xlsx')

payload = { 'apikey': consumer_key,
            'symbol': 'GOOG',
            'projection':'fundamental'}

results = requests.get(url,params=payload)

print(results.json())