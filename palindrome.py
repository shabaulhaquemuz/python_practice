#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=input("enter the Text:")
length=len(n)
start=0
count=0
end=len(n)-1
for i in range(length//2):
    if(n[start]!=n[end]):
        count=1
        break
    else:
        start+=1
        end-=1
if(count==0):
    print("Palindrome")
else:
    print("Not a Palindrome")


# In[ ]:




