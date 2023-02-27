from lxml import etree, html
from bs4 import BeautifulSoup
import requests
import re
import bs4


source_url = 'http://seshatdatabank.info/browser/AfDurrn'

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
#print(main_text)
# puts each paragraph into a separate element of a list.
# or
# lets put everything in a helping_dic
helping_dic = {}
majid_text= []
for goodie in main_text:
    if goodie.text not in helping_dic.keys():
        helping_dic[goodie.text] = goodie.text
        majid_text.append(goodie.text)
        #print(goodie.text)
        #print()

print(len(main_text))
print(len(helping_dic))




#with open('ref_seshat.csv', 'w') as my_file:
#    pass


