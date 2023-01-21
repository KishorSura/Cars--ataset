#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np


# In[5]:

#importing csv_file
df=pd.read_csv("C:/Users/DELL/Downloads/2. Cars Data1.csv")


# In[6]:

#first five rows
df.head()


# In[7]:

#number of rows and columns
df.shape


# In[8]:


#fill the null values with mean of the respective column
df.isnull().sum()


# In[9]:


#lets drop
new_df1=df.dropna(how="all")


# In[10]:


new_df1.isnull().sum()


# In[11]:


#next fill the null values with mean
df1=new_df1.fillna({"Cylinders":new_df1.Cylinders.mean()})
df1


# In[12]:


df1.isnull().sum()


# In[13]:


#2 Check oyt different types of dataset and count the occurrence 
df1.head(2)


# In[14]:


df1["Make"].value_counts()


# In[15]:


#show all the records of origin where condition is Asia or Europe 
df1.head()


# In[16]:


df1[(df1["Origin"]=="Asia")|(df1["Origin"]=="Europe")]


# In[17]:


df1[df1["Origin"].isin(["Asia","Europe"])]


# In[18]:


#remove all records where weight is above 4000
df1[~(df1["Weight"]>4000)]


# In[19]:


#increase the value of  coulmn "MPG_Highway" by 3
df1["MPG_City"]=df1["MPG_City"].apply(lambda x:x+3)


# In[20]:


df1


# In[36]:


#graphical representation of count of make

a=df1["Make"].value_counts()

