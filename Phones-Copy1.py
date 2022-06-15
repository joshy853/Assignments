#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import bs4


# In[3]:


from bs4 import  BeautifulSoup


# In[4]:


url="https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree"


# In[5]:


res=requests.get(url)


# In[6]:


res


# In[7]:


phones=BeautifulSoup(res.text)


# In[8]:


phones


# In[32]:


phones_names=phones.select("._4rR01T")


# In[33]:


phones_names


# In[28]:


phones_names=[]


# In[13]:


for item in phones:
    phones_names.append(item.text)
    phones_names


# In[14]:


phones_names


# In[16]:


price=phones.select("._1_WHN1")


# In[17]:


price


# In[18]:


prices_rating=[]


# In[19]:


for item in price:
    prices_rating.append(item.text)
    prices_rating


# In[20]:


prices_rating


# In[22]:


battery=phones.select(".rgWa7D:nth-child(4)")


# In[23]:


battery


# In[24]:


import pandas as pan


# In[35]:


data=pan.DataFrame(phones_names,columns=["phones name"])


# In[36]:


data


# In[37]:


data.to_csv("C:/Users/Joshy/Desktop/New folder.csv")


# In[38]:


data


# In[ ]:




