# this file scrapes the texts from sprachbar dw and saves a latex file 
# simply put the latex source into overleaf and get the pdf file.

# next step, get everything from sprachbar:
# go to file: scrape_3.py
# 
# <div class="group">
# <h4>Sprachbar</h4>
# <ul class="smallList">
# <li><a href="/de/am-aschermittwoch-ist-alles-vorbei/l-39902505">Am Aschermittwoch ist alles vorbei</a></li>

from types import new_class
from lxml import etree, html
from bs4 import BeautifulSoup
import requests
import re
import bs4


source_url = 'https://www.verywellmind.com/imposter-syndrome-and-social-anxiety-disorder-4156469'

# cool trick
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
#source = requests.get(source_url, headers=headers).text
source = requests.get(source_url, headers=headers)

#soup = html.fromstring(source)
soup = BeautifulSoup(source.content.decode('utf-8'), 'lxml')

block_words = [' in ', ' the ', ' a ', ' to ', ' off ', ' on ', ' with ', ' by ', ' across ', ' along ',
                        ' more ', ' its ', ' them ', ' at ', ' about ', ' that ', ' this ', ' it ',
                        ' of ', ' get ', ' take ', ' from ', ' as ', ' while ', ' when ',
                        ' out ', ' under ', ' about ', ' for ', ' been ', ' was ', ' had ',
                        ' have ', ' whether ', ' his ', ' her ', ' most ', ' less ', ' among '
                        ' over ', ' like ', ' up ', ' towards ', ' near ', ' nearly ', ' despite ',
                        ' though ', ' except ', ' against ', ' between ', ' either ', ' nor ']

#  class_='comp mntl-sc-block mntl-sc-block-html'
# class_='mntl-sc-block-heading__text'
# selects the main text
#main_text = soup.find_all(['p','span']).findAll(True, {'class':['comp mntl-sc-block mntl-sc-block-html', 'mntl-sc-block-heading__text']})
main_text = soup.findAll(True, {'class':['comp mntl-sc-block mntl-sc-block-html',
                                             'mntl-sc-block-heading__text',
                                             'comp expert-content mntl-sc-block-callout-body mntl-text-block']})

#print(main_text)
# puts each paragraph into a separate element of a list.
majid_text= []
for goodie in main_text:
    if goodie.get('id') =='mntl-sc-block-callout-body_1-0-1':
        goodtext= '\\textbf{' + goodie.text + '}'
        majid_text.append(goodtext)
    else:
        majid_text.append(goodie.text)
    #print(goodie)
    #print()
#

# replace the blocked words
# new_majid=[]
# for par in majid_text:
#     for word in block_words:
#         insensitive_word = re.compile(re.escape(word), re.IGNORECASE)
#         new_par = insensitive_word.sub(' (---) ', par)
#         # new_par=par.replace(word, ' (---) ')
#         par = new_par
#     new_majid.append(par)


# fror pure texts to escape the apostrophe problem
new_majid=[]
for par in majid_text:
    for word in block_words:
        insensitive_word = re.compile(re.escape(word), re.IGNORECASE)
        new_par = insensitive_word.sub(' (...) ', par)
        # new_par=par.replace(word, ' (---) ')
        par = new_par
    new_majid.append(par)

with open('lat_text_eng.tex', 'w') as my_file:
    my_file.write('\\documentclass[14pt,a4paper]{extarticle}\n')
    my_file.write('\\usepackage[english]{babel}\n')
    my_file.write('\\usepackage[letterpaper,top=1.5cm,bottom=1.5cm,left=1.5cm,right=1.5cm,marginparwidth=1.5cm]{geometry}\n')
    my_file.write('\\begin{document}\n')
    my_file.write('\\section{Text with Blanks}')

    for par in new_majid:
        my_file.write(par)
        my_file.write('\\newline\\newline ')
    
    my_file.write('\\newline\\newline ')
    my_file.write('\\section{Text without Blanks}')

    for par in majid_text:
        my_file.write(par)
        my_file.write('\\newline\\newline ')
    
    my_file.write('\\newline\\newline ')

    my_file.write('\\end{document}')


