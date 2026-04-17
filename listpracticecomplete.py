#!/usr/bin/env python
# coding: utf-8

# In[2]:


#fetch value greater than 10 and store it in new_list
list1=[10,4,5,67,89,90,1,2,3,1000]
newlist=[]
for i in range(len(list1)):
    if(list1[i]>10):
        newlist.append(list1[i])
print(newlist)


# In[3]:


#fetch value greater than 10 and store it in new_list
list1=[10,4,5,67,89,90,1,2,3,1000]
newlist=[]
for i in list1:
    if(i>10):
        newlist.append(i)
print(newlist)


# In[5]:


#fetch value greater than 10 and store it in new_list
list1=[10,4,5,67,89,90,1,2,3,1000]
newlist=list(filter(lambda x:x>10,list1))
print(newlist)


# In[7]:


#fetch value greater than 10 and store it in new_list
list1=[10,4,5,67,89,90,1,2,3,1000]
newlist=[i for i in list1 if(i>10)]
print(newlist)


# In[12]:


#to print the elements of string data type from the list
mylist=[10,20,30,"hey","naina",10,"29"]
for i in range(len(mylist)):
    if(type(mylist[i])==str):
        print(mylist[i])


# In[11]:


mylist=[10,20,30,"hey","naina",10,"29"]
for i in mylist:
    if(type(i)==str):
        print(i)


# In[14]:


##to find the maximum in a list
mylist2=[10,1000,20,30,15,6,7,8,999]
maxi=0
for i in mylist2:
    if(i>maxi):
        maxi=i
print(maxi)


# In[15]:


##to find the maximum in a list
mylist2=[10,1000,20,30,15,6,7,8,999]
maxi=mylist2[0]
for i in range(len(mylist2)):
    if(mylist2[i]>maxi):
        maxi=mylist2[i]
print(maxi)


# In[17]:


##to find the maximum in a list of negative numbers
mylist9=[-1,-34,-2,-543,-56,-3212]
maxi=-9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for i in mylist9:
    if(i>maxi):
        maxi=i
print(maxi)

#if its negative elements in the list,then indexing method is used to find the maximum or a very large negative  number


# In[18]:


##to find the maximum in a list of negative numbers
mylist9=[-1,-34,-2,-543,-56,-3212]
maxi=mylist9[0]
for i in range(len(mylist9)):
    if(mylist9[i]>maxi):
        maxi=mylist9[i]
print(maxi)
#if its negative elements in the list,then indexing method is used to find the maximum or a very large negative  number


# In[19]:


##average of elements of a list
mylist5=[10,20,30,15,6,7,8,999]
summ=0
count=0
for i in range(len(mylist5)):
    summ+=mylist5[i]
    count+=1
average=summ/count
print("summ is:",summ)
print("count is:",count)
print("average is:",average)


# In[20]:


##average of elements of a list
mylist5=[10,20,30,15,6,7,8,999]
summ=0
count=0
for i in mylist5:
    summ+=i
    count+=1
average=summ/count
print("sum is:",summ)
print("count:",count)
print("average:",average)


# In[21]:


##to check which element of the list has more than 4 letters
mylist6=['hllo','hey','user','aman','shabaul','haque']
for i in range(len(mylist6)):
    if(len(mylist6[i])>4):
        print(mylist6[i])


# In[22]:


##to check which element of the list has more than 4 letters
mylist6=['hllo','hey','user','aman','shabaul','haque']
for i in mylist6:
    if(len(i)>4):
        print(i)


# In[23]:


#finding minimum(-ve values) using min=0,max cant be founded for -ve values from this method
V=[-1,-34,-2,-543,-56,-3212]
minn=0
for i in V:
    if(i<minn):
        minn=i
print(minn)


# In[24]:


#finding minimum(-ve values) using min=0,max cant be founded for -ve values from this method
V=[-1,-34,-2,-543,-56,-3212]
minn=V[0]
for i in range(len(V)):
    if(V[i]<minn):
        minn=V[i]
print(minn)


# In[32]:


#Finding second maximum in a list
o=[5764,23,43,67,865,42]
o.sort()
print(o)


# In[33]:


o = [5, 2, 9, 1]

o.sort()          # modifies original list
print(o)          # [1, 2, 5, 9]


# * `o.sort()` sorts the **same list in-place**, meaning the original list `o` is modified and no new list is created.
# * `sorted(o)` returns a **new sorted list**, while the original list `o` remains unchanged.


# In[34]:


o = [5, 2, 9, 1]

a = sorted(o)     # creates new sorted list
print(a)          # [1, 2, 5, 9]
print(o)          # [5, 2, 9, 1] (original unchanged)


# In[36]:


#arrange a list in descending order
o=[5,2,9,1]
o.sort(reverse=True)
print(o)


# In[39]:


o=[5,2,9,1]
a=sorted(o,reverse=True)
print("original list:",o)
print("sorted list:",a)


# In[40]:


#Finding minimum in a list
o=[5764,23,43,67,865,42]
min(o)


# In[41]:


#Finding maximum in a list
o=[5764,23,43,67,865,42]
max(o)


# In[42]:


#Finding second minimum in a list
o=[5764,23,43,67,865,42]
a=sorted(o,reverse=True)
print(a[-2])


# In[45]:


#Finding second minimum in a list
o=[5764,23,43,67,865,42]
o.sort(reverse=True)
print(o[-2])


# In[43]:


#Finding second maximum in a list
o=[5764,23,43,67,865,42]
a=sorted(o)
print(a[-2])


# In[46]:


#Finding second maximum in a list
o=[5764,23,43,67,865,42]
o.sort()
print(o[-2])


# In[48]:


#Finding second maximum in a list
o=[5764,23,43,67,865,42]
o.sort(reverse=True)
print(o[1])


# In[53]:


#Finding second maximum in a list
mylist=[5764,23,43,67,865,42,10000]
if(mylist[0]>mylist[1]):
    maximum=mylist[0]
    secondmaximum=mylist[1]
else:
    maximum=mylist[1]
    secondmaximum=mylist[0]
for i in mylist[2:]:
    if(i>maximum):
        secondmaximum=maximum
        maximum=i
    elif(i>secondmaximum and i!=maximum):
        secondmaximum=i
print(maximum,secondmaximum)




# In[55]:


#Finding second maximum in a list
mylist=[5764,23,43,67,865,42,10000]
if(mylist[0]>mylist[1]):
    maximum=mylist[0]
    secondmaximum=mylist[1]
else:
    maximum=mylist[1]
    secondmaximum=mylist[0]
for i in mylist[2:]:
    if(i>maximum):
        secondmaximum=maximum
        maximum=i
    elif(i>secondmaximum and i!=maximum):
        secondmaximum=i
print(maximum,secondmaximum)


# In[57]:


#Finding second maximum in a list
mylist=[5764,23,43,67,865,42,10000]
if(mylist[0]>mylist[1]):
    maximum=mylist[0]
    secondmaximum=mylist[1]
else:
    maximum=mylist[1]
    secondmaximum=mylist[0]
for i in mylist[2:]:
    if(i>maximum):
        secondmaximum=maximum
        maximum=i
    elif(i>secondmaximum and i!=maximum):
        secondmaximum=i
print(maximum,secondmaximum)


# In[59]:


#Finding second maximum in a list
mylist=[5764,23,43,67,865,42,10000]
if(mylist[0]>mylist[1]):
    maximum=mylist[0]
    secondmaximum=mylist[1]
else:
    maximum=mylist[1]
    secondmaximum=mylist[0]
for i in mylist[2:]:
    if(i>maximum):
        secondmaximum=maximum
        maximum=i
    elif(i>secondmaximum and i!=maximum):
        secondmaximum=i
print(maximum,secondmaximum)


# In[60]:


#Finding second maximum in a list
mylist=[5764,23,43,67,865,42,10000]
if(mylist[0]>mylist[1]):
    maximum=mylist[0]
    secondmaximum=mylist[1]
else:
    maximum=mylist[1]
    secondmaximum=mylist[0]
for i in mylist[2:]:
    if(i>maximum):
        secondmaximum=maximum
        maximum=i
    elif(i>secondmaximum and i!=maximum):
        secondmaximum=i
print(maximum,secondmaximum)


# In[63]:


#finding duplicate in a list and create a new list for duplicate
p=[22,3,2,4,55,66,33,222,222,22,3,55]
newlist=[]
duplicate=[]
for i in p:
    if(i not in newlist):
        newlist.append(i)
    else:
        duplicate.append(i)
print(newlist,duplicate)

#BUT THIS APPROACH WILL GIVE DUPLICATE VALUES IN THE DUPLICATE LIST ITSELF


# In[64]:


#finding duplicate in a list and create a new list for duplicate
p=[22,3,2,4,55,66,33,222,222,22,3,55,222,222]
newlist=[]
duplicate=[]
for i in p:
    if(i not in newlist):
        newlist.append(i)
    else:
        duplicate.append(i)
print(newlist,duplicate)
#SEE THE ISSUE IN THE OUTPUT OF DUPLICATE LIST


# In[65]:


#finding duplicate in a list and create a new list for duplicate
p=[22,3,2,4,55,66,33,222,222,22,3,55]
newlist=[]
duplicate=[]
for i in p:
    if(i not in newlist):
        newlist.append(i)
    elif(i not in duplicate):
        duplicate.append(i)
print(p,newlist,duplicate)



# In[66]:


#nested loop
list10=[10,20,30,40]
for i in range(0,1):
    print(i,list10[i])


# In[67]:


list11=[10,20,30,40]
for i in range(0,3):
    print(i,list11[i])


# In[69]:


list12=[10,20,30,40]
for i in range(len(list12)):
    print(i,list12[i])


# In[70]:


list12=[10,20,30,40]
for i in range(len(list12)):
    print(i,list12)


# In[73]:


list13=[10,20,30,40]
for i in range(0,1):
    print(i)
    for j in range(1,3):
        print(i,list13[i],j,list13[j])


# In[75]:


list14=[10,20,30,40]
for i in range(0,2):
    print(list14[i])
    for j in range(1,4):
        print(i,list14[i],j,list14[j])


# In[76]:


list15=[10,20,30,40]
for i in range(0,4):
    print(list15[i])
    for j in range(1,4):
        print(i,list15[i],list15[j])


# In[93]:


#to check duplicate elements in the list
# Print unique duplicate elements using two for loops”
# “Identify duplicates in a list using nested loops (no repetition)
list15 = [10, 20, 30, 40, 10, 20,20]
duplicate=[]
for i in range(len(list15)):
    for j in range(i+1,len(list15)):
        if(list15[i]==list15[j] and list15[i] not in duplicate):
            print("duplicates are:",list15[i])
            duplicate.append(list15[i])
print("LIST OF UNIQUE DUPLICATE ITEMS ARE:",duplicate)


# In[94]:


#to check duplicate elements in the list
# Print unique duplicate elements using two for loops”
# “Identify duplicates in a list using nested loops (no repetition)
list15 = [10, 20, 30, 40, 10, 20,20]
duplicate=[]
for i in range(len(list15)):
    for j in range(i+1,len(list15)):
        if(list15[i]==list15[j] and list15[i] not in duplicate):
            print("duplicates are:",list15[i])
            duplicate.append(list15[i])
print("LIST OF UNIQUE DUPLICATE ITEMS ARE:",duplicate)


# In[95]:


#to check if sum of two elements of a list is 9
list18=[1,2,3,7,14,6,4,5]
for i in range(len(list18)):
    for j in range(i+1,len(list18)):
        if(list18[i]+list18[j]==9):
            print(list18[i],list18[j])


# In[96]:


#to print duplicate characters from a string
string="hey user"
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if(string[i]==string[j]):
            print(string[i],string[j])


# In[98]:


#to print duplicate characters from a string
string="hey usere" 
newlist=[]
duplicate=[]
for i in string:
    if(i not in newlist):
        newlist.append(i)
    else:
        duplicate.append(i)
print(newlist,duplicate)
#It will print the duplicate items more than 1 if the letter is appearing more than twice


# In[100]:


#to print duplicate characters from a string
string="hey usereee" 
newlist=[]
duplicate=[]
for i in string:
    if(i not in newlist):
        newlist.append(i)
    elif(i not in duplicate):
        duplicate.append(i)
print(newlist)
print(duplicate)
#This will give the unique duplicates only in the list named as duplicate


# In[101]:


#to print duplicate characters from a string
string="hey usereee"
newlist=[]
duplicate=[]
for i in string:
    if(i not in newlist):
        newlist.append(i)
    elif(i not in duplicate):
        duplicate.append(i)
print(newlist)
print(duplicate)
#This will give the unique duplicates only in the list named as duplicate


# In[102]:


#to print duplicate characters from a string[problem:print duplicate characters multiple times]
string="hey useru"
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if(string[i]==string[j]):
            print(string[i])


# In[104]:


#to print duplicate characters from a string[problem:print unique duplicates],solution is below:-
string="hey usereeue"
duplicatestr=[]
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if(string[i]==string[j] and string[i] not in duplicatestr):
            duplicatestr.append(string[i])
print(duplicatestr)


# In[105]:


#to print duplicate characters from a string[problem:print unique duplicates],solution is below:-
string="hey usereeue"
duplicatestr=[]
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if(string[i]==string[j] and string[i] not in duplicatestr):
            duplicatestr.append(string[i])
print(duplicatestr)


# In[106]:


#print unique duplicates in the form of list
list22=[10, 20, 10, 10, 10, 10, 31, 40, 31]
duplicatelist=[]
for i in range(len(list22)):
    for j in range(i+1,len(list22)):
        if(list22[i]==list22[j] and list22[i] not in duplicatelist):
            duplicatelist.append(list22[i])
print(duplicatelist)



# In[107]:


#to print duplicate item just once, using for loop
list20=[10,20,10,10,10,10,31,40,31]
duplicate=[]
for i in range(len(list20)):
    for j in range(i+1,len(list20)):
        if(list20[i]==list20[j] and list20[i] not in duplicate):
            duplicate.append(list20[i])
print(duplicate)


# In[2]:


#finding two elements sum of which is 9 using single loop and using two pointer approach(while loop)
list19 = [1,2,3,5,7,11,18,6,4]
print(list19)
list19.sort()
print(list19)
start=0
end=len(list19)-1
while(start<end):
    p=list19[start]+list19[end]
    if(p>9):
        end-=1
    elif(p<9):
        start+=1
    else:
        print(list19[start],list19[end])
        start+=1
        end-=1



# In[4]:


#finding two elements sum of which is 9 using single loop and using two pointer approach(while loop)
list19 = [1,2,3,5,7,11,18,6,4]
list19.sort()
start=0
end=len(list19)-1
while(start<end):
    s=list19[start]+list19[end]
    if(s>9):
        end-=1
    elif(s<9):
        start+=1
    else:
        print(list19[start],list19[end])
        start+=1
        end-=1


# In[5]:


#finding two elements sum of which is 9 using single loop and using two pointer approach(while loop)
list19 = [1,2,3,5,7,11,18,6,4]
list19.sort()
start=0
end=len(list19)-1
while(start<end):
    if(list19[start]+list19[end]>9):
        end-=1
    elif(list19[start]+list19[end]<9):
        start+=1
    else:
        print(list19[start],list19[end])
        start+=1
        end-=1


# In[11]:


s=input("enter any word:")
start=0
end=len(s)-1
count=0
for i in range(len(s)//2):
    if(s[start]!=s[end]):
        count=1
        break
    start+=1
    end-=1
if(count==0):
    print("Palindrome")
else:
    print("Not a palindrome")


# In[13]:


n = int(input("Enter how many numbers: "))

total = 0

for i in range(n):
    num = int(input("Enter number: "))
    total += num

avg = total / n

print("Average =", avg)


# In[14]:


# <!-- 1.Write a Python program to find the maximum element in a list of numbers without max functions
# numbers = [10, 20, 4, 45, 99]
# The maximum element is: 99 -->
numbers = [10, 20, 4, 45, 99]
max(numbers)


# In[15]:


numbers = [10, 20, 4, 45, 99]
maximum=max(numbers)
print(maximum)


# In[16]:


numbers = [10, 20, 4, 45, 99]
maxi=0
for i in numbers:
    if(i>maxi):
        maxi=i
print(maxi)


# In[17]:


#2.Write a Python program to sum all the elements in a list of numbers.
#a. numbers = [10, 20, 30, 40]
#b. The sum of all elements is: 100
numbers = [10, 20, 30, 40]
summ=0
for i in numbers:
    summ+=i
print(summ)


# In[18]:


numbers = [10, 20, 30, 40]
sum(numbers)


# In[19]:


numbers = [10, 20, 30, 40]
summation=sum(numbers)
print(summation)


# In[21]:


#3.Write a Python program to reverse a list without reverse or slicing operator
#a. numbers = [1, 2, 3, 4, 5]
#b. Reversed list: [5, 4, 3, 2, 1]
numbers = [1, 2, 3, 4, 5]
reversed_list=[]
for i in range(len(numbers)):
    x=numbers.pop()
    reversed_list.append(x)
print(reversed_list)


# In[22]:


#4.Write a Python program to sort a list in ascending order without sort functions
x4=[4,76,54,67,90,1000,800,900]
x4.sort()
print(x4)


# In[23]:


#4.Write a Python program to sort a list in ascending order without sort functions
x4=[4,76,54,67,90,1000,800,900]
ascending=sorted(x4)
print(ascending)


# In[24]:


#4.Write a Python program to sort a list in ascending order without sort functions
x4=[4,76,54,67,90,1000,800,900]
x4.sort(reverse=True)
print(x4)


# In[27]:


#4.Write a Python program to sort a list in ascending order without sort functions
x4=[4,76,54,67,90,1000,800,900]
descending=sorted(x4,reverse=True)
print(descending)


# In[32]:


#4.Write a Python program to sort a list in ascending order without sort functions
x4=[4,76,54,67,90,1000,800,900]
for i in range(len(x4)):
    for j in range(i+1,len(x4)):
        if(x4[i]>x4[j]):
            x4[i],x4[j]=x4[j],x4[i]
print(x4)


# In[36]:


x4 = [4,76,54,67,90,1000,800,900]
i=0
n=len(x4)
while(i<n-1):
    if(x4[i]>x4[i+1]):
        x4[i],x4[i+1]=x4[i+1],x4[i]
        i=0 #Sorting needs rechecking previous elements after swap — that’s why restart is required.
    else:
        i+=1
print(x4)


# In[40]:


#5.Write a Python program to remove duplicates from a list while maintaining the order of elements.
#a. numbers = [1, 2, 2, 3, 4, 4, 5]
#b. List after removing duplicates: [1, 2, 3, 4, 5]
numbers = [1, 2, 2, 3, 4, 4, 5]
unique=[]
for i in numbers:
    if(i not in unique):
        unique.append(i)
print(unique)



# In[44]:


#6.Write a Python program to find all pairs of numbers in a list that add up to a specific target sum.
#a. numbers = [1, 2, 3, 4, 3, 5, 6] target_sum = 6
#b. Pairs that add up to 6: [(3, 3), (2, 4), (1, 5)]
numbers = [1, 2, 3, 4, 3, 5, 6]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]+numbers[j]==6):
            print(numbers[i],numbers[j])


# In[45]:


#6.Write a Python program to find all pairs of numbers in a list that add up to a specific target sum.
#a. numbers = [1, 2, 3, 4, 3, 5, 6] target_sum = 6
#b. Pairs that add up to 6: [(3, 3), (2, 4), (1, 5)]
numbers = [1, 2, 3, 4, 3, 5, 6]
# If you want output like:
# [(3,3), (2,4), (1,5)]
pairs=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]+numbers[j]==6):
            pairs.append((numbers[i],numbers[j]))
print(pairs)


# In[46]:


#6.Write a Python program to find all pairs of numbers in a list that add up to a specific target sum.
#a. numbers = [1, 2, 3, 4, 3, 5, 6] target_sum = 6
#b. Pairs that add up to 6: [(3, 3), (2, 4), (1, 5)]
numbers = [1, 2, 3, 4, 3, 5, 6]
# If you want output like in descending order as given:
# [(3,3), (2,4), (1,5)]
pairs=[]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]+numbers[j]==6):
            pairs.append((numbers[i],numbers[j]))
pairs.sort(reverse=True)
print(pairs)


# In[2]:


#7.Write a Python program to flatten a nested list (list within lists) into a single list.
#a. nested_list = [1, [2, 3], [4, [5, 6], 7], 8]
#b. Flattened list: [1, 2, 3, 4, 5, 6, 7, 8]
nested_list = [1, [2, 3], [4, [5, 6], 7], 8]
newlist=[]
Flattened_list=[]
for i in nested_list:
    if(type(i)!=list):
        newlist.append(i)
    elif(type(i)==list):
        newlist.extend(i)
for j in newlist:
    if(type(j)!=list):
        Flattened_list.append(j)
    elif(type(j)==list):
        Flattened_list.extend(j)
print(newlist)
print(Flattened_list)


# In[5]:


#8.Write a Python program to find the sum of the elements in a list, excluding the largest and smallest element. Don’t use max or min functions
#a. numbers = [1, 2, 3, 4, 5]
#b. Sum excluding the largest and smallest element: 9
numbers = [1, 2, 3, 4, 5]
maxi=numbers[0]
mini=numbers[0]
summ=0
for i in range(len(numbers)):
    if(numbers[i]>maxi):
        maxi=numbers[i]
for j in range(len(numbers)):
    if(numbers[j]<mini):
        mini=numbers[j]
for k in numbers:
    if(k!=maxi and k!=mini):
        summ+=k
print("maximum element is:",maxi)
print("minimum element is:",mini)
print("sum is:",summ)

#numbers = [1, 2, 3, 4, 5, 5]..if it has two maximumns
#Your code removes both 5s, but if you want to remove only one largest and one smallest go for code below


# In[ ]:


numbers = [1, 2, 3, 4, 5]

maxi = numbers[0]
mini = numbers[0]
summ = 0

# find max and min
for i in numbers:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

# calculate total sum
for i in numbers:
    summ += i

# subtract only one max and one min
summ = summ - maxi - mini

print("maximum element is:", maxi)
print("minimum element is:", mini)
print("sum is:", summ)


# In[6]:


#9.Write a Python program to check if a list is a palindrome (reads the same backward as forward) using two pointer approach
#a. numbers = [1, 2, 3, 2, 1]
#b. True
numbers = [1, 2, 3, 2, 1]
start=0
end=len(numbers)-1
count=0
for i in range(len(numbers)//2):
    if(numbers[start]!=numbers[end]):
        count=1
        break
    start+=1
    end-=1
if(count==0):
    print("Palindrome")
else:
    print("Not Palindrome")


# In[10]:


#11. Find Common Elements in Two Lists
#a. list1 = [1, 2, 3, 4, 5]
#b. list2 = [3, 4, 5, 6, 7]
#c. Result: [3, 4, 5]
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7,4]
result=[]
for i in list1:
    for j in list2:
        if(i==j and i not in result):
            result.append(i)
print(result)


# In[12]:


#12. Find the Longest Word in a List
#a. words = ["apple", "banana", "strawberry", "kiwi"]
#b. Strawberry
words = ["apple", "Indian Blackberry", "banana", "strawberry", "kiwi"]
longest=words[0]
for i in range(len(words)):
    if(len(words[i])>len(longest)):
        longest=words[i]
print(longest)


# In[16]:


#14. Find Missing Number in a List
#You are given a list of n-1 numbers in the range 1 to n. One number is missing from the sequence. Find the missing number.
#a. numbers = [1, 2, 4, 5, 6]
#b. 3
numbers = [1, 2, 4, 5, 6]
start=0
nexxt=1
for i in range(len(numbers)-1):
    if((numbers[nexxt]-numbers[start])!=1):
        print(numbers[nexxt]-1)
    start+=1
    nexxt+=1
#But this is only true when there is just one missing number


# In[20]:


#14. Find Missing Number in a List
#You are given a list of n-1 numbers in the range 1 to n. More than One number is missing from the sequence. Find the missing number.
#a. numbers = [1, 2, 4, 5, 6]
#b. 3|
x15=[1,2,4,5,6,7,9,10,11,13]
start=0
nexxt=1
missing=[]
for i in range(len(x15)-1):
    if(x15[nexxt]-x15[start]!=1):
        missing.append(x15[nexxt]-1)
    start+=1
    nexxt+=1
print(missing)


# In[7]:


#15. Find the First Non-Repeating Element
#Given a list of integers, find the first element that appears only once.
#a. numbers = [4, 5, 1, 2, 0, 4, 5, 2]
#b. Expected Output: 1
numbers = [4, 5, 1, 2, 0, 4, 5, 2]
for num in numbers:
    if(numbers.count(num)==1):
        print(num)
        break


# In[9]:


#15. Find the First Non-Repeating Element
#Given a list of integers, find the first element that appears only once.
#a. numbers = [4, 5, 1, 2, 0, 4, 5, 2]
#b. Expected Output: 1
for i in range(len(numbers)):
    count=0
    for j in range(i+1,len(numbers)):
        if(i!=j and numbers[i]==numbers[j]):
            count+=1
    if(count==0):
        print(numbers[i])
        break


# In[10]:


numbers = [4, 5, 1, 2, 0, 4, 5, 2]
for i in range(len(numbers)):
    count=0
    for j in range(i+1,len(numbers)):
        if(i!=j and numbers[i]==numbers[j]):
            count+=1
    if(count==0):
        print(numbers[i])
        break


# In[11]:


numbers = [4, 5, 1, 2, 0, 4, 5, 2]
for i in range(len(numbers)):
    count=0
    for j in range(i+1,len(numbers)):
        if(i!=j and numbers[i]==numbers[j]):
            count+=1
    if(count==0):
        print(numbers[i])
        break


# In[15]:


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


# In[21]:


#17. Find Elements Greater Than Their Left Neighbor
#a. numbers = [1, 3, 2, 6, 5, 8, 7]
#b. [3, 6, 8]
numbers = [1, 3, 2, 6, 5, 8, 7]
start=0
nexxt=1
gret=[]
for i in range(len(numbers)-1):
    if(numbers[nexxt]>numbers[start]):
        gret.append(numbers[nexxt])
    start+=1
    nexxt+=1
print(gret)


# In[18]:


#17. Find Elements Greater Than Their Left Neighbor
#a. numbers = [1, 3, 2, 6, 5, 8, 7]
#b. [3, 6, 8]
list21 = [1, 3, 2, 6, 5, 8, 7]
greaterlist = []

for i in range(1, len(list21)):
    if list21[i] > list21[i - 1]:
        greaterlist.append(list21[i])

print(greaterlist)


# In[23]:


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




