# this file scrapes the texts from sprachbar dw and saves a latex file 
# simply put the latex source into overleaf and get the pdf file.

# next step, get everything from sprachbar:
# go to file: scrape_3.py
# 
# <div class="group">
# <h4>Sprachbar</h4>
# <ul class="smallList">
# <li><a href="/de/am-aschermittwoch-ist-alles-vorbei/l-39902505">Am Aschermittwoch ist alles vorbei</a></li>


# lots of other developments to make: Put things in functions

from types import new_class
from bs4 import BeautifulSoup
import requests
import re
import bs4


#source_url = 'https://www.dw.com/de/l%C3%BCgen/l-42305910'

source_url = 'https://www.dw.com/de/oben-und-unten-nah-und-fern/l-47931500'
# cool trick
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
source = requests.get(source_url, headers=headers).text

soup = BeautifulSoup(source, 'lxml')

# get all the useful (other) links:
main_source = 'https://www.dw.com'
list_of_urls=[]
useful_links0 = soup.find_all('ul', class_ = 'smallList')

# the good smallList is the second one of the two
useful_links = useful_links0[1].find_all('a')
print(len(useful_links))
for my_url in useful_links:
    # print(my_url['href'])
    list_of_urls.append(main_source + my_url['href'])

#list of all extracted urls
print(list_of_urls)

# next: use all these urls to make new files.






block_words = [' in ', ' auf ', ' das ', ' die ', ' der ', ' am ', ' mit ', ' ab ', ' zu ', ' wie ',
                ' an ', ' sich ', ' um ', ' mich ', ' mir ', ' von ', ' vom ', ' aus ', ' als ', ' bis ',
                ' dem ', ' den ', ' es ', ' ob ', ' obwohl ', ' des ', ' zum ', ' zur ', ' nach ',
                ' ihr ', ' ihm ', ' ihn ', ' sie ', ' über ', ' ein ', ' einen ', ' eine ', ' im ',
                ' denen ', ' bei '  ' ihre ', ' seine ', ' ihren ', ' seinen ', ' meinen ', ' so ',
                ' mein ', ' sein ', ' dein ', ' meine ', ' meiner ', ' deinen ', ' deiner ', ' euch ',
                ' seiner ', ' ihrer ', ' diese ' , ' dafür ', ' damit ', ]

# selects the main text
main_text = soup.find('div', class_ ='dkTaskWrapper tab3')

# chooses all the new word defs (keeps the word itself)
unwanted = main_text.find_all('span', class_ ='bubbleText')

# removes all new word definitions from the text
for unw in unwanted:
    unw.extract()

# a list of new words
# for unw in unwanted:
#     print(unw.text)

# puts each paragraph into a separate element of a list.
majid_text= []
for goodie in main_text.find_all('p'):
    majid_text.append(goodie.text)
    #print()
#

# replace the blocked words
new_majid=[]
used_words =set()
for par in majid_text:
    for word in block_words:
        insensitive_word = re.compile(re.escape(word), re.IGNORECASE)
        if insensitive_word:
            used_words.add(word)
        new_par = insensitive_word.sub(' (---) ', par)
        # new_par=par.replace(word, ' (---) ')
        par = new_par
    new_majid.append(par)

with open('lat_text.tex', 'w') as my_file:
    my_file.write('\\documentclass[14pt,a4paper]{extarticle}\n')
    my_file.write('\\usepackage[german]{babel}\n')
    my_file.write('\\usepackage[letterpaper,top=1.5cm,bottom=1.5cm,left=1.5cm,right=1.5cm,marginparwidth=1.5cm]{geometry}\n')
    my_file.write('\\begin{document}\n')
    # my_file.write('\\section{Used Words}')
    # for word in used_words:
    #     my_file.write(word + '| ')
    my_file.write('\\section{Text mit Blanks}')

    for par in new_majid:
        my_file.write(par)
        my_file.write('\\newline\\newline ')
    
    my_file.write('\\newline\\newline ')
    my_file.write('\\section{Text Ohne Blanks}')

    for par in majid_text:
        my_file.write(par)
        my_file.write('\\newline\\newline ')
    
    my_file.write('\\newline\\newline ')

    my_file.write('\\section{Vocabular}')

    for unw in unwanted:
        my_file.write(unw.text)
        my_file.write('\\newline\\newline ')

    my_file.write('\\end{document}')

print(used_words)
