import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import datetime


path='exchange_data'
if not os.path.exists('exchange_data'):
    os.makedirs('exchange_data')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36','referer':'https://www.cbn.gov.ng/'}
response=requests.get('https://www.cbn.gov.ng/rates/exchratebycurrency.asp',headers = headers)
if response.status_code == 403 or response.status_code == 401:
    print("The request has been denied")
    exit()
soup=BeautifulSoup(response.content,'lxml')

ans = soup.find('a',text=' Export Exchange Rate Results to Excel / CSV ')
href=ans['href']
url= ('https://www.cbn.gov.ng' + href)
with open('exchange_data/exchange.csv','w') as file:
    content=requests.get(url)
    file.write(content.content.decode())

    
df=pd.read_csv('exchange_data/exchange.csv')
todaytime=datetime.date.today()
today=todaytime.strftime('%#m/%#d/%Y')
try:
    todays_rates=df.loc[today]
except:
    try:
        print("Todays rates are not up yet.... Do you want yesterdays rates?.... (Y/N)")
        yesterday = input(">> ")
        if yesterday.lower() == 'n':
            exit()
        elif yesterday.lower() == 'y':
            delta=datetime.timedelta(days=1)
            day = todaytime - delta
            day = day.strftime('%#m/%#d/%Y')
            todays_rates=df.loc[day]
        else:
            print('option not recognized')
    except:
        print("Testerdays rate not available, should I print the latest rates?.... (Y/N)")
        latest = input(">> ")
        if latest.lower() == 'n':
            exit()
        elif latest.lower() == 'y':
            day = df.index[0]
            todays_rates=df.loc[day]
        else:
            print('option not recognized')
    
print(todays_rates[["Rate Date","Currency","Rate Year","Rate Month"]].rename(columns={'Rate Date':'Currency','Currency':'Year','Rate Year':'Month','Rate Month':'Buying Rate'}))
input('Press enter to continue...')
print("Do you want to keep exchange rate csv file?... (Y/N)")

ans=input('>>')
if ans.lower() == 'n':
    try:
        os.remove("exchange_data/exchange.csv")
    except:
        print("File does not exist")
elif ans.lower() == 'y':
    print("collect csv from the folder exchange_data in current directory")
else:
    print('option not recognized')


input("Press Enter to exit...")