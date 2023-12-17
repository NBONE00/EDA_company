#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import math 
import missingno as msno
import numpy as np 


# In[32]:


df_cust = pd.read_csv("/Users/noahbonekamp/Desktop/kunden.csv", sep=";")
df_vis = pd.read_csv("/Users/noahbonekamp/Desktop/besucher.csv", sep=";")
df_geo = pd.read_csv("/Users/noahbonekamp/Desktop/geo_test.csv", delimiter=";")


# In[33]:


df_geo['Niederlassung']= df_geo['Niederlassung'].astype(str)
df_geo['Niederlassung'] = df_geo['Niederlassung'].str.title()
mapping = {
    'Berlin-Mitte': 'Berlin',
    'Berlin-Charlottenburg': 'Berlin',
    'Nrw': 'Nordrein-Westfalen',
    'Düsseldorf': 'Nordrein-Westfalen'
}
df_geo['Niederlassung'] = df_geo['Niederlassung'].replace(mapping, regex=True)


# In[34]:


uniques = list(df_geo['Niederlassung'].unique())
print(uniques)
print(df_geo['Niederlassung'].nunique())


# In[35]:


cust_m = pd.merge(df_cust, df_geo, how='left', on='KundeNr')
vis_m = pd.merge(df_vis, df_geo, how='left', on='KundeNr')


# In[36]:


cust_m.describe().T


# In[37]:


vis_m.describe().T


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




