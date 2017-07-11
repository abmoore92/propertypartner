import pandas as pd
import time
import datetime

def write_today(df):
    date = time.strftime("%Y-%m-%d")
    df.to_csv('Properties_'+date+'.csv')

def append_today(df):
    df.to_csv('Properties_All.csv', mode='a', header=False)

def read_datasource_time(source_string):
    return datetime.datetime.strptime(source_string[21:-15],'%b %d %Y %H:%M:%S')


url = 'https://docs.google.com/spreadsheets/d/19h2GmLN-2CLgk79gVxcazxtKqS6rwW36YA-qvuzEpG4/export?format=xlsx'
df = pd.read_excel(url, header=1).rename(columns={'Unnamed: 1':'code'})
source = pd.read_excel(url).columns[0]
df['source'] = source
df['time'] = datetime.datetime.now()
#write_today(df)
append_today(df)