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
from bs4 import BeautifulSoup
import requests
import re
import bs4


source_url = 'https://www.dw.com/de/l%C3%BCgen/l-42305910'

# cool trick
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
source = requests.get(source_url, headers=headers).text

soup = BeautifulSoup(source, 'lxml')
block_words = [' in ', ' auf ', ' das ', ' die ', ' der ', ' am ', ' mit ', ' ab ', ' zu ', ' an ', ' sich ', ' um ']

# selects the main text
main_text = soup.find('div', class_ ='dkTaskWrapper tab3')

# chooses all the new word defs (keeps the word itself)
unwanted = main_text.find_all('span', class_ ='bubbleText')

# removes all new word definitions from the text
for unw in unwanted:
    unw.extract()

# a list of new words
for unw in unwanted:
    print(unw.text)

# puts each paragraph into a separate element of a list.
majid_text= []
for goodie in main_text.find_all('p'):
    majid_text.append(goodie.text)
    #print()
#

# replace the blocked words
new_majid=[]
for par in majid_text:
    for word in block_words:
        insensitive_word = re.compile(re.escape(word), re.IGNORECASE)
        new_par = insensitive_word.sub(' (---) ', par)
        # new_par=par.replace(word, ' (---) ')
        par = new_par
    new_majid.append(par)

# with open('raw_text.txt', 'w') as my_file:
#     for par in new_majid:
#         my_file.write(par)
#         my_file.write('\n\n')
    
#     my_file.write('\n')

#     for par in majid_text:
#         my_file.write(par)
#         my_file.write('\n')
    
#     my_file.write('\n')

#     for unw in unwanted:
#         my_file.write(unw.text)
#         my_file.write('\n')

with open('lat_text.tex', 'w') as my_file:
    my_file.write('\\documentclass[14pt,a4paper]{extarticle}\n')
    my_file.write('\\usepackage[german]{babel}\n')
    my_file.write('\\usepackage[letterpaper,top=1.5cm,bottom=1.5cm,left=1.5cm,right=1.5cm,marginparwidth=1.5cm]{geometry}\n')
    my_file.write('\\begin{document}\n')
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



# for p in new_majid:
#     print(p)
#     print()
#print(block_words.upper())
#print()


# print(main_text.prettify())
# for p in soup.find_all('p'):
#     #print(type(p))
#     if 'registriert' in p.text:
#         print(p.text)

#print(soup.prettify())