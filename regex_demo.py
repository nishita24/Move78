#!/usr/bin/env python
# coding: utf-8

# # RegEx

# In[2]:


import re


# In[20]:


pincode = input("Enter any pincode ")
res_p = re.search("^[1-9]{1}[0-9]{5}$", pincode)

if res_p:
    print("Valid")
else:
    print("Invalid")


# In[8]:


ifsc_code = input("Enter any IFSC code ")
res_i = re.search("^[A-Z]{4}0[A-Z 0-9]{6}$", ifsc_code)

if res_i:
    print("Valid")
else:
    print("Invalid")


# In[3]:


ifsc_code = input("Enter any IFSC code ")
res_i = re.findall("^[A-Z]{4}0[A-Z 0-9]{6}$", ifsc_code)

print(res_i)


# In[ ]:




