#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from prophet import Prophet
import prophet as ph
import os
import pkg_resources
import logging
import numpy as  np


# In[2]:


from prophet.models import StanBackendEnum 


# In[3]:


model_file ='C:\\Users\\mpskln1777\\Anaconda3\\Lib\\site-packages\prophet\\stan_model\\prophet_model.bin'


# In[4]:


import cmdstanpy


# In[5]:


logger = logging.getLogger('model_file')
logger.setLevel(logging.DEBUG)
m = Prophet(yearly_seasonality=True,
seasonality_prior_scale=0.005,
changepoint_prior_scale=0.800,stan_backend='CMDSTANPY')
print(m.stan_backend)


# In[6]:


m = Prophet(stan_backend='CMDSTANPY')
print(f'Using backend: {m.stan_backend.get_type()}')


# In[17]:


df3 = pd.read_excel('//MPSTLPSRV2//TalepTahminPaylasim2//model//yıllık.xlsx')


# In[18]:


df3.info()


# In[ ]:





# In[ ]:





# In[11]:


c_tahmin=table.loc[:,["dagıtılan enerji"]]


# In[12]:


c_tahmin.reset_index(drop=False,inplace=True)


# In[40]:


df = pd.DataFrame()
df['ds'] = pd.to_datetime(df3['Tarih'])
df['y'] = df3['Gerçekleşen']


# In[41]:


m = Prophet(weekly_seasonality=True,stan_backend='CMDSTANPY')


# In[42]:


m.fit(df)


# In[43]:


future = m.make_future_dataframe(periods=744, freq='H')
forecast= m.predict(future)


# In[44]:


holiday = pd.DataFrame({
  'ds': df['ds'],
  'holiday': 'start',
  'lower_window': 0,
  'upper_window': 2,
})


# In[45]:


m=Prophet(interval_width=3,stan_backend='CMDSTANPY')
m = Prophet(mcmc_samples=100000,stan_backend='CMDSTANPY')
m = Prophet(yearly_seasonality=True,
seasonality_prior_scale=0.2,
changepoint_prior_scale=0.1,stan_backend='CMDSTANPY')
m.fit(df)
future = m.make_future_dataframe(periods=15, freq='M')
forecast = m.predict(future)


# In[46]:


de=forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(15)


# In[47]:


import datetime
tarih =datetime.datetime.now()
zaman_damgası = datetime.datetime.timestamp(tarih)
zaman_damgası
z=str(zaman_damgası) + ".xlsx"


# In[48]:


kr8=de.to_excel(z,sheet_name="celil")


# In[49]:


de


# In[23]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
sender = 'info@mepasenerji.com'
receivers = ['enerjipiyasasi@mepasenerji.com']
port = 25
msg=MIMEMultipart()
msg['Subject'] = 'Prophet K1 Dağıtılan Tahmini'
msg['From'] = 'info@mepasenerji.com'
msg['To'] = 'enerjipiyasasi@mepasenerji.com'
eklenti_dosya_ismi=z
dsgFilename='tahmin.xlsx'
msg.attach(MIMEText("merhaba K1 Prophet  Dağıtılan tahmini ektedir.Saygılarımla"))
with(open(eklenti_dosya_ismi,'rb')) as eklenti_dosyasi:
    payload=MIMEBase('application', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet',name=dsgFilename)
    payload.set_payload(eklenti_dosyasi.read())
    encoders.encode_base64(payload)
    payload.add_header("Content-Decomposition","attachment",filename=eklenti_dosya_ismi)
    msg.attach(payload)
    msg_str=msg.as_string()
with smtplib.SMTP('mail.mepasenerji.com', 25) as server: 
    server.sendmail(sender, receivers, msg_str)
    print("Successfully sent email")


# In[24]:


import os
os.remove(z, dir_fd=None)


# In[25]:


logger.removeFilter(model_file)


# In[ ]:





# In[ ]:




