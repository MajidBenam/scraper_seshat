from bs4 import BeautifulSoup
import requests

# Open local file
with open('voa_1.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# to make the html prettier.
# warning: this will only get the first title tag.
#match = soup.title
#print(soup.prettify())

# treat the text inside title as an attribute and get only the text back 
#match = soup.title.text
#print(match)

# et the div with a class (don't forget the _)
#match = soup.find('div', class_='footer')
#print(match)

#article = soup.find('div', class_='article')
#headline = article.h2.a.text
# print(headline)


# for article in soup.find_all('div', class_='article'):
#     headline=article.h2.a.text
#     print(headline)

#     summary = article.p.text
#     print(summary)

#     print()
list_of_ps = soup.find_all('p')

for i in range(1, len(list_of_ps)-2):
    print(list_of_ps[i].text)
        #print(type(p.a.href))