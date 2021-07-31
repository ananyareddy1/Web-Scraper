#import libraries
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import urllib
import re
import nltk
from nltk.corpus import stopwords




#Paste url here
url = 'https://en.wikipedia.org/wiki/Web_scraping'

#Get text from html
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
text = soup.get_text()
text1 = soup.get_text("p")


#Print title and section headings

for heading in soup.find_all(["h1"]):
    print('Article title: '+ heading.text.replace("[edit]", "").strip())

print("\n")
print('Sub-headings: ')

for heading in soup.find_all(["h2"]):
    print(heading.text.replace("[edit]", "").strip())

for heading in soup.find_all(["h3"]):
    print(heading.text.replace("[edit]", "").strip())

print("\n")



words = re.findall('\w+', text1)

#Getting stopwords using nltk

stop_words = stopwords.words('english')
stopwords_dict = Counter(stop_words)
morestopwords_dict = ['the', 'and', 'to']

#Getting most frequent words and their count

print('Most frequently occurring words in the article: ')
frequent_words = Counter(words).most_common(10)
print(frequent_words)























