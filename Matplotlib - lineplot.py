#!/usr/bin/env python
# coding: utf-8

# In[1]:


#두가지 방법으로 matpltlib그리기 


# In[2]:


import matplotlib as mpl
import matplotlib as plt
from matplotlib import pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# plt를 이용하는 방법


# In[4]:


import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x), "-", linewidth=1, label="sin(x)")
plt.plot(x, np.cos(x), "--", linewidth=1, label="cos(x)")
plt.xlim(0, 10)
plt.ylim(-1, 1)
plt.title("Sine & Cosine Curve")
plt.xlabel("x")
plt.legend()


# In[5]:


#스타일 바꾸기 (with구문)


# In[6]:


with plt.style.context("ggplot"):
    plt.plot(x, np.sin(x), "-", linewidth=1, label="sin(x)")
    plt.plot(x, np.cos(x), "--", linewidth=1, label="cos(x)")
    plt.xlim(0, 10)
    plt.ylim(-1, 1)
    plt.title("Sine & Cosine Curve")
    plt.xlabel("x")
    plt.legend()


# In[7]:


# ax, figure를 이용하는 방법


# In[8]:


fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 100)

ax.plot(x, np.sin(x), "-", linewidth=1, label="sin(x)")
ax.plot(x, np.cos(x), "--", linewidth=1, label="cos(x)")
ax.set_xlim([0, 10])
ax.set_ylim([-1, 1])
ax.set_title("Sine & Cosine Curve")
ax.set_xlabel("x")
ax.legend()


# In[9]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(x, np.sin(x), 'b-', linewidth=0.5, label="sin(x)")
ax[0].set_title("Sine & Cosine Curve")
ax[0].set(xlim=[0, 10], ylim=[-1, 1])
ax[0].legend()

ax[1].plot(x, np.cos(x), 'g-', linewidth=0.5, label="cos(x)")
ax[1].set(xlim=[0, 10], ylim=[-1, 1], xlabel="x")
ax[1].legend()


# In[10]:


plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x), 'b-', linewidth=0.5, label="sin(x)")
plt.title("Sine & Cosine Curve")
plt.axis([0, 10, -1, 1])
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), 'g-', linewidth=0.5, label="cos(x)")
plt.xlabel("x")
plt.axis([0, 10, -1, 1])
plt.legend()


# In[11]:


# equal을 쓰면 x축과 y축의 범위가 동일해짐


# In[12]:


plt.plot(x, np.sin(x), "-", linewidth=1)
plt.title("Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.margins(0, 0)
plt.axis("equal")

