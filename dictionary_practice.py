#!/usr/bin/env python
# coding: utf-8

# In[1]:


#👉 Count frequency of elements in a list
mylist= [1,2,2,3,3,3]
d={}
for i in mylist:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)


# In[2]:


#👉 Store frequency of each character
s="aabcc"
d1={}
for i in s:
    if(i not in d1):
        d1[i]=1
    else:
        d1[i]=d1[i]+1
print(d1)


# In[3]:


#3. Find Key with Maximum Value
m={'a':10, 'b':20, 'c':15}
max_char=0
max_count=0
for i in m:
    if(m[i]>max_count):
        max_count=m[i]
        max_char=i
print(max_char)
print(max_count)


# In[5]:


#4. Merge Two Dictionaries
d1 = {'a':1, 'b':2}
d2 = {'b':3, 'c':4}
d3={}
for i in d1:
    d3[i]=d1[i]
for j in d2:
    d3[j]=d2[j]
print(d3)


# In[9]:


#5. Remove Duplicates Using Dictionary
mylist=[1,2,2,3,4,4]
d5={}
new=[]
for i in mylist:
    if(i not in d5):
        d5[i]=i
print(d5)
for i in d5:
    new.append(d5[i])
print(new)


# In[ ]:




