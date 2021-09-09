#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:49:27 2019

@author: Ethan Davis, Hannah Tosi, Justin Clark, Jackie Littlefield
"""
###combines jsons from all jobs into one###
import os
import json
from gutenberg.query import get_metadata

geo_data = dict()
geo_data['all'] = []
path = './geo/json_outs'
for a in os.listdir(path):
    with open(path+'/'+a, 'r') as myfile:
        for line in myfile:
            f = json.loads(line)
            geo_data['all'] += f['data']
for x in geo_data['all']:
    x['title'] = list(get_metadata('title', x['file'][:-4]))
    x['author'] = list(get_metadata('author', x['file'][:-4]))
    x['language'] = list(get_metadata('language', x['file'][:-4]))
with open('./geo/geo_alldata.txt', 'w') as fp:
    json.dump(geo_data, fp)


