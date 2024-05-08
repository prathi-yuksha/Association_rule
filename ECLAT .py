#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyECLAT


# In[2]:


from pyECLAT import Example2


# In[3]:


data = Example2().get()


# In[5]:


data.head()


# In[6]:


from pyECLAT import ECLAT


# In[7]:


e = ECLAT(data=data)
e.df_bin #binary values


# In[10]:


items = e.df_bin.astype(int).sum(axis=0)
items


# In[13]:


transaction = e.df_bin.astype(int).sum(axis=1)
transaction


# In[16]:


import pandas as pd

data = pd.DataFrame({"items":items,"transaction":transaction})
data.sort_values("transaction",ascending=False)
data.style.background_gradient(cmap='PuBu')


# In[ ]:




