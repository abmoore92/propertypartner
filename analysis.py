import pandas as pd
import time
import datetime

#pivot using data source time for index and property code for column, value choice as input
def timeSeriesPivot(df,column,timetype):
    return df.pivot(index=timetype,columns='code',values=column)

#calculate totals on time period for a specific column
def timeSeriesTotals(df,column,timetype):
    return timeSeriesPivot(df,column,timetype).sum(axis=1)

def timeSeriesTotalsMultipleMetrics(df,columns,timetype):
    outdata = pd.DataFrame()
    for col in columns:
        outdata[col] = timeSeriesTotals(df,col,timetype)
    return outdata

#means are not being valuation weighted
def timeSeriesMeans(df,column,timetype):
    return timeSeriesPivot(df,column,timetype).mean(axis=1)

def timeSeriesMeansMultipleMetrics(df,columns,timetype):
    outdata = pd.DataFrame()
    for col in columns:
        outdata[col] = timeSeriesMeans(df,col,timetype)
    return outdata

#last_updated causes issues with pivot because it is not unique - need to find a way of ignoring or deleting duplicated dynamically
time_setting = 'retrieve_time'

file = 'Properties_All_hourly.csv'

data = pd.read_csv(file,parse_dates=['last_updated','retrieve_time'])

pctcols = [c for c in data.columns if '%' in c]
meancols = pctcols + ['New Listing Price', 'Lowest Share Price']

datameans = timeSeriesMeansMultipleMetrics(data,meancols,time_setting)
datameans.plot()

totalcols = ['£ Available at Lowest Share Price','Amount of Highest Bid','Latest Valuation']
datatotals = timeSeriesTotalsMultipleMetrics(data,totalcols,time_setting)
datatotals.plot()

data[['code','Lowest Share Price','retrieve_time']].pivot(index='retrieve_time',columns='code').plot(title='Lowest Share Price for all properties')