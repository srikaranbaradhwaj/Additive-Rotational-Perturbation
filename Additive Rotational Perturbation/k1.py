#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import math

def rotate90Clockwise(A,N): 
    for i in range(N//2): 
        for j in range(i, N-i-1): 
            temp = A[i][j] 
            A[i][j] = A[N - 1 - j][i] 
            A[N-1-j][i] = A[N-1-i][N-1-j] 
            A[N-1-i][N-1-j] = A[j][N-1-i] 
            A[j][N-1-i] = temp 
  
 
def printMatrix(A): 
    N = len(A[0]) 
    for i in range(N): 
        print(A[i])


# In[12]:


ext_file=open("d1.csv")
with open("d1.csv", 'r') as csv:
     first_line = csv.readline()
     your_data = csv.readlines()
ncol = first_line.count(',') + 1
l = len(ext_file.readlines())-1
s=int(math.ceil(math.sqrt(l)))
t=s*s
print(l,s,t)
abc = pd.DataFrame(np.zeros((t, ncol)))
abc2=abc
abc=pd.read_csv("d1.csv", delimiter = ',')
for m in range(l,t):
    abc = abc.append(pd.Series(0, index=abc.columns), ignore_index=True)
abc3=abc
print(abc)
d=abc.values.tolist()
dm=[]
for i in range(0,t):
    dm.append(0)
for z in range(0,ncol):
    for i in range(0,t):
        dm[i]=d[i][z]
    mat=np.reshape(dm,(s,s))
    mat1=mat
    print(mat1)
    for i in range(2,s+1):
        rotate90Clockwise(mat1,i)
#     print('\n')
#     printMatrix(mat1)
#     print('\n')
    mat2=np.reshape(mat1,(1,t))
    mat2=mat2.flatten()
    b=mat2.tolist()
    for i in range(0,t-1):
        b[i]=float(b[i])+float(b[i+1])
        b[t-1]=float(b[t-1])
    print(b)
    for k in range(0,t):
        abc.iloc[k][z]=b[k]
    print(abc)
abc.to_csv('output.csv',index=False)


# In[ ]:





# In[ ]:




