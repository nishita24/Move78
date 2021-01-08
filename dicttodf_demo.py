#!/usr/bin/env python
# coding: utf-8

# # Array of Dictionaries to Dataframe

# In[1]:


import pandas as pd


# In[55]:


file = open('message.txt')


# In[56]:


arr = file.read()
arr


# In[57]:


file.close()


# In[50]:


import json 
dict_arr = json.loads(arr)


# In[51]:


dict_arr


# In[52]:


df = pd.DataFrame(dict_arr)


# In[53]:


df


# In[58]:


df.to_excel("output.xlsx")


# In[ ]:




