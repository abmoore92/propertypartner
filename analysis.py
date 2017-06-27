import pandas as pd
import time
import datetime

#pivot using data source time for index and property code for column, value choice as input
def timeSeriesPivot(df,column):
    return df.pivot(index='time',columns='code',values=column)

#calculate totals on time period for a specific column
def timeSeriesTotals(df,column):
    return timeSeriesPivot(df,column).sum(axis=1)

def timeSeriesTotalsMultipleMetrics(df,columns):
    outdata = pd.DataFrame()
    for col in columns:
        outdata[col] = timeSeriesTotals(df,col)
    return outdata

#means are not being valuation weighted
def timeSeriesMeans(df,column):
    return timeSeriesPivot(df,column).mean(axis=1)

def timeSeriesMeansMultipleMetrics(df,columns):
    outdata = pd.DataFrame()
    for col in columns:
        outdata[col] = timeSeriesMeans(df,col)
    return outdata


data = pd.read_csv('Properties_All_example.csv',parse_dates=['time'])

pctcols = [c for c in data.columns if '%' in c]
meancols = pctcols + ['New Listing Price', 'Lowest Share Price']

datameans = timeSeriesMeansMultipleMetrics(data,meancols)
datameans.plot()

totalcols = ['£ Available at Lowest Share Price','Amount of Highest Bid','Latest Valuation']
datatotals = timeSeriesTotalsMultipleMetrics(data,totalcols)
datatotals.plot()