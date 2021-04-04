#!/usr/bin/env python
# coding: utf-8

# # US Population Analysis

# In[1]:


import pandas as pd
import numpy as np
import folium as fo


# In[2]:


data = pd.read_csv('us_citi_population.csv')


# In[3]:


data.head(10)


# In[5]:


data.describe()


# In[4]:


lat = data['lat']
lon = data['lon']
name = data['name']
pop = data['pop']


# In[6]:


def colorful_markers(popu):
    if popu > 35000:
        return 'red'
    elif 10000<popu<35000:
        return 'blue'
    else:
        return 'green'
    


# In[7]:


map = fo.Map()


# In[8]:


map


# In[10]:


population = fo.FeatureGroup(name='US POPULATION')


# In[11]:


for lat,lon,name,pop in zip(lat,lon,name,pop):
    population.add_child(fo.Marker(location=[lat,lon],
                                  popup=[name,pop],
                                  icon=fo.Icon(color=colorful_markers(pop))))


# In[12]:


map.add_child(population)


# In[ ]:




