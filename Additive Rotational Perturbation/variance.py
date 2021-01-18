#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import math


# In[13]:


ext1=open("iris.csv")
ext2=open("output.csv")
with open('iris.csv', 'r') as csv:
     first_line = csv.readline()
ncol = first_line.count(',') + 1
l1 = len(ext1.readlines())-1
l2=len(ext2.readlines())-1
abc=pd.read_csv("iris.csv", delimiter = ',')
abc2=pd.read_csv("output.csv", delimiter = ',')
d=abc.values.tolist()
d1=abc2.values.tolist()
dm=[]
dm1=[]
for i in range(0,l1):
    dm.append(0)
for i in range(0,l2):
    dm1.append(0)
dm_mean=[]
dm1_mean=[]
v1=[]
v2=[]
for i in range(0,ncol):
    dm_mean.append(0)
    dm1_mean.append(0)
    v1.append(0)
    v2.append(0)
for z in range(0,ncol):
    for i in range(0,l1):
        dm[i]=d[i][z]
    dm_mean[z]=sum(dm)/len(dm)
    for i in range(0,l2):
        dm1[i]=d1[i][z]
    dm1_mean[z]=sum(dm1)/len(dm1)
print("Mean :")
print("Original Dataset : " ,dm_mean)
print("Modified Dataset : " ,dm1_mean)
print("\nVariance :")
sum1=0
sum2=0
for z in range(0,ncol):
    for i in range(0,l1):
        sum1=sum1+((d[i][z]-dm_mean[z])**2)
    v1[z]=sum1/(l1-1)
    for i in range(0,l2):
        sum2=sum2+((d1[i][z]-dm1_mean[z])**2)
    v2[z]=sum2/(l2-1)
print("Original Dataset : " ,v1)
print("Modified Dataset : " ,v2)


# In[ ]:





# In[ ]:




