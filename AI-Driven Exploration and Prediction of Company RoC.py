#!/usr/bin/env python
# coding: utf-8

# # Code

# ## Importing required libraries

# In[64]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## Loading the dataset.

# In[65]:


#Reading the dataset from CSV format.
df = pd.read_csv('/Users/sachinanandharaj/Downloads/Data_Gov_Tamil_Nadu.csv', low_memory=False)


# In[66]:


#Printing the given Dataset
df


# ## Preprocessing

# In[60]:


#Cleaning the dataset by removing the NA value rows from the dataset
df = df.dropna()


# In[61]:


#Printing the dataset
df


# ### Data Type Correction

# In[57]:


df['INDUSTRIAL_CLASS'].astype('int32')


# In[58]:


df['LATEST_YEAR_ANNUAL_RETURN'] = pd.to_datetime(df['LATEST_YEAR_ANNUAL_RETURN'])


# In[62]:


df['LATEST_YEAR_FINANCIAL_STATEMENT'] = pd.to_datetime(df['LATEST_YEAR_FINANCIAL_STATEMENT'])


# In[30]:


df['INDUSTRIAL_CLASS'] = df['INDUSTRIAL_CLASS'].astype('int32')


# In[63]:


df


# ## Exploratory Data Analysis

# In[40]:


sns.scatterplot(x='AUTHORIZED_CAP', y='PAIDUP_CAPITAL', data= ds)
plt.title('Scatterplot of Authorized Capital vs Paidup Capital')
plt.xlabel('Authorized Capital')
plt.ylabel('Paidup Capital')


# In[41]:


sns.set(style='whitegrid')  # Customize the plot style 
plt.figure(figsize=(10, 6))  # Set the figure size

# Create the count plot for the COMPANY_CATEGORY column
sns.countplot(x='COMPANY_CATEGORY', data=ds, palette='Set3')  # Adjust the color palette if needed

# Customize the plot (optional)
plt.title('Distribution of Company Categories')
plt.xlabel('Company Category')
plt.ylabel('Count')


# In[43]:



### Create the count plot for the COMPANY_SUB_CATEGORY column
sns.countplot(x='COMPANY_SUB_CATEGORY', data=ds, palette='Set3')  # Adjust the color palette if needed

### Customize the plot 
plt.title('Frequency of Company Subcategories')
plt.xlabel('Company Subcategory')
plt.ylabel('Count')


# In[44]:


sns.boxplot(data=ds, palette='Set2')

# Add a violin plot on top of the box plot for better visualization
sns.violinplot(data=ds, palette='Set3', inner=None)

# Customize the plot (optional)
plt.title('Comparison of Authorized Capital and Paid-up Capital')
plt.ylabel('Capital Value (in Rupees)')


# ## Saving the Preprocessed dataset

# In[16]:


df.to_csv('modified_dataset.csv', index=False)


# In[18]:


ds = pd.read_csv('modified_dataset.csv')

