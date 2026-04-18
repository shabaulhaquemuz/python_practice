#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Get the first 4 characters
# 👉 Expected: "Data"
s = "DataScienceIsAwesome"
s[0:4]


# In[26]:


# Get the last 7 characters
# 👉 Expected1: "emosewA"
#Expected2: "Awesome"
s = "DataScienceIsAwesome"
print(s[-1:-8:-1])
print(s[13:])
print(s[-7:])


# In[27]:


#Extract "Science" from the string
s = "DataScienceIsAwesome"
s[4:11]


# In[28]:


#Reverse the entire string
s = "DataScienceIsAwesome"
s[::-1]


# In[30]:


#Get every 2nd character from the string
s = "DataScienceIsAwesome"
s[::2]


# In[31]:


#Get characters from index 4 to 11
s = "DataScienceIsAwesome"
s[4:12]


# In[34]:


#Get the string except the first and last character
s = "DataScienceIsAwesome"
s[1:-1]


# In[38]:


#Reverse only "Science" part from the string
s = "DataScienceIsAwesome"
print(s[10:3:-1])
print(s[4:11][::-1]) #better way


# In[39]:


#Get characters from index -10 to -1
s = "DataScienceIsAwesome"
s[-10:]


# In[40]:


#Get every 3rd character starting from index 1
s = "DataScienceIsAwesome"
s[1::3]


# In[41]:


#Reverse the string but skip every 2nd character (tricky!)
s = "DataScienceIsAwesome"
s[::-2]


# In[ ]:




