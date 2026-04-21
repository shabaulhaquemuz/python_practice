#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 🟢 LEVEL 1: Core Basics (Must be instant)
# 1.Create a dictionary of numbers → squares (1–10)
squares={i:i*i for i in range(1,11)}
print(squares)


# In[4]:


triple={i:i*i for i in range(1,11)}
print(triple)


# In[6]:


quad={i:i*i*i for i in range(1,10)}
print(quad)


# In[12]:


#2.Access value safely using get()
#With .get() you always use a key, not a value.
print(squares.get(5))
print(squares.get(2))
print(squares.get(10))
print(squares.get(15))


# In[14]:


# 3. Add a key
squares[15]=225
print(squares)


# In[15]:


#4. Update a key
squares[15]=333
print(squares)


# In[20]:


#5. Delete a key
a=squares.pop(2)
print(a)


# In[25]:


#delete a key
del squares[5]


# In[26]:


print(squares)
#see 2 and 5 are deleted


# In[29]:


# 5. Check if key exists
if 5 in squares:
    print("key exists")
else:
    print("key doesnt exist")


# In[30]:


if 6 in squares:
    print("key exist")
else:
    print("key doesnt exist")


# In[31]:


#6. Iterate over dictionary
#a.over keys
for k in squares.keys():
    print(k)


# In[32]:


#b.iterate over values
for v in squares.values():
    print(v)


# In[37]:


#c.iterate over Key-Value pairs
for i,j in squares.items():
    print(i,j)


# In[38]:


#manually create a dictionary
students={
    "name" :"Shabaul Haque",
    "Age"  :24,
    "Marks":99,
    "City" :"Muzaffarpur"
}


# In[39]:


print(students)


# In[40]:


#7. Count frequency of elements in a list
numbers = [1, 2, 2, 3, 4, 1, 2, 3, 5, 1, 6, 2, 3]
d={}
for i in numbers:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)


# In[41]:


#8.Merge two dictionaries
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 200, "d": 40, "e": 50}
dict3={}
for i in dict1:
    dict3[i]=dict1[i]
for j in dict2:
    dict3[j]=dict2[j]
print(dict3)



# In[42]:


# 3. Find Maximum Value in dictionary
marks = {"Rahul": 85, "Aman": 92, "Neha": 88, "Sara": 95}
maxx=0
for i in marks.values():
    if(i>maxx):
        maxx=i
print(maxx)


# In[44]:


#Find keys with maximum value
marks = {"Rahul": 85, "Aman": 92, "Neha": 88, "Sara": 95}
max_value=0
max_key=None
for key,value in marks.items():
    if(value>max_value):
        max_value=value
        max_key=key
print(max_key,max_value)


# In[47]:


#4. Sort Dictionary by Values


# In[50]:


# 5. Convert Two Lists into Dictionary
keys = ["name", "age", "city"]
values = ["Ali", 22, "Mumbai"]
dict1={}
for i in range(len(keys)):
    dict1[keys[i]]=values[i]
print(dict1)


# In[51]:


#create dictionay comprehension:
d={i:i*i for i in range(1,11)}
print(d)


# In[52]:


#7. Filter Dictionary (value > 10)
data = {"a": 5, "b": 15, "c": 8, "d": 20, "e": 3}
for key,value in data.items():
    if(value>10):
        print(key,value)


# In[53]:


#7. Filter Dictionary (value > 10). give output in dictionary format only
data = {"a": 5, "b": 15, "c": 8, "d": 20, "e": 3}
filtered={}
for key,value in data.items():
    if(value>10):
        filtered[key]=value
print(filtered)


# In[57]:


# Create nested dictionary
# 👉 student → marks, subjects
student={
    "Shabaul":{
        "marks":99,
        "subject":"maths"
    },
    "Saif":{
        "marks":90,
        "subject":"science"
    }
}
print(student)


# In[58]:


student = {
    "Ali": {
        "marks": 85,
        "subjects": ["Math", "Science"]
    },
    "Sara": {
        "marks": 92,
        "subjects": ["English", "History"]
    }
}

print(student)


# In[ ]:




