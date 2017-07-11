import pandas as pd
import time
import datetime
import os

def write_today(df):
    date = time.strftime("%Y-%m-%d")
    df.to_csv('Properties_'+date+'.csv')

#append dataframe to file or make new file with header if no file exists
def append_now(df,filename):
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', encoding='utf-8', header=False)
    else:
        df.to_csv(filename, mode='a', encoding='utf-8', header=True)

def read_datasource_time(source_string):
    return datetime.datetime.strptime(source_string[21:-15],'%b %d %Y %H:%M:%S')


url = 'https://docs.google.com/spreadsheets/d/19h2GmLN-2CLgk79gVxcazxtKqS6rwW36YA-qvuzEpG4/export?format=xlsx'
df = pd.read_excel(url, header=1).rename(columns={'Unnamed: 1':'code','Unnamed: 12':'URL'})

source = pd.read_excel(url).columns[0]
df['source'] = source

#datetime column of when the data was most recently updated
df['last_updated'] = read_datasource_time(source)

#datetime column of the time when the script is run
df['retrieve_time'] = datetime.datetime.now()

#write this entry
filename = 'Properties_All.csv'
append_now(df,filename)