#!/usr/bin/env python
# coding: utf-8

# # Dataframe to Array of Dictionaries

# In[1]:


import pandas as pd


# In[19]:


df = pd.read_excel('Result_id_189.xlsx')


# In[20]:


df


# In[14]:


df.set_index('VALUER', inplace = True)


# In[8]:


res = df.transpose()


# In[9]:


res


# In[15]:


res['residual_age']


# In[23]:


lst  = df.set_index('VALUER').T.to_dict('list')


# In[24]:


lst


# In[25]:


lst['report_date']


# In[ ]:




