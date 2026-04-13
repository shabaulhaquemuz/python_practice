#!/usr/bin/env python
# coding: utf-8

# In[25]:


mylist=[0,1,0,2,-1,0,3]
# output=[1,2,-1,3,0,0,0]
newlist=[]
for i in range(len(mylist)):
    if(mylist[i]!=0):
        newlist.append(mylist[i])
count=0
for i in range(len(mylist)):
    if(mylist[i]==0):
        count+=1
        newlist.append(mylist[i])

print(newlist)
print(count)


# In[ ]:





# In[ ]:




