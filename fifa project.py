#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import seaborn as sns


# In[4]:


from matplotlib import pyplot as plt


# In[7]:


fifa=pd.read_csv('players_20.csv')


# In[8]:


fifa.head()


# In[9]:


#check columns 
for col in fifa.columns:
    print(col)


# In[11]:


fifa.tail()


# In[12]:


fifa.shape


# In[13]:


fifa.describe()


# In[14]:


fifa['nationality'].value_counts()


# In[15]:


fifa['nationality'].value_counts()[0:10]


# In[16]:


fifa['nationality'].value_counts()[0:10].keys()


# In[ ]:





# In[24]:


list(fifa['nationality'].value_counts()[0:5])


# In[25]:


plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color='g')
plt.xlabel('countries')
plt.ylabel('number of players')
plt.title('Nationality')
plt.show()


# In[26]:


players_salary=fifa[['short_name','wage_eur']]


# In[27]:


players_salary.head()


# In[28]:


players_salary=players_salary.sort_values(by=['wage_eur'],ascending=False)


# In[29]:


players_salary.head()


# In[34]:


plt.figure(figsize=(9,5))
plt.bar(list(players_salary['short_name'])[0:5],list(players_salary['wage_eur'])[0:5],color=('green','blue','orange','pink','black'))
plt.show()


# In[36]:


#finding nationality argentina or not
fifa['nationality']=='Argentina'


# In[37]:


Argentina=fifa[fifa['nationality']=='Argentina']


# In[39]:


Argentina.head(10)


# In[41]:


Argentina.sort_values(by=['height_cm'],ascending=False).head()


# In[42]:


Argentina.sort_values(by=['weight_kg'],ascending=False).head()


# In[44]:


Argentina.sort_values(by=['wage_eur'],ascending=False).head()


# In[47]:


Argentina[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head()


# In[48]:


#shooting

players_shooting=fifa[['short_name','shooting']]


# In[49]:


players_shooting.sort_values(by=['shooting'],ascending=False).head()


# In[52]:


#defending
players_defending=fifa[['short_name','defending','nationality','club']]


# In[53]:


players_defending.sort_values(by=['defending'],ascending=False).head()


# In[54]:


#extract real madrid players
mufc=fifa[fifa['club']=='Manchester United']


# In[56]:


mufc.sort_values(by=['shooting'],ascending=False).head()


# In[57]:


mufc.sort_values(by=['defending'],ascending=False).head()


# In[58]:


mufc.sort_values(by=['wage_eur'],ascending=False).head()


# In[59]:


mufc['nationality'].value_counts()


# In[ ]:




