#!/usr/bin/env python
# coding: utf-8

# # GET API

# In[9]:


import urllib.request
import json


# In[6]:


webdata = urllib.request.urlopen('https://ifsc.razorpay.com/KARB0000001').read()


# In[9]:


ifsc = json.loads(webdata)


# In[10]:


print(ifsc)


# <h4>taking ifsc code as input:
# 

# In[11]:


import requests
ifsc = input("enter the IFSC Code ")

api_url = "https://ifsc.razorpay.com/"+ifsc 
json_ifsc = requests.get(api_url)

if json_ifsc.status_code == 200:
    print(json_ifsc.json())
elif json_ifsc.status_code == 404:
    print("Invalid IFSC")
else:
    print("Unexpected error")


# In[ ]:




