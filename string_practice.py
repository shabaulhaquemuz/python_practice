#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter first number:"))
m=int(input("enter 2nd number:"))
LCM=1
a,b=m,n
for i in range(2,max(a,b)+1):
    while(b%i==0 or a%i==0):
        LCM*=i
        if(b%i==0):
            b=b//i
        if(a%i==0):
            a=a//i
print(LCM)



# In[10]:


# 5. Reverse a String

# 👉 Without using slicing ([::-1])
string="shabaul"
print(string[::-1])
new=""
for ch in string:
    new=ch+new
print(new)


# In[11]:


s="saif"
rev=""
for ch in s:
    rev=ch+rev
print(rev)


# In[12]:


# Count vowels in a string
# 👉 input: "education" → output: 5
string="education"
count=0
for i in string:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
print(count)



# In[19]:


# Check if a string is a palindrome
# 👉 "madam" → True
n=input("enter the string:")
start=0
end=len(n)-1
count=0
for i in range(len(n)//2):
    if(n[start]!=n[end]):
        count=1
        break
    start+=1
    end-=1
if(count==0):
    print("palindrome")
else:
    print("not a palindrome")


# In[21]:


# Count frequency of each character
s="shabaul"
dict1={}
for i in s:
    if(i not in dict1):
        dict1[i]=1
    else:
        dict1[i]=dict1[i]+1
print(dict1) 


# In[22]:


# Remove all spaces from a string
# 👉 "hello world" → "helloworld"
s="hello world"
n=""
for i in s:
    if(i!=" "):
        n=n+i
print(n)


# In[27]:


# Find the first non-repeating character
# 👉 "aabbcde" → c
s="aabbcde"
for i in range(len(s)):
    count=0
    for j in range(len(s)):
        if(s[i]==s[j]):
            count+=1
    if(count==1):
        print(s[i])
        break


# In[37]:


# Check if two strings are anagrams
# 👉 "listen" & "silent" → True
str1="listen"
str2="silent"
dict1={}
dict2={}
for i in str1:
    if(i in dict1):
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
for j in str2:
    if(j in dict2):
        dict2[j]=dict2[j]+1
    else:
        dict2[j]=1
print(dict1==dict2)


# In[43]:


# Replace all vowels with *
# 👉 "hello" → "h*ll*"
s="hello"
h=""
for i in s:
    if i in "aeiou":
        h=h+"*"
    else:
        h=h+i
print(h)


# In[47]:


# 10.

# Find the longest word in a sentence
# 👉 "I love programming" → "programming"
s="I love programming"
a=s.split(" ")
longest=a[0]
for i in a:
    if(len(i)>len(longest)):
        longest=i   
print(a)
print(longest)


# In[50]:


# Capitalize the first letter of each word without using .title()
# "i love programming"
s="i love programming"
a=s.split(" ")
result=""
for i in a:
    result=result+i[0].upper()+i[1:]+" "
print(result)



# In[51]:


# 11.# Remove duplicate characters
# 👉 "programming" → "progamin"
s="programming"
d=""
for i in s:
    if(i not in d):
        d=d+i
print(d)


# In[54]:


# 13.

# Check if a string contains only digits
s="765432h"
h="1234567890"
count=0
for i in s:
    if(i not in h):
        count=1
        break
if(count==0):
    print("only numbers")
else:
    print("not only numbers, but characters also")



# In[60]:


# 15.
# Find the most frequent character
s="hellomynameisshabaull"
d={}
for i in s:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
#Finding max frequent
max_char=0
max_count=0
for key in d:
    if(d[key]>max_count):
        max_count=d[key]
        max_char=key
print(max_char)
print(max_count)


# In[ ]:




