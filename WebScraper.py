#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging
import os
import pandas as pd
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import requests
from bs4 import BeautifulSoup
import pandas as  pd


# In[2]:


def extract_company(text):
    return text.split('Name:')[-1]
def extract_purpose(text):
    return text.split('Purpose:')[-1]


# In[3]:


URL = 'http://3.95.249.159:8000/random_company'


# In[4]:


df=pd.DataFrame(columns=['Company','Purpose'])


# In[5]:


company=[]
purpose=[]
for i in range(50):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    li_elem = soup.find_all('li')
    for li in li_elem:
        if li.text.find('Purpose:')==0:
            purpose.append(extract_purpose(li.text))
        elif li.text.find('Name:')==0:
            company.append(extract_company(li.text))
        else:
            continue


# In[6]:


df['Company']=company


# In[7]:


df['Purpose']=purpose


# In[8]:


df.to_csv('company.csv')

