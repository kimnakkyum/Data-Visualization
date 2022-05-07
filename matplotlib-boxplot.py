#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib as mpl
import matplotlib as plt
from matplotlib import pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from seaborn import load_dataset
tips = load_dataset("tips")


# In[3]:


tips.info()


# In[4]:


# 남성인 사람일때 tip을 describe를 하는데 소숫점 첫째자리까지


# In[5]:


tips.loc[tips.sex =="Male", "tip"].describe().round(1)


# In[6]:


tips.loc[tips.sex =="Female", "tip"].describe().round(1)


# In[7]:


labels = []
tip_list = []

for label, df_per_sex in tips.groupby("sex"):
    labels.append(label)
    tip_list.append(df_per_sex["tip"].tolist())
# 남성과 여성의 tip을 리스트로 표현하기 [[,]] --> 남자 tip 쫙 그 다음 여자 tip 쫙 
    
    
plt.boxplot(tip_list, labels=labels)
plt.title("tips")
plt.xlabel("sex")
plt.ylabel("tips")


# In[8]:


# IQR = Q3 - Q1
# Lower1.5*IQR whisker = Q1-1.5 * IQR
# Upper1.5*IQR whisker = Q1+1.5 * IQR

