#!/usr/bin/env python
# coding: utf-8

# In[8]:


# ✅ Section 1: Basics of Functions (Q1–5)
# 1.Write a function that prints "Hello, World!". Call it twice.
def greet():
    print("Hello, World!")
greet()
greet()


# In[10]:


# 2.Create a function that takes two numbers as parameters and returns their sum.
def summation(a,b):
    return a+b
print(summation(2,3))


# In[12]:


# 3.Write a function with a default argument that greets a user.
# Default argument means giving a predefined value to a parameter in a function, so if no argument is passed,
# that default value is used.
def greeting(wish="Hey Good Morning"):
    return wish
print(greeting())


# In[13]:


# 4.Write a function that returns the square of a number.
def squarenum(a):
    return a**2
print(squarenum(2))


# In[15]:


# 5.Create a function that accepts no arguments and returns your name as a string.
def myname():
    return "Shabaul Haque"
print(myname())


# In[24]:


#Q6. Write a function that takes a name and age as positional arguments and prints:
def nameage(name,age):
    return f"Name:{name},AGE:{age}"
print(nameage("Saif",23))

#used return keyword


# In[26]:


#Q6. Write a function that takes a name and age as positional arguments and prints:
def agename(name,age):
    print(name,age)
agename("saif",23)


# In[29]:


#Q7. Write a function called power(x, y=2) that returns x raised to the power y.
#Test it by calling it with one and two arguments.
def power(x,y=2):
    return x**y
power(3)


# In[30]:


power(5,6)

# def power(x, y=2):
#     return x**y
# y=2 is the default value
# But if you pass a second argument, it overrides the default


# power(3)
# Only one argument → y uses default → y = 2
# 👉 Result: 3^2=9

# BUT,
# power(6, 5)
# Two arguments → y becomes 5 (overrides default)
# 👉 Result: 6^5=7776


# In[ ]:




