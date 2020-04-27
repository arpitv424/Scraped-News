#!/usr/bin/env python
# coding: utf-8

# In[129]:


# Importing necessary libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[5]:


news=[]


# In[39]:


# INSHORTS News Headline

url1 = requests.get('https://inshorts.com/en/read/national').text
soup1 = BeautifulSoup(url1, 'lxml')

for title in soup1.find_all('div',class_='card-stack'):
    for heading in soup1.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)

url2 = requests.get('https://inshorts.com/en/read/business').text
soup2 = BeautifulSoup(url2, 'lxml')

for title in soup2.find_all('div',class_='card-stack'):
    for heading in soup2.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)
        
url3 = requests.get('https://inshorts.com/en/read/world').text
soup3 = BeautifulSoup(url3, 'lxml')

for title in soup3.find_all('div',class_='card-stack'):
    for heading in soup3.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)
        
url4 = requests.get('https://inshorts.com/en/read/politics').text
soup4 = BeautifulSoup(url4, 'lxml')

for title in soup4.find_all('div',class_='card-stack'):
    for heading in soup4.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)
        
url5 = requests.get('https://inshorts.com/en/read/technology').text
soup5 = BeautifulSoup(url5, 'lxml')

for title in soup5.find_all('div',class_='card-stack'):
    for heading in soup5.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)
    
url6 = requests.get('https://inshorts.com/en/read/entertainment').text
soup6 = BeautifulSoup(url6, 'lxml')

for title in soup6.find_all('div',class_='card-stack'):
    for heading in soup6.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)
        
url7 = requests.get('https://inshorts.com/en/read/automobile').text
soup7 = BeautifulSoup(url7, 'lxml')

for title in soup7.find_all('div',class_='card-stack'):
    for heading in soup7.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)

url8 = requests.get('https://inshorts.com/en/read/sports').text
soup8 = BeautifulSoup(url8, 'lxml')

for title in soup8.find_all('div',class_='card-stack'):
    for heading in soup8.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)
        
url9 = requests.get('https://inshorts.com/en/read/startup').text
soup9 = BeautifulSoup(url9, 'lxml')

for title in soup9.find_all('div',class_='card-stack'):
    for heading in soup9.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)
        
url10 = requests.get('https://inshorts.com/en/read/miscellaneous').text
soup10 = BeautifulSoup(url10, 'lxml')

for title in soup10.find_all('div',class_='card-stack'):
    for heading in soup10.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)
        
url11 = requests.get('https://inshorts.com/en/read/hatke').text
soup11 = BeautifulSoup(url11, 'lxml')

for title in soup11.find_all('div',class_='card-stack'):
    for heading in soup11.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)
        
url12 = requests.get('https://inshorts.com/en/read/science').text
soup12 = BeautifulSoup(url12, 'lxml')

for title in soup11.find_all('div',class_='card-stack'):
    for heading in soup11.find_all('div',class_="news-card-title news-right-box"):
        headline=heading.a.span.text
        news.append(headline)


# In[118]:


# GOOGLE News Headlines

url13=requests.get('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en').text
soup13=BeautifulSoup(url13, 'lxml')
           
for i in soup13.findAll('a', class_='SFllF'):
    x=str(i)
    try:
        link='https://news.google.com/'+x[x.index('./')+2:x.index('ceid=IN%3Aen')+12]
        url=requests.get(link).text
        soupx=BeautifulSoup(url13, 'lxml')
        for i in ['h3']:
            for j in soupx.findAll(i):
                news.append(j.text)
        for k in ['h4']:
            for z in soupx.findAll(i):
                news.append(z.text)
    except:
        continue


# In[50]:


# FOX News Headlines

url14 = requests.get('https://www.foxnews.com/').text
soup14 = BeautifulSoup(url14, 'lxml')

for title in soup14.findAll('h2' or 'h3'):
    news.append(title.text)


# In[60]:


# DAILYMAIL News Headlines

url15 = requests.get('https://www.dailymail.co.uk/home/index.html').text
soup15 = BeautifulSoup(url15, 'lxml')

for title in soup15.findAll('h2' or 'h3'):
    news.append(title.a.text)


# In[65]:


# WASHINGTON POST News Healines

url16 = requests.get('https://www.washingtonpost.com/?noredirect=on').text
soup16 = BeautifulSoup(url16, 'lxml')

for title in soup16.findAll('h2' or 'h3'):
    news.append(title.text)


# In[69]:


# ABC News Headlines

url17 = requests.get('https://abcnews.go.com/').text
soup17 = BeautifulSoup(url17, 'lxml')

for title in soup17.findAll('div',class_='headlines-li-div'):
    news.append(title.h1.text)


# In[72]:


# BBC News Headlines

url18 = requests.get('https://www.bbc.com/news').text
soup18 = BeautifulSoup(url18, 'lxml')

for title in soup18.findAll('div',class_='gel-wrap gs-u-pt+'):
    news.append(title.h3.text)


# In[76]:


# Keywords that have chances to make the news headline viral.
# Source of Keywords: "https://buffer.com/resources/the-most-popular-words-in-most-viral-headlines"

keywords=["for","need","wait til you see","will make you","til you see what","how to","when you see","that will make you","til you see"
"will blow your mind","what happens when","it looks like a","wait til you","you need to know","here are the",
"what happened to this","you see what","the reason why is","you need to","might look like a","this is what",
"is what thappens when","that will make","for the first time","what happened","what this guy","what he found is",
"this guy","what happened to","this is what happens","that will","like a normal","thing i've ever seen",
"in the world","the definitive ranking of","what he did","look like a normal","looks like a","never","the best",
"i've ever seen","facebook","make you","how to make","awesome","blow your mind","girl","photos","love","happened",
"heart","being","something","years","found","seen","actually","valentine’s","down","reasons","watch","need","awesome","media","makes","mind",
"right","social","beautiful","happened","should","things","little","heart","facebook"]


# In[124]:


# ANTICIPATION of Virality of the news

c=0
v=[]
viral_headline=[]
for i in news:
    x=i.split()
    for j in keywords:
        for k in x:
            if k==j:
                c+=1
                viral_headline.append(i)
    v.append(c)


# In[130]:


# Length of DATASET and ANTICIPATED Viral News Headlines


print("Length of Dataset:",len(news))
print(c,"out of",len(news),"news headlines are anticipated to be viral")


# In[126]:


data = pd.DataFrame({'Id':range(len(news)), 'News_Headlines':news, 'Viral_Anticipated_News':v})
data.to_csv('scrape_news.csv')


# In[127]:


data.head(20)


# In[ ]:





# In[ ]:




