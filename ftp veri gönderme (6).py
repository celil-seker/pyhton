#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pypyodbc
db = pypyodbc.connect(
   'Driver={SQL Server};'
    'Server=10.242.1.135;'
    'Database=Medas;'
    'UID=TalepTahminGoruntuleme;'
    'PWD=Mepas@951;')
imlec = db.cursor()


# In[2]:


from warnings import filterwarnings
filterwarnings("ignore")


# In[3]:


import pandas as pd


# In[4]:


df = pd.read_sql_query("SELECT Tarih,Saat,Gerceklesen From K3_Hesaplama_V2_Sehirler",db)


# In[5]:


df


# In[11]:


import datetime


# In[12]:


now=datetime.datetime.now()


# In[13]:


d=int(now.hour)


# In[14]:


v=df.index


# In[15]:


a=len(v)


# In[16]:


df1=df.iloc[a-48:a]


# In[17]:


df1.reset_index(drop=True,inplace=True)


# In[18]:


dfk =  pd.read_csv('C:\\Users\\mpskln1777\\Documents\mete\\Meram_Daily.csv')
dfk3=dfk
df22=dfk3


# In[19]:


c=dfk.index
f=[]
f=dfk["Energy kWh"]


# In[20]:


dfkl=dfk


# In[21]:


s=dfk["Starts dd.mm.YYYY HH:MM"]


# In[22]:


da=[]


# In[23]:


from datetime import datetime


# In[24]:


for v in range(len(s.index)): 
    a=s[v]
    format_data = "%d.%m.%Y %H:%M"
    date = datetime.strptime(a, format_data)
    dat=datetime.strftime(date, '%d %m %Y')
    sat=datetime.strftime(date, '%H')
    s[v]=dat
    da.append(sat)


# In[25]:


sl=df1["tarih"]


# In[26]:


for lv in range(len(sl.index)): 
    a=sl[lv]
    format_data = "%d.%m.%Y %H:%M:%S"
    date = datetime.strptime(a, format_data)
    dat=datetime.strftime(date, '%d %m %Y')
    sl[lv]=dat


# In[27]:


dfkl["Ends dd.mm.YYYY HH:MM"]=da


# In[28]:


dfk.rename(columns ={'Starts dd.mm.YYYY HH:MM':'tarih','Ends dd.mm.YYYY HH:MM':'saat','Energy kWh':'kwh'},inplace=True)


# In[29]:


for v in range(len(dfk.index)):
    for j in range(len(df1.index)):
        if (dfk.tarih[v] == df1.tarih[j] and int(dfk.saat[v]) == int(df1.saat[j])):
            if (int(df1.saat[j])<=d-3):
                dfk.kwh[v]=int(df1.gerceklesen[j])*1000


# In[30]:


dfk.rename(columns ={'tarih':'Starts dd.mm.YYYY HH:MM','saat':'Ends dd.mm.YYYY HH:MM','kwh':'Energy kWh'},inplace=True)


# In[31]:


df22["Energy kWh"]=dfk["Energy kWh"]


# In[32]:


df22 =  pd.read_csv('C:\\Users\\mpskln1777\\Documents\mete\\Meram_Daily.csv')


# In[33]:


df22["Energy kWh"]=dfk["Energy kWh"]


# In[34]:


kr8=df22.to_csv('Meram_Daily.csv',index=False)


# In[35]:


kr9=df22.to_csv('C:\\Users\\mpskln1777\\Documents\mete\\Meram_Daily.csv',index=False)


# In[36]:


import ftplib


# In[37]:


ftp = ftplib.FTP("ftp.meteologica.com", "Mepas", "2Az4-Gk_")


# In[38]:


ftp.cwd("/Calibration/Daily")


# In[39]:


yerel='Meram_Daily.csv'
ftp.storbinary('STOR '+yerel, open(yerel, 'rb'))


# In[40]:


ftp.dir()


# In[41]:


ftp.quit()


# In[42]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
sender = 'info@mepasenerji.com'
receivers = ['celil.seker@mepasenerji.com']
port = 25
msg=MIMEMultipart()
msg['Subject'] = 'Meteologica K3 Tahmini'
msg['From'] = 'info@mepasenerji.com'
msg['To'] = 'celil.seker@mepasenerji.com'
eklenti_dosya_ismi=yerel
dsgFilename=yerel
msg.attach(MIMEText("merhaba Meteologica gönderilen dosya ektedir.Saygılarımla"))
with(open(eklenti_dosya_ismi,'rb')) as eklenti_dosyasi:
    payload=MIMEBase('text', 'csv',name=dsgFilename)
    payload.set_payload(eklenti_dosyasi.read())
    encoders.encode_base64(payload)
    payload.add_header("Content-Decomposition","attachment",filename=eklenti_dosya_ismi)
    msg.attach(payload)
    msg_str=msg.as_string()
with smtplib.SMTP('mail.mepasenerji.com', 25) as server:
    server.sendmail(sender, receivers, msg_str)
    print("Successfully sent email")


# In[43]:


import os
os.remove(yerel, dir_fd=None)


# In[ ]:




