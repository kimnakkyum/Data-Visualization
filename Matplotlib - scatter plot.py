#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris
iris = load_iris()
iris


# In[2]:


# dict 형태의 데이터를 보기 좋게 만들기 위해 데이터 프레임 타입으로 변환합니다.
import pandas as pd

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['class'] = iris.target

df.tail()


# In[3]:


#scatter plot


# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[6]:


plt.scatter(df['sepal length (cm)'],df['sepal width (cm)'])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




