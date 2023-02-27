from lxml import etree, html
from bs4 import BeautifulSoup
import requests
import csv
import re
import bs4
import json
import time

my_politys = []
with open("c:/my_python/politys2.csv", 'r') as pol_csv:
    csv_reader = csv.reader(pol_csv, delimiter=',')
    for row in csv_reader:
        my_politys.append(row[2])


for pol in my_politys:
    print(pol)      

helping_dic = {}
big_dic ={}
politys = ['AfGhurd', 'AfDurrn']    # with all the names
for polity in my_politys:
    source_url = 'http://seshatdatabank.info/browser/' + polity
    #source_url = 'http://seshatdatabank.info/browser/AfDurrn'
    #print(source_url)

    # cool trick
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    #source = requests.get(source_url, headers=headers).text
    source = requests.get(source_url, headers=headers)

    #soup = html.fromstring(source)
    soup = BeautifulSoup(source.content.decode('utf-8'), 'lxml')

    # selects the main text
    main_text = soup.find_all('span', class_ = 'reference-text')
    #for my_ref in main_text:
    #    print(my_ref.find_previous('a')['href'])
    #print(main_text)
    # puts each paragraph into a separate element of a list.
    # or
    # lets put everything in a helping_dic
    #helping_dic = {}
    majid_text= []
    # dic that will save a dictionary for each polity, keeping all the records.
    big_dic[polity] = {}
    for goodie in main_text:
        inside_href_messy = goodie.find_previous('a')['href']
        inside_number_neat = inside_href_messy.split('-')[1]
        key_for_unique = polity + '_' + str(inside_number_neat)
        if goodie.text not in helping_dic.keys():
            key_for_unique = polity + '_' + str(inside_number_neat)
            #inside_number = my_ref.find_previous('a')['href']
            helping_dic[key_for_unique] = goodie.text
            helping_dic[goodie.text] = goodie.text
            #helping_dic[polity] = {}
            majid_text.append(goodie.text)
            #helping_dic[]
            #print(goodie.text)
            #print()
        big_dic[polity][inside_href_messy] = goodie.text
        #my_ref.find_previous('a')['href']
    print(source_url, ' : ', len(majid_text))
    time.sleep(5)

print(len(big_dic))

with open('c:/my_python/all_polity_based_refs2.json', 'w') as fp:
    json.dump(big_dic, fp)

print(len(helping_dic))

with open('c:/my_python/unique_polity_based_refs2.json', 'w') as fpf:
    json.dump(helping_dic, fpf)