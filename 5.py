#!/usr/bin/env python
# coding: utf-8

# In[28]:


import os


# In[34]:


def CountSize(a):
    dirs = os.listdir(a)
    size = 0 
    for file in dirs:
        size += os.path.getsize(a)
    print(size)


# In[37]:


CountSize('C:\\Users\Acer\Desktop\projects')

