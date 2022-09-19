# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import os
import json
import pandas as pd


os.chdir(r'C:\Users\Sky\Videos\alx_data_analyst')

#with open('tweet-json.json','w') as file:
#   json_ = requests.get('https://video.udacity-data.com/topher/2018/November/5be5fb7d_tweet-json/tweet-json.txt')
#    file.write(json_.content.decode())
    
    
with open('tweet-json.json','r') as file:
    dicts = [json.loads(i) for i in file]
        
df=[{'id':i['id'],'retweet_count':i['retweet_count'],'favorite_count':i['favorite_count'],'retweeted':i['retweeted'],'lang':i['lang']} for i in dicts]


df=pd.DataFrame(df)

df.to_csv('tweets_dataframe.csv',index=False)
