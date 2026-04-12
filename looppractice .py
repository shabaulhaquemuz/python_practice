#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a program to print all natural numbers from 1 to n.
n=int(input("enter the value of n:"))
for i in range(1,n+1):
    print(i,end=" ")


# In[3]:


#Write a program to print all natural numbers in reverse (from 1 to n).
n=int(input("enter the value of n:"))
i=1
while(i<=n):
    print(i)
    i+=1


# In[4]:


#Write a program to print all natural numbers in reverse (from n to 1).
n=int(input("enter the value of n:"))
for i in range(n,0,-1):
    print(i, end=" ")


# In[38]:


#1. Write a program to print all natural numbers from n to 1. – using while loop
n=int(input("enter the value of n:"))
while(n>=1):
    print(n)
    n-=1


# In[43]:


#3. Write a program to print all alphabets from a to z.
for i in range(97,123):
    print(chr(i),end=" ")



# In[44]:


#3. Write a program to print all alphabets from A to Z.
for i in range(65,91):
    print(chr(i),end=" ")


# In[1]:


#3. Write a program to print all alphabets from a to z. – using while loop
i=97
while(i<=122):
    print(chr(i),end=" ")
    i+=1


# In[5]:


#3.. Write a program to print all alphabets from A to Z. – using while loop
i=65
while(i<=90):
    print(chr(i),end=" ")
    i+=1


# In[7]:


#4. Write a program to print all even numbers between 1 to 100.
for i in range(1,101):
    if(i%2==0):
        print(i,end=" ")


# In[1]:


#4. Write a program to print all even numbers between 1 to 100.
i=1
while(i<=100):
    if(i%2==0):
        print(i,end=" ")
    i+=1


# In[4]:


#5. Write a program to find the sum of all odd numbers between 1 to n.
n=int(input("enter n:"))
sum=0
for i in range(1,n+1):
    if(i%2!=0):
        sum+=i
print(sum)



# In[6]:


#5. Write a program to find the sum of all odd numbers between 1 to n.
n=int(input("enter n:"))
i=1
sum=0
while(i<=n):
    if(i%2!=0):
        sum+=i
    i+=1
print(sum)


# In[26]:


#6. Write a program to count the number of digits in a number.
n=int(input("enter any number:"))
count=0
num=abs(n)
for i in range(len(str(num))):
               digit=num%10
               count+=1
               num=num//10
print(count)


# In[25]:


n=int(input("enter any number:"))
count=0
num=abs(n)
while(num>=1):
    count+=1
    num=num//10
print(count)


# In[22]:


#7. Write a program to calculate the sum of digits of a number.
n=int(input("enter any  number:"))
sum=0
num=abs(n)
for i in range(len(str(num))):
    digit=num%10
    sum+=digit
    num=num//10
print(sum)


# In[42]:


#7. Write a program to calculate the sum of digits of a number.
n=int(input("enter a number:"))
sum=0
num=abs(n)
while(num>=1):
    digit=num%10
    sum+=digit
    num=num//10
print(sum)



# In[36]:


#8.Write a program to find the first and last digit of a number.
n=int(input("enter the number:"))
num=abs(n)
last_digit=num%10
for i in range(len(str(num))):
    if(num<10):
        first_digit=num
        break
    num=num//10
print("first digit is:",first_digit)
print("last digit is:",last_digit)   


# In[45]:


#8.Write a program to find the first and last digit of a number.
n=int(input("enter a number:"))
num=abs(n)
last_digit=num%10
while(num>0):
    if(num<10):
        first_digit=num
        break
    num=num//10
print("first digit",first_digit)
print("last_digit",last_digit)


# In[ ]:





# In[39]:


#9. Write a program to find the sum of first and last digit of a number.
n=int(input("enter the value of n:"))
num=abs(n)
sum=0
last_digit=num%10
for i in range(len(str(num))):
    if(num<10):
        first_digit=num
        break
    num=num//10
print("first_digit:",first_digit)
print("last_digit:",last_digit)
print("sum of first and last digits is:",first_digit+last_digit)




# In[47]:


#9. Write a program to find the sum of first and last digit of a number.
n=int(input("enter the value of n:"))
num=abs(n)
sum=0
last_digit=num%10
while(num>0):
    if(num<10):
        first_digit=num
        break
    num=num//10
print("first_digit:",first_digit)
print("last_digit:",last_digit)
print("sum of first and last digits is:",first_digit+last_digit)




# In[40]:


#10.Write a program to enter a number and print its reverse.
n=int(input("enter a number:"))
num=abs(n)
print("original number is:",num)
print("reverse is:")
for i in range(len(str(num))):
    digit=num%10
    print(digit,end=" ")
    num=num//10



# In[52]:


#10.Write a program to enter a number and print its reverse.
n=int(input("enter a number:"))
num=abs(n)
print("original number is:",num)
print("reverse is:")
while(num>0):
    digit=num%10
    print(digit,end="")
    num=num//10


# In[63]:


#11.Write a program to find the power of a number using for loop.
n=int(input("enter a number:"))
power=int(input("enter degree for power:"))
num=abs(n)
power_value=1
for i in range(power):
    power_value*=num
print(power_value)


# In[66]:


#12.Write a program to find all factors of a number.
n=int(input("enter any number:"))
print("factors are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")   


# In[69]:


#13.Write a program to calculate the factorial of a number.
n=int(input("enter any number:"))
factorial=1
for i in range(n,0,-1):
    factorial*=i
print(factorial)


# In[70]:


#13.Write a program to calculate the factorial of a number.
n=int(input("enter any number:"))
factorial=1
while(n>0):
    factorial*=n
    n-=1
print(factorial)


# In[17]:


#14.Write a program to find LCM of two numbers.
#14.Write a program to find LCM of two numbers.
m=int(input("enter first number:"))
n=int(input("enter second number:"))
LCM=1
a, b = m, n   # store original values
for i in range(2,max(a,b)+1):
    while(b%i==0 or a%i==0):
        LCM*=i
        if(a%i==0):
            a=a//i
        if(b%i==0):
            b=b//i
print("LCM is:",LCM)



# 👉 But m and n are changing inside the loop
# 👉 Better to store original values


# In[84]:


#15.Write a program to check whether a number is Prime number or not.
n=int(input("enter any number:"))
count=0
if(n<=1):
    print("prime number is always greater than 1")
else:
    for i in range(2,n):
                if(n%i==0):
                    count=1
                    break
    if(count==0):
        print("prime")
    else:
        print("not a prime")

No ❌ — -2 is NOT a prime number

get_ipython().run_line_magic('pinfo', 'Why')

# A prime number is defined as:
# 👉 A number greater than 1
# 👉 Has only 2 factors: 1 and itself
# Negative numbers (like -2, -3, -5) → ❌ NOT prime
# 0 and 1 → ❌ NOT prime
# Only numbers > 1 can be prime


# In[4]:


#15.Write a program to check whether a number is Prime number or not.
n=int(input("enter the number:"))
i=2
count=0
if(n<=1):
    print("prime number is always greater than 1")
else:
    while(i<n):
        if(n%i==0):
            count=1
            break
        i+=1
    if(count==0):
        print("prime")
    else:
        print("not a prime")


# In[11]:


#16.Write a program to print all Prime numbers between 1 to n.
n=int(input("enter value of n:"))
for i in range(2,n+1):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count+=1
    if(count==0):
        print("prime",i)


# In[14]:


#16.Write a program to print all Prime numbers between 1 to n.
n=int(input("enter a number:"))
for i in range(2,n+1):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count+=1
    if(count==0):
        print(i,end=" ")


# In[19]:


#17.Write a program to find all prime factors of a number.
n=int(input("enter a number:"))
for i in range(2,n+1):
    count=0
    if(n%i==0):
        for j in range(2,i):
            if(i%j==0):
                count+=1
        if(count==0):
            print(i)


# In[23]:


# 18.Write a program to check whether a number is an Armstrong number or not.
# a. An Armstrong number is a n-digit number that is equal to the sum
# of the nth power of its digits. For example –
# 6 = 61 = 6
# 371 = 33 + 73 + 13 = 371
n=int(input("enter a number:"))
length=len(str(n))
power_digit=1
sum_power=0
original=n
for i in range(length):
    digit=n%10
    power_digit=digit**length
    sum_power+=power_digit
    n=n//10
if(sum_power==original):
    print("armstrong")
else:
    print("not an armstrong")


# In[25]:


n=int(input("enter any number:"))
original=n
length=len(str(n))
power_digit=1
sum_power=0
for i in range(length):
    digit=n%10
    power_digit=digit**length
    sum_power+=power_digit
    n=n//10
if(sum_power==original):
    print("armstrong")
else:
    print("non-armstrong")


# In[27]:


# 19.Write a program to check whether a number is Strong number or not
# a. Strong number is a special number whose sum of factorial digits is
# equal to the original number.
# For example: 145 is a strong number. Since, 1! + 4! + 5! = 145
n=int(input("enter any number:"))
sum_factorial=0
original=n
length=len(str(n))
for i in range(length):
    digit=n%10
    factorial_digit=1
    for j in range(digit,0,-1):
        factorial_digit*=j
    sum_factorial+=factorial_digit
    n=n//10
if(sum_factorial==original):
    print("strong")
else:
    print("not strong")


# In[29]:


n=int(input("enter a number:"))
original=n
length=len(str(n))
sum_factorial=0
for i in range(length):
    digit=n%10
    factorial_digit=1
    for j in range(digit,0,-1):
        factorial_digit*=j
    sum_factorial+=factorial_digit
    n=n//10
if(sum_factorial==original):
    print("strong")
else:
    print("not a strong number")


# In[30]:


# 20.Write a program to check whether a number is perfect number or not

# a. Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
# For example: 6 is the first perfect number
# Proper divisors of 6 are 1, 2, 3
# Sum of its proper divisors = 1 + 2 + 3 = 6.
# Hence 6 is a perfect number.
n=int(input("enter any number:"))
original=n
sum_divisor=0
for i in range(1,n):
    if(n%i==0):
        sum_divisor+=i
if(sum_divisor==original):
    print("perfect")
else:
    print("not a perfect")



# In[35]:


# 21.Write a program to print fibonacci series upto n terms
# a. Fibonacci series is a series of numbers where the current number is the sum of the previous two terms.
# For Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... , (n-1th + n-2th)
n=int(input("enter value of n:"))
first_term=0
second_term=1
print(first_term,end=" ")
print(second_term,end=" ")
for i in range(n-2):
    next_term=first_term+second_term
    print(next_term,end=" ")
    first_term=second_term
    second_term=next_term


# In[36]:


# 22.Write a program to find ones complement of a binary number
# a. One's complement of a binary number is defined as value obtained by inverting all binary bits.
# It is the result of swapping all 1s to 0s and all 0s to 1s.
n=int(input("enter any number:"))
binary=bin(n)[2:]
complement=""
for bit in binary:
    if(bit=="1"):
        complement+="0"
    else:
        complement+="1"
print("1's complement is:",complement)


# In[ ]:





# In[ ]:




