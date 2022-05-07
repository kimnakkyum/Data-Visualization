#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.datasets import load_iris
iris = load_iris()
iris


# In[3]:


# dict 형태의 데이터를 보기 좋게 만들기 위해 데이터 프레임 타입으로 변환합니다.
import pandas as pd

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['class'] = iris.target

df.tail()


# In[7]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


# class가 0과 1 사이의 상관계수 분석하기


# In[10]:


np.unique(df["class"], return_counts = True)


# In[14]:


df_0 = df[df["class"] == 0] 


# In[15]:


df_1 = df[df["class"] == 1] 


# In[18]:


df_01 = pd.concat([df_0, df_1])


# In[21]:


df_01


# In[24]:


df_corr = df_01.corr()
df_corr


# In[ ]:


#히트맵


# In[28]:


colormap = plt.cm.PuBu 
plt.figure(figsize=(10, 8)) 
plt.title("Person Correlation of Features", y = 1.05, size = 15) 
sns.heatmap(df_corr, linewidths = 0.1, vmax = 1.0, 
            square = True, cmap = colormap, linecolor = "white", annot = True, annot_kws = {"size" : 16})


# In[ ]:


# 히트맵 반쪽짜리


# In[26]:


fig, ax = plt.subplots( figsize=(7,7) )

# 삼각형 마스크를 만든다(위 쪽 삼각형에 True, 아래 삼각형에 False)
mask = np.zeros_like(df_corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# 히트맵을 그린다
sns.heatmap(df_corr, 
            cmap = 'RdYlBu_r', 
            annot = True,   # 실제 값을 표시한다
            mask=mask,      # 표시하지 않을 마스크 부분을 지정한다
            linewidths=.5,  # 경계면 실선으로 구분하기
            cbar_kws={"shrink": .5},# 컬러바 크기 절반으로 줄이기
            vmin = -1,vmax = 1   # 컬러바 범위 -1 ~ 1
           )  
plt.show()

