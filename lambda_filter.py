#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Square a Number
# Write a lambda function to return the square of a number.
# Example:
# Input: 5
# Output: 25
square=lambda x:x**2
print(square(5))


# In[6]:


# Add Two Numbers
# Create a lambda function that adds two numbers.

# Example:
# Input: 3, 7
# Output: 10
two=lambda x,y:x+y
print(two(3,7))


# In[7]:


# Check Even or Odd
# Write a lambda function to check if a number is even.

# Example:
# Input: 8
# Output: True
even=lambda x:x%2==0
print(even(8))


# In[10]:


# Find Maximum of Two Numbers
# Create a lambda function that returns the greater number.

# Example:
# Input: 10, 15
# Output: 15
maxx=lambda x,y: x if(x>y) else y
print(maxx(3,4))


# In[11]:


# Question:
# Write a lambda function to find the cube of a number.

# Example:
# Input: 3
# Output: 27
cube=lambda x:x**3
print(cube(9))


# In[13]:


# Filter Even Numbers
# Use filter() with lambda to get even numbers from a list.

# Example:
# Input: [1,2,3,4,5,6]
# Output: [2,4,6]
nums=[1,2,3,4,5,6]
mylist=list(filter(lambda x:x%2==0, nums))
print(mylist)


# In[14]:


# Filter Odd Numbers
# Use filter() with lambda to get odd numbers from a list.

# Example:
# Input: [1,2,3,4,5,6]
# Output: [1,3,5]
nums=[1,2,3,4,5,6]
odd=list(filter(lambda x:x%2!=0,nums))
print(odd)


# In[15]:


# Filter Names Starting with 'A'
# Use filter() with lambda to find names starting with letter A.

# Example:
# Input: ["Ali","Ahmed","Sara","John"]
# Output: ['Ali', 'Ahmed']
names=["Ali","Ahmed","Sara","John"]
names = ["Ali","Ahmed","Sara","John"]

result = list(filter(lambda x: x.startswith("A"), names))

print(result)


# In[16]:


# Filter Numbers Greater Than 10
# Use filter() with lambda to get numbers greater than 10.

# Example:
# Input: [5,12,7,20,3,15]
# Output: [12,20,15]
nums=[5,12,7,20,3,15]
ten=list(filter(lambda x:x>10, nums))
print(ten)


# In[17]:


# Filter Strings with Length More Than 4
# Use filter() with lambda to find strings whose length is greater than 4.

# Example:
# Input: ["apple","bat","mango","cat"]
# Output: ['apple', 'mango']
strings= ["apple","bat","mango","cat"]
length=list(filter(lambda x: len(x)>4, strings))
print(length)


# In[ ]:




