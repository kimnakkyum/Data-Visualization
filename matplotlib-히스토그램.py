#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib as mpl
import matplotlib as plt
from matplotlib import pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


np.random.seed(0)

mu = 72
sigma = 8
X = np.random.normal(mu, sigma, 10000)

plt.hist(X, rwidth=0.9, bins=16)
# bins는 전체 계급 구간이 16이라는 의미


# In[3]:


from seaborn import load_dataset
tips = load_dataset("tips")
tips.info()


# In[4]:


plt.hist(x = tips.tip, rwidth=0.9, bins = 20)
plt.title("tips")
plt.xlabel("tip")
plt.ylabel("frequency")


# In[5]:


import scipy as sp

bins = 20
plt.hist(x = tips.tip, rwidth=0.9, bins = bins, density=True)
plt.title("tips")
plt.xlabel("tip")
plt.ylabel("density")

mu, sigma = tips.tip.mean(), tips.tip.std()
tip_min = tips.tip.min()
tip_max = tips.tip.max()
x = np.linspace(tip_min, tip_max, bins)
y = sp.stats.norm(mu, sigma).pdf(x)
plt.plot(x, y)

