#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests


# In[6]:


url = "http://213.14.250.112:2323/AceDataService.svc?wsdl"


# In[9]:


from suds.client import Client
client = Client("http://213.14.250.112:2323/AceDataService.svc?wsdl")


# In[11]:


print(client)


# In[28]:


response = client.service.GetIndex("MesasGes2", "Mesas753", 100571)


# In[29]:


response


# In[54]:


response=client.service.GetProfileData("MesasGes2", "Mesas753", 100571,tarih,tarih2)


# In[55]:


response


# In[68]:


json=response._Sonuc[0]


# In[69]:


json


# In[72]:


import pandas as pd


# In[74]:


Pd_Series1 = pd.Series(json)


# In[80]:


Pd_Series1


# In[81]:


df = pd.DataFrame(Pd_Series1)


# In[101]:


Pd_Series1[4][0]


# In[103]:


df[0][0][0]


# In[126]:


data = pd.io.json.json_normalize(df[0][0])
label = df[0][0]["Capasitive"]


# In[127]:


label


# In[58]:


an = datetime.datetime.now()


# In[18]:


import datetime


# In[21]:


an


# In[22]:


bugün = datetime.datetime.today()


# In[23]:


bugün


# In[25]:


bugün=datetime.datetime.strftime(an, '%x')


# In[26]:


bugün


# In[41]:


an = datetime.datetime.now()
tarih = datetime.datetime.strftime(an, '%Y-%m-%d %H:%M:%S')
tarih


# In[51]:


saa=datetime.datetime(2022, 11, 14)


# In[48]:


tarih = datetime.datetime.strftime(saa, '%Y-%m-%d')
tarih


# In[53]:


tarih2 = datetime.datetime.strftime(saa, '%Y-%m-%d')
tarih2


# In[ ]:




