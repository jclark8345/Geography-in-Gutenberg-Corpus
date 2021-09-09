"""
Created on Fri Dec  6 16:25:36 2019

authors: Ethan Davis, Justin Clark, Hannah Tosi, Jackie Littlefield
"""
###This code was run on the VACC###
from pathlib import Path
import argparse
import json
import pandas as pd
import geograpy
from gutenberg.cleanup import strip_headers

#recieves job file as argument from bash script
def make_args():
    description = 'get proverbs from gutenberg books'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-ifile',
                        '--inputfile',
                        help='path to input directory of books',
                        required=True,
                        type=valid_path)
    return parser.parse_args()

def valid_path(p):
    return Path(p)

#extracts list of book files from the job text
def get_filenames(infile):
    files = []
    with open(infile, 'r') as myfile:
        for line in myfile:
            files += [line.rstrip()]
    return files

#reads in GeoNames data
def gather_geodata():
    geodata = pd.read_csv('./geo/geodata.csv')
    return geodata

#reads through a book and extracts place names
def read(myfile, filename, geodata):
    d = []
    for row in myfile:
        d += [row]
    s = ''.join(d)
    #remove header and footer
    s1 = strip_headers(s).strip()
    lx = s1.splitlines()   
    #divide into 20 sections to avaid memory errors with geograpy
    frac = round(len(lx)*.05)
    ls = [lx[frac*x:frac*(x+1)] for x in range(19)]
    ls += [lx[frac*19:]]
    #gather place names with geograpy
    #and crossreference with GeoNames
    instances = dict()
    instances['file'] = filename
    instances['cities'] = dict()
    instances['countries'] = dict()
    for l in ls:
        s2 = ' '.join(l)
        places = geograpy.get_place_context(text = s2)
        country_mentions = places.country_mentions
        city_mentions = places.city_mentions
        for x in city_mentions:
            if x[0] in set(geodata.loc[:,'cities']):
                if x[0] in instances.keys():
                    instances['cities'][x[0]] += x[1]
                else:
                    instances['cities'][x[0]] = x[1]
        for x in country_mentions:
            if x[0] in set(geodata.loc[:,'country_name']):
                if x[0] in instances.keys():
                    instances['countries'][x[0]] += x[1]
                else:
                    instances['countries'][x[0]] = x[1]
    return instances

#reads through all books in a job and creates a json file
if __name__ == '__main__':
    args = make_args()
    print('args made')
    infile = args.inputfile
    outname = str(infile)[18:-4] + '.json'
    geodata = gather_geodata()
    locationlist = []
    folder ='/users/a/r/areagan/scratch/gutenberg/gutenberg-007/'
    files = get_filenames(infile)
    for filename in files:
        with open(folder+filename, 'r', encoding = 'utf-8') as myfile:
            try:
                a = read(myfile, filename, geodata)
                locationlist += [a]
            except:
                continue
    locdata = dict()
    locdata["data"] = locationlist
    with open('./geo/json_outs2/'+outname , 'w') as fp:
        json.dump(locdata, fp)