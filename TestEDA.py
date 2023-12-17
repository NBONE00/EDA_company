#!/usr/bin/env python
# coding: utf-8

# In[216]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import math 
import missingno as msno
import numpy as np 
from IPython.display import display
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# In[ ]:





# In[217]:


df_cust = pd.read_csv("/Users/noahbonekamp/Desktop/kunden.csv", sep=";")
df_vis = pd.read_csv("/Users/noahbonekamp/Desktop/besucher.csv", sep=";")
df_geo = pd.read_csv("/Users/noahbonekamp/Desktop/geo_test.csv", delimiter=";")


# In[218]:


df_geo['Niederlassung']= df_geo['Niederlassung'].astype(str)
df_geo['Niederlassung'] = df_geo['Niederlassung'].str.title()
mapping = {
    'Berlin-Mitte': 'Berlin',
    'Berlin-Charlottenburg': 'Berlin',
    'Nrw': 'Nordrein-Westfalen',
    'Düsseldorf': 'Nordrein-Westfalen'
}
df_geo['Niederlassung'] = df_geo['Niederlassung'].replace(mapping, regex=True)


# In[219]:


uniques = list(df_geo['Niederlassung'].unique())
print(uniques)
print(df_geo['Niederlassung'].nunique())


# In[220]:


cust_m = pd.merge(df_cust, df_geo, how='left', on='KundeNr')
vis_m = pd.merge(df_vis, df_geo, how='left', on='KundeNr')


# In[221]:


cust_m.info()


# In[222]:


cust_m.head(5)


# In[ ]:





# In[223]:


cust_m.set_index('KundeNr', inplace=True)
vis_m.set_index('KundeNr', inplace=True)


# In[224]:


cust_m.describe().T


# In[225]:


vis_m.describe().T


# In[226]:


cust_m.index.nunique()


# In[227]:


vis_m.index.nunique()


# In[228]:


mean_v = cust_m['Preis'].mean()
max_v = cust_m['Preis'].max()
min_v = cust_m['Preis'].min()
Total = cust_m['Preis'].sum()

mean_values = round(mean_v, 2)
max_values = round(max_v, 2)
min_values = round(min_v,2)
total_value = round(Total, 2)

table = pd.DataFrame({
    'Durchschnitt': ['{:,.2f}€'.format(mean_values)],
    'Maximaler Preis': ['{:,.2f}€'.format(max_values)],
    'Minimaler Preis': ['{:,.2f}€'.format(min_values)], 
    'Gesamtumsatz': ['{:,.2f}€'.format(total_value)]
})
display(table)


# In[229]:


var = cust_m['Niederlassung'].value_counts()
mean_value = var.mean()

var2= cust_m.groupby('Niederlassung')['Preis'].agg('mean')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10, 4))
ax1.bar(var.index, var.values, color='blue')
ax1.set_ylabel('Verkaufte Autos')
ax1.set_title('Verkaufte Autos je Bundesland')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
ax1.axhline(y=mean_value, color='red', linestyle='-')

ax2.bar(var2.index, var2.values, color='skyblue')
ax2.set_ylabel('Durchschnittlicher Preis') 
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
ax2.set_title('Durchschnittlicher Preis je Bundesland')

plt.show()


# In[230]:


var = cust_m['Geschlecht'].value_counts()

var.plot(kind='bar', rot=45, color=['red', 'blue'],)
plt.xlabel('Geschlecht')
plt.ylabel('Anzahl verkaufter Fzg.')
plt.title('Gegenüberstellung Geschlecht')
plt.xticks([0,1],['Männlich', 'Weiblich'], rotation=45)
#to not show the following message: matplotlib.legend.Legend at 0x139a53ad0>
plt.legend().set_visible(False)


# In[267]:


mean_cust = cust_m['Alter'].mean()
mean_vis = vis_m['Alter'].mean()
cust_m['Alter'] = pd.to_numeric(cust_m['Alter'])
age_cust_m_mean = cust_m.groupby('Geschlecht')['Alter'].mean()
cust_m['Einkommen'] = pd.to_numeric(cust_m['Einkommen'], errors = 'coerce')
#Hier gibt es einen großen Outlier von 1,000,000,000.0€
threshold = cust_m['Einkommen'].quantile(0.95)
filtered_cust_m = cust_m[cust_m['Einkommen'] <= threshold]
mean_cust_Einkommen = filtered_cust_m['Einkommen'].mean()

table = pd.DataFrame({
    'Durschnittliches Alter Kunden': [round(mean_cust, 2)], 
    'Durschnittliches Alter Visitors': [round(mean_vis, 2)], 
    'Durchschnittliches Alter männlich (Kunden)': ['50.34'],
    'Durchschnittliches Alter weiblich (Kunden)': ['50.52'], 
    'Durchschnittliches Einkommen Kunden': ['{:,.2f}€'.format(mean_cust_Einkommen)] 
})
display(table.T)
    


# In[254]:


plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Korrelation Heatmap')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




