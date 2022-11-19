#!/usr/bin/env python
# coding: utf-8

# In[12]:


import ftplib


# In[13]:


import os, os.path


# In[14]:


ftp = ftplib.FTP("ftp.meteologica.com", "Mepas", "2Az4-Gk_")


# In[15]:


ftp.cwd("/Forecast")


# In[16]:


d=ftp.retrlines('LIST')  


# In[17]:


a=ftp.nlst()
d=len(a)


# In[18]:


k=a[d-1]


# In[19]:


UzakDosya = k
YerelDosya = k
ftp.retrbinary('RETR ' + UzakDosya, open(YerelDosya, 'wb').write)


# In[24]:


ftp.quit()


# In[21]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
sender = 'info@mepasenerji.com'
receivers = ['enerjipiyasasi@mepasenerji.com']
port = 25
msg=MIMEMultipart()
msg['Subject'] = 'Meteologica K3 Tahmini'
msg['From'] = 'info@mepasenerji.com'
msg['To'] = 'enerjipiyasasi@mepasenerji.com'
eklenti_dosya_ismi=k
dsgFilename=k
msg.attach(MIMEText("merhaba Meteologica tahmini ektedir.Saygılarımla"))
with(open(eklenti_dosya_ismi,'rb')) as eklenti_dosyasi:
    payload=MIMEBase('tezt', 'csv',name=dsgFilename)
    payload.set_payload(eklenti_dosyasi.read())
    encoders.encode_base64(payload)
    payload.add_header("Content-Decomposition","attachment",filename=eklenti_dosya_ismi)
    msg.attach(payload)
    msg_str=msg.as_string()
with smtplib.SMTP('mail.mepasenerji.com', 25) as server:
    server.sendmail(sender, receivers, msg_str)
    print("Successfully sent email")


# In[23]:


_files = []
ftp.retrlines("LIST", _files.append)
files = []
for _file in _files:
     _file = _file.strip().split()[-1]
    if _file.find(date[2:8]) != -1:
        files.append(_file)
        logger.info('Found file {}', _file)


# In[ ]:


serverfiles.index


# In[ ]:


print( len([name for name in os.listdir('.') if os.path.isfile(name)]))


# In[ ]:


LIST


# In[10]:


a


# In[11]:


LISTNLST'LIST'LISTNLSTsys


# In[ ]:


a=ftp.nlst()
d=len(a)


# In[ ]:


fa=ftp.mlsd()


# In[ ]:


fa


# In[ ]:


print(a)


# In[ ]:


a


# In[ ]:


d


# In[ ]:


k=a[d-1]


# In[ ]:


k


# In[ ]:


UzakDosya = k
YerelDosya = k
ftp.retrbinary('RETR ' + UzakDosya, open(YerelDosya, 'wb').write)


# In[ ]:


ftp.quit()


# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
sender = 'info@mepasenerji.com'
receivers = ['enerjipiyasasi@mepasenerji.com']
port = 25
msg=MIMEMultipart()
msg['Subject'] = 'Meteologica K3 Tahmini'
msg['From'] = 'info@mepasenerji.com'
msg['To'] = 'enerjipiyasasi@mepasenerji.com'
eklenti_dosya_ismi=k
dsgFilename=k
msg.attach(MIMEText("merhaba Meteologica tahmini ektedir.Saygılarımla"))
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


# In[ ]:


import os
os.remove(k, dir_fd=None)


# In[ ]:





# In[ ]:




