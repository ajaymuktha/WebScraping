#import libraries
import nltk
import urllib
import bs4 as bs
import pandas as pd
import re
from nltk.corpus import stopwords
nltk.download('stopwords')

# Gettings the data source
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Space').read()

# Parsing the data for  creating BeautifulSoup object
soup = bs.BeautifulSoup(source,'lxml')

# Fetching the data
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',text)  
text = re.sub(r'\s+',' ',text) 
text = text.lower() 
text = re.sub(r'\d',' ',text)

# Formation of Sentences
sentences = nltk.sent_tokenize(text)



