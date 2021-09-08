# -*- coding: utf-8 -*-
"""
@author: Ethan Davis, Jackie Littlefield, Justin Clark, Hannah Tosi
"""

import pandas as pd
import numpy as np
import json
from matplotlib import pyplot as plt
#create a dataframe from the authordata.csv file
    #this file was exported from R
    #it was created in R by calling the "gutenbergr" library and 
    #accessing the "authors" data
authorsDF = pd.read_csv("authordata.csv", header = 0, encoding='latin1')

#create a copy of the dataframe
    #if the birthdate is NAN, replace it with 0
authorNAN = authorsDF.replace(np.nan,0)

#in the copy, delete all authors with a birthdate of 0
for i in range(len(authorNAN)):
    line = authorNAN.loc[i, 'birthdate']
    if authorNAN.loc[i, 'birthdate'] == np.float64(0.0):
        authorNAN = authorNAN.drop([i])

#read in the place name data collected from the gutenberg corpus
with open('geo_alldata.json') as myfile:
    js = json.load(myfile)
data = js['all']

#store the gutenberg data as a dataframe
df = pd.DataFrame(data)

#create a function that will return the first item in a list 
    #this will be used to find all the author names so they can be 
    #made into strings
def return_first(x):
    """ The return_first function returns the first element of a list """
    if x == []:
        return ''
    else:
        return x[0] 

#convert all the author names in the gutenberg corpus to strings
df["author"] = df["author"].apply(return_first)

#merge the cleaned authors data set with the gutenberg data set
merged = pd.merge(authorNAN, df, on = "author")

#read subset of the GeoNames database
geodata = pd.read_csv('geodata.csv')

#gather two letter country codes and country names
all_countries = []
for a in list(merged.loc[:,'countries']):
    for b in a.keys():
        if b not in all_countries:
            all_countries += [b]
all_countries.sort()

country_codes = dict()
for a in all_countries:
    b = geodata.loc[geodata['country_name']==a]
    code = list(b.loc[:,'country_code'])[0]
    country_codes[a] = code

#collect data by year
years = []
for year in range(-750, 1982):
    hits = merged.loc[merged['birthdate'] == year]
    years += [(year,hits)]


timeseries = dict()
for year in years:
    mentions = dict()
    for book in year[1].iterrows():
        for c in book[1]['countries']:
            if country_codes[c] not in mentions.keys():
                mentions[country_codes[c]] = 1
            else:
                mentions[country_codes[c]] += 1
    timeseries[year[0]] = mentions                
ts = pd.DataFrame(timeseries)
ts = ts.transpose()
ts = ts.fillna(0)
ts.to_csv('timeseries.csv')

timeseriestotal = dict()
for year in years:
    mentions = dict()
    for book in year[1].iterrows():
        cs = book[1]['countries']
        for c in cs:
            if country_codes[c] not in mentions.keys():
                mentions[country_codes[c]] = cs[c]
            else:
                mentions[country_codes[c]] += cs[c]
    timeseriestotal[year[0]] = mentions   
tstotal = pd.DataFrame(timeseriestotal)
tstotal = tstotal.transpose()
tstotal = tstotal.fillna(0)
tstotal.to_csv('timeseriestotal.csv')

timeseriescities = dict()
for year in years:
    mentions = dict()
    for book in year[1].iterrows():
        for c in book[1]['cities']:
            if c not in mentions.keys():
                mentions[c] = 1
            else:
                mentions[c] += 1
    timeseriescities[year[0]] = mentions                
tscities = pd.DataFrame(timeseriescities)
tscities = tscities.transpose()
tscities = tscities.fillna(0)
tscities.to_csv('timeseriescities.csv')

#gather top countries
topcountries = [(sum(ts[country]), country) for country in ts.columns]
topcountries.sort(reverse = True)
top10count = topcountries[:10]

#gather top cities
topcities = [(sum(tscities[city]), city) for city in tscities.columns]
topcities.sort(reverse = True)
top100 = topcities[:100]

#plot relative freq by decade#
tsd = ts.groupby(lambda x: (x//10)*10).sum()
#normalize rows
tsdn = tsd.div(tsd.sum(axis=1), axis=0)
tsdn.fillna(0)
#plot for all countries
tsdn.plot()
plt.title('Relative frequency by decade')
plt.xlabel('Year')
plt.ylabel('Relative freq')
plt.savefig('normalized_original.png', dpi =300)
#plot for all countries after 1800
tsdn.truncate(before = 1800).plot()
plt.title('Relative frequency by decade')
plt.xlabel('Year')
plt.ylabel('Relative freq')
plt.ylim([0,.15])
plt.savefig('1800_and_later.png', dpi =300)
#plot for top 10 countries
tsdn.truncate(before = 1600)[[x[1] for x in top10count]].plot()
plt.title('Relative frequency by decade')
plt.xlabel('Year')
plt.ylabel('Relative freq')
plt.ylim([0,.15])
plt.savefig('ts10.png', dpi =300)

#plot total metnions by decade#
#bin by decade
tstd = tstotal.groupby(lambda x: (x//10)*10).sum()
#plot after 1600
tstd.truncate(before = 1600)[[x[1] for x in top10count]].plot()
plt.title('Total mentions per decade')
plt.xlabel('Year')
plt.ylabel('total mentions')
plt.savefig('total10.png', dpi =300)


#plot top cities by decade#
tscd = tscities.groupby(lambda x: (x//10)*10).sum()
tscdn = tscd.div(tscd.sum(axis=1), axis=0)
tscdn = tscdn.fillna(0)

#list of top ciies excluding likely false posiives
cit = ['London', 'Paris', 'Rome', 'Washington', 'Berlin', 'Oxford', 'Cambridge', 'Jerusalem']
tscdn[cit].truncate(before=1600).plot()
plt.legend(prop = {'size':8})
plt.ylabel('Relative freq')
plt.xlabel('Year')
plt.title('Common Cities by Decade')
plt.savefig('common_cities2.png', dpi = 300)

#nonwest
tscdn[["Shanghai", "Istanbul", "Hong Kong", "Moscow", "Seoul", "Delhi", "Mumbai", "Cairo", "Beijing", "Tokyo", "Osaka"]].truncate(before=1600).plot()
plt.legend(prop = {'size':8})
plt.ylabel('Relative freq')
plt.xlabel('Year')
plt.title('Common Cities by Decade (Non-Western)')
plt.savefig('nonwest_cities2.png', dpi = 300)

#british
tscdn[["London", "Manchester", "Birmingham", "Leeds", "Glasgow", "Liverpool", "Newcastle", "Belfast"]].truncate(before=1600).plot()
plt.legend(prop = {'size':8})
plt.ylabel('Relative freq')
plt.xlabel('Year')
plt.title('British Cities by Decade')
plt.savefig('british_cities.png', dpi = 300)