#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=input("enter any character:")
if(n=="a"):
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))
    result=num1+num2
    print(result)
else:
    print("input is not matched")


# In[13]:


alpha=input("enter any character:")
if(alpha=="a" or alpha=="e" or alpha=="i" or alpha=="o" or alpha=="u" or alpha=="A" or alpha=="E" or alpha=="I" or alpha=="O" or alpha=="U"):
    print("Vowel")
else:
    print("consonant")


# In[24]:


char1=input("enter char:")
if(char1=="s"):
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))
    print("original positions:", num1,num2)
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    print("swapped positions are:", num1, num2)
else:
    print("input is not matched")


# In[ ]:




