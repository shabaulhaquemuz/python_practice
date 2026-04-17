#!/usr/bin/env python
# coding: utf-8

# In[19]:


# <!-- 1.Write a Python program to find the maximum element in a list of numbers without max functions
# numbers = [10, 20, 4, 45, 99]
# The maximum element is: 99 -->
numbers = [100,10, 20, 4, 45, 99]
maxx=0
for i in range(len(numbers)):
    if(numbers[i]>maxx):
        maxx=numbers[i]
print(maxx)


# In[20]:


#2.Write a Python program to sum all the elements in a list of numbers.
#a. numbers = [10, 20, 30, 40]
#b. The sum of all elements is: 100
numbers = [10, 20, 30, 40]
summ=0
for i in numbers:
    summ+=i
print(summ)


# In[27]:


#3.Write a Python program to reverse a list without reverse or slicing operator
#a. numbers = [1, 2, 3, 4, 5]
#b. Reversed list: [5, 4, 3, 2, 1]
numbers = [1, 2, 3, 4, 5]
reverse_list=[]
for i in range(len(numbers)):
    x=numbers.pop()
    reverse_list.append(x)
print(reverse_list)


# In[34]:


#4.Write a Python program to sort a list in ascending order without sort functions
x4=[4,76,54,67,90,1000,800,900]
for i in range(len(x4)):
    for j in range(i+1,len(x4)):
        if(x4[i]>x4[j]):
            x4[i],x4[j]=x4[j],x4[i]
print(x4)


# In[35]:


#5.Write a Python program to remove duplicates from a list while maintaining the order of elements.
#a. numbers = [1, 2, 2, 3, 4, 4, 5]
#b. List after removing duplicates: [1, 2, 3, 4, 5]
numbers = [1, 2, 2, 3, 4, 4, 5]
no_duplicates=[]
for i in numbers:
    if(i not in no_duplicates):
        no_duplicates.append(i)
print(no_duplicates)


# In[43]:


#6.Write a Python program to find all pairs of numbers in a list that add up to a specific target sum.
#a. numbers = [1, 2, 3, 4, 3, 5, 6] target_sum = 6
#b. Pairs that add up to 6: [(3, 3), (2, 4), (1, 5)]
numbers = [1, 2, 3, 4, 3, 5, 6]
new=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]+numbers[j]==6):
            new.append((numbers[i],numbers[j]))
new.sort(reverse=True)
print(new)


# In[46]:


#7.Write a Python program to flatten a nested list (list within lists) into a single list.
#a. nested_list = [1, [2, 3], [4, [5, 6], 7], 8]
#b. Flattened list: [1, 2, 3, 4, 5, 6, 7, 8]
nested_list = [1, [2, 3], [4, [5, 6], 7], 8]
new=[]
flattened=[]
for i in range(len(nested_list)):
    if(type(nested_list[i])!=list):
        new.append(nested_list[i])
    elif(type(nested_list[i])==list):
        new.extend(nested_list[i])
print(new)
for j in range(len(new)):
    if(type(new[j])!=list):
        flattened.append(new[j])
    elif(type(new[j])==list):
        flattened.extend(new[j])
print(flattened)


# In[47]:


#8.Write a Python program to find the sum of the elements in a list, excluding the largest and smallest element. Don’t use max or min functions
#a. numbers = [1, 2, 3, 4, 5]
#b. Sum excluding the largest and smallest element: 9
numbers = [1, 2, 3, 4, 5]
maxx=numbers[0]
minn=numbers[0]
summ=0
for i in range(len(numbers)):
    if(numbers[i]>maxx):
        maxx=numbers[i]
    elif(numbers[i]<minn):
        minn=numbers[i]
print("min is:",minn)
print("max is:",maxx)
for k in range(len(numbers)):
    if(numbers[k]!=maxx and numbers[k]!=minn):
        summ+=numbers[k]
print("sum is:",summ)


# In[49]:


#9.Write a Python program to check if a list is a palindrome (reads the same backward as forward) using two pointer approach
#a. numbers = [1, 2, 3, 2, 1]
#b. True
numbers = [1, 2, 3, 2, 1]
start=0
end=-1
count=0
for i in range(len(numbers)//2):
    if(numbers[start]!=numbers[end]):
        count=1
        break
    else:
        start+=1
        end-=1
if(count==0):
    print("palindrome")
else:
    print("not palindrome")


# In[51]:


#11. Find Common Elements in Two Lists
#a. list1 = [1, 2, 3, 4, 5]
#b. list2 = [3, 4, 5, 6, 7]
#c. Result: [3, 4, 5]
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result=[]
for i in list1:
    for j in list2:
        if(i==j and i not in result):
            result.append(i)
print(result)


# In[52]:


#12. Find the Longest Word in a List
#a. words = ["apple", "banana", "strawberry", "kiwi"]
#b. Strawberry
words = ["apple", "banana", "strawberry", "kiwi"]
longest=words[0]
for i in range(len(words)):
    if(len(words[i])>len(longest)):
        longest=words[i]
print(longest)



# In[55]:


#14. Find Missing Number in a List
#You are given a list of n-1 numbers in the range 1 to n. One number is missing from the sequence. Find the missing number.
#a. numbers = [1, 2, 4, 5, 6]
#b. 3
numbers = [1, 2, 4, 5, 6]
start=0
nexxt=1
for i in range(len(numbers)-1):
    if(numbers[nexxt]-numbers[start]!=1):
        print(numbers[nexxt]-1)
    start+=1
    nexxt+=1


# In[58]:


#15. Find the First Non-Repeating Element
#Given a list of integers, find the first element that appears only once.
#a. numbers = [4, 5, 1, 2, 0, 4, 5, 2]
#b. Expected Output: 1
numbers = [4, 5, 1, 2, 0, 4, 5, 2]
for i in range(len(numbers)):
    count=0
    for j in range(len(numbers)):
        if(i!=j and numbers[i]==numbers[j]):
            count+=1
    if(count==0):
        print(numbers[i])
        break




# In[59]:


#16. Move All Zeros to the End
#Given a list of integers, move all zeros to the end while maintaining the relative order of non-zero elements. Don’t use any inbuilt functions
#a. numbers = [0, 1, 0, 3, 12]
#b. [1, 3, 12, 0, 0]
numbers = [0, 1, 0, 3, 12]
new=[]
for i in range(len(numbers)):
    if(numbers[i]!=0):
        new.append(numbers[i])
for j in range(len(numbers)):
    if(numbers[j]==0):
        new.append(numbers[j])
print(new)


# In[61]:


#17. Find Elements Greater Than Their Left Neighbor
#a. numbers = [1, 3, 2, 6, 5, 8, 7]
#b. [3, 6, 8]
numbers = [1, 3, 2, 6, 5, 8, 7]
new=[]
start=0
nexxt=1
for i in range(len(numbers)-1):
    if(numbers[nexxt]>numbers[start]):
        new.append(numbers[nexxt])
    start+=1
    nexxt+=1
print(new)


# In[65]:


#18. Find Triplets That Sum to Zero
#Given a list of numbers, find all unique triplets (a, b, c) such that a + b + c = 0.
#a. numbers = [-1, 0, 1, 2, -1, -4]
#b. Expected Output: [(-1, -1, 2), (-1, 0, 1)]
numbers = [-1, 0, 1, 2, -1, -4]
new=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if(numbers[i]+numbers[j]+numbers[k]==0):
                triplets=[numbers[i],numbers[j],numbers[k]]
                triplets.sort()
                if(triplets not in new):
                    new.append(triplets)
print(new)



# In[ ]:




