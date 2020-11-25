#!/usr/bin/env python
# coding: utf-8

# In[1]:


def CountSize(a , b):
    counter = 0
    if len(a) == len(b):
        for i in range (len(a)):
            if a[i] != b[i]:
                counter += 1
        print(counter)
    else: print("wrong size")


# In[2]:


CountSize("AAAA" , "AAAT")
CountSize("AAAA" , "CCCT")
CountSize("AAAA" , "AAAA")


# In[ ]:




