#!/usr/bin/env python
# coding: utf-8

# # Assignment - 2
# Import the necessary libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plot
import imageio


# In[13]:


url='https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
df = pd.read_csv(url_csv, sep = "|")
df


# # Assign it to a variable called users and use the 'user_id' as index

# In[14]:


users =pd.read_csv(url_csv, sep="|", index_col="user_id")
users


# # See the first 10 and last 10 entries

# In[16]:


df.head(10)


# In[17]:


df.tail(10)


# # What is the number of observations in the dataset?

# In[31]:


df.count()[0]


# # What is the number of columns in the dataset?

# In[38]:


len(df.columns)
#df.columns


# # Print the name of all the columns

# In[42]:


df.columns.tolist()


# # How is the dataset indexed?

# In[49]:


df.index


# # What is the data type of each column?

# In[56]:


df.info()

Print only the occupation column
# In[64]:


users =pd.read_csv(url_csv, sep="|", index_col="user_id")
df['occupation']


How many different occupations are in this dataset?
# In[65]:



users["occupation"].value_counts().head(1)

DataFrame Info
# In[66]:


df.info()


# In[67]:


#describing all the columns
users.describe()


# In[68]:


#summarize onlyn ocupational column
users["occupation"].value_counts()


# In[ ]:


#What is the mean age of users?
#What is the age with least occurence?


# In[69]:


users.age.mean()


# In[70]:


users.age.value_counts().tail()

