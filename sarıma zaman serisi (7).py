#!/usr/bin/env python
# coding: utf-8

# In[109]:


import warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import matplotlib
import pmdarima as pm
import pandas as pd 


# In[110]:


from matplotlib import ft2font


# In[111]:


import os
import platform
from typing import List
import sys


# In[112]:


df =  pd.read_excel('//MPSTLPSRV2//TalepTahminPaylasim2//model//k1//verison.xlsx')
df21 =  pd.read_excel('//MPSTLPSRV2//TalepTahminPaylasim2/model//k1//tüketim.xlsx')


# In[113]:


table = pd.pivot_table(df,index=['Tarih'],aggfunc=np.mean)


# In[114]:


df21.index=table.index


# In[115]:


table = pd.pivot_table(df,index=['Tarih'],aggfunc=np.mean)


# In[116]:


table


# In[117]:


table=table.join(df21)


# In[118]:


c_tahmin=table.loc[:,["dagıtılan enerji"]]


# In[119]:


c_tahmin.reset_index(drop=False,inplace=True)


# In[120]:


c_tahmin.index=c_tahmin.Tarih


# In[121]:


c_tahmin


# In[122]:


data3=c_tahmin["dagıtılan enerji"]


# In[123]:


data3=data3.to_frame()


# In[124]:


data4=data3


# In[125]:


data3.plot(figsize = (15, 6))
plt.show()


# In[126]:


from pylab import rcParams
rcParams['figure.figsize'] = 18, 8
decomposition = sm.tsa.seasonal_decompose(data3, model='additive')
fig = decomposition.plot()
plt.show()


# In[127]:


from statsmodels.tsa.stattools import adfuller
def adf_test(timeseries):
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
       dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)

print(adf_test(data3))


# In[128]:


ts_t_adj = data3 - data3.shift(1)
ts_t_adj = ts_t_adj.dropna()
ts_t_adj.plot()

print(adf_test(data3))


# In[129]:


ts_s_adj = ts_t_adj - ts_t_adj.shift(360)
ts_s_adj = ts_s_adj.dropna()
ts_s_adj.plot()


# In[130]:


from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_acf(ts_s_adj)
matplotlib.pyplot.show()
plot_pacf(ts_s_adj)
matplotlib.pyplot.show()


# In[131]:


p = range(0, 3)
d = range(1,2)
q = range(0, 3)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue


# In[132]:


my_order = (1, 1, 1)
my_seasonal_order = (1, 1, 1, 12)


# In[133]:


import statsmodels.api as sm


# In[134]:


model=sm.tsa.statespace.SARIMAX(data4,order=(1, 1, 0),seasonal_order=(1,1,0,12))
results=model.fit()


# In[135]:


results.summary()


# In[136]:


forecast_values = results.get_forecast(steps = 48)


# In[137]:


forecast_ci = forecast_values.conf_int()


# In[138]:


tahmin=forecast_values.predicted_mean.to_frame('Tahmin').rename_axis('Tarih').reset_index()


# In[139]:


import datetime
tarih =datetime.datetime.now()
zaman_damgası = datetime.datetime.timestamp(tarih)
zaman_damgası
z=str(zaman_damgası) + ".xlsx"


# In[140]:


kr8=tahmin.to_excel(z,sheet_name="Tahmin")


# In[141]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
sender = 'info@mepasenerji.com'
receivers = ['enerjipiyasasi@mepasenerji.com']
port = 25
msg=MIMEMultipart()
msg['Subject'] = 'Sarıma K1 Dağıtılan Tahmini'
msg['From'] = 'info@mepasenerji.com'
msg['To'] = 'enerjipiyasasi@mepasenerji.com'
eklenti_dosya_ismi=z
dsgFilename='tahmin.xlsx'
msg.attach(MIMEText("merhaba K1 SARIMA dağıtılan tahmini ektedir.Saygılarımla"))
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


# In[142]:


import os
os.remove(z, dir_fd=None)


# In[ ]:





# In[ ]:





# In[ ]:




