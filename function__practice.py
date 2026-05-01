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


# In[1]:


def greeting():
    print("Hello Shabaul, How are you?")
greeting()


# In[2]:


greeting()


# In[3]:


def greeting(z):
    print("Hello",z,"How are you?")
greeting("Shabaul Haque")


# In[7]:


def greeting(z):
    return f"Hello {z}! How are you bro?"
greeting("Saif")


# In[8]:


# return:
# Sends a value back to the caller of the function from  the function
# Ends the function's execution immediately.
# You can store the returned value or use it later in your code.


# print:
# Just displays the output to the screen (console).
# Does not send any value back to the caller.
# Mainly used for debugging or user messages.


# In[9]:


# | Feature         | `return`                     | `print`                    |
# | --------------- | ---------------------------- | -------------------------- |
# | Purpose         | Gives output from function   | Displays output to console |
# | Use in chaining | Yes                          | No                         |
# | Data reuse      | Yes (can store or pass it)   | No                         |
# | Ends function?  | Yes                          | No                         |
# | Output visible? | No (unless printed manually) | Yes                        |


# In[11]:


#function to write factors of a number
def factors(num):
    for i in range(1,num+1):
        if(num%i==0):
            print(i,end=" ")
factors(6)


# In[12]:


#function to write factors of a number using return
def factors(num):
    result=[]
    for i in range(1,num+1):
        if(num%i==0):
            result.append(i)
    return result
factors(8)


# In[14]:


def armstrong(num):
    original=num
    count=len(str(num))
    summ_power=0
    for i in range(len(str(num))):
        digit=num%10
        power_digit=digit**count
        summ_power+=power_digit
        num=num//10
    if(summ_power==original):
        print("Armstrong")
    else:
        print("Not an Armstrong")
armstrong(153)


# In[23]:


def positional(name,age,college):
    print("My name is",name,"age is",age,"and college is",college)
positional("saif,",24,"ctae")


# In[26]:


def keywordarg():
    print("My name is",name,"age is",age,"and college is",college)
keywordarg(name="saif",age=24,college="ctae")

#in keyword argument, you still have to pass the parameter


# In[32]:


def keywordarg(name,age,college):
    print("My name is",name,"age is",age,"and college is",college)
keywordarg(name="saif",age=24,college="ctae")

#Keyword arguments give output based on parameter names, not position
#The order inside print() or return decides the output order, not the keyword arguments.

#example 1
def demo(a, b):
    print(b, a)

demo(a=10, b=20)

#reverse example
def demo(a, b):
    print(a, b)

demo(a=10, b=20)


# In[34]:


def keypos(name,age,sex):
    print("My name is",name,"age is",age,"sex is",sex)
keypos("Saif",age=24,"male")

# Positional arguments must come before keyword arguments.
# If you put a positional argument after a keyword argument → it will show error


# In[35]:


def keypos(name,age,sex):
    print("My name is",name,"age is",age,"sex is",sex)
keypos("Saif","male",age=24)

#clash: male here is treated as age because its positional and age=24 is keyword so its clash


# In[36]:


def keypos(name,age,age):
    print("My name is",name,"age is",age,"sex is",sex)
keypos("Saif","male",age=24)
#Duplicate parameters are not allowed in Python functions.


# In[37]:


def keypos(name,age,sex):
    print("my name is",name,"age is",age,"sex is",sex)
keypos("shabaul",23,sex="male")


# In[38]:


# In Python:

# **print()** is a built-in function.

# **return** is a keyword, not a function or method.

#  Keyword
# ✅ A keyword is a reserved word in Python.

# ✅ It has a special meaning and cannot be used as a variable name.

# ✅ Keywords control the structure and flow of a program (like if, for, return, def, etc.)



# In[39]:


# return:
# Sends a value back to the caller of the function from  the function
# Ends the function's execution immediately.
# You can store the returned value or use it later in your code.


# print:
# Just displays the output to the screen (console).
# Does not send any value back to the caller.
# Mainly used for debugging or user messages.


# In[40]:


def check(x):
    print(x+10)
check(5)
#print just displays the output on the console


# In[41]:


def check(x):
    print(x+10)
a=check(20)
#again displays the output even after assigning to the variable


# In[43]:


def check(x):
    print(x+10)
a=check(20)
print(a)
#see after displaying the output print is not storing the value in the variable
#The caller is the line of code that calls/invokes the function
# print() only displays to the screen — it does not send a value back to the caller.


# In[44]:


def check(a):
    return a-10
check(30)
#return sends the value back to the caller of the function from the function


# In[45]:


def check(a):
    return a*10
a=check(20)
#return saved the value in the variable but not displaying until the variable is printed


# In[46]:


def check(a):
    return a-10
x=check(20)
print(x)
#return saved the value in the variable and can be later be used in the program by using the same variable


# In[48]:


print(x)
#here it is later used


# In[49]:


#create a function to find the sum of square of natural numbers upto n
def sumsqnum(n):
    summ=0
    for i in range(1,n+1):
        summ+=i**2
    return summ
sumsqnum(5)



# In[50]:


sum=0
def squaresum(num):
    global sum
    for i in range(1,num+1):
        sum+=i**2
    print(sum)
squaresum(3)
#inside function to use global variable, global keyword is defined locally to that particular function
#The global keyword is written inside the function, but it refers to a variable that exists outside the function (in global scope).
# ✅ global is a keyword in Python.

# ❌ It is not a function.

# ❌not even a method


# In[51]:


x = 10

def show():
    print(x+1)  # ✅ This works fine

show()
# We can use a globally declared variable inside a function without using the global keyword, but only if we are reading/accessing it.
# If we want to modify it, we must use the global keyword.


# In[52]:


x = 10

def change():
    global x
    x = x + 5  # ✅ Modify after declaring global
    print(x)

change()
#global keyword is defined here, because the global variable is getting modified inside the code


# In[53]:


x = 10

def change():
    x = x + 5  # ❌ Error: local variable 'x' referenced before assignment
    print(x)

change()
#global variable is modified and global keyword is not defined under the function so it is giving an error


# In[54]:


#function to calculate the sum of digits of a number
def digsum(num):
    summ=0
    for i in range(len(str(num))):
        digit=num%10
        summ+=digit
        num=num//10
    return summ
digsum(234567)


# In[56]:


#function to check if a number is odd or even
def eveodd(num):
    if(num%2==0):
        print("Even")
    else:
        print("odd")
eveodd(3)


# In[57]:


#function to calculate the sum of two numbers
def sumtwo(a,b):
    summ=a+b
    return summ
sumtwo(4,5)


# In[58]:


# ✅ 1. What is the difference between a function and a method in Python?
# Answer:

# A function is a reusable block of code that performs a specific task and is defined using def.

# A method is a kind of function that is associated with an object and is called using dot . notation (e.g., list.append()).


# In[59]:


#✅ 2. Write a function that returns the square of a number.
def square(num):
    return num**2
square(2)


# In[60]:


#✅ 3. What is the purpose of return in a function? What happens if you don’t use return?
#return sends the value/result back to the caller of the function
#we can store the value of the return in a variable which can be later used in the code or can be passed into another function
#it stops the function execution immediately
#Without return, the function returns None by default.


# In[61]:


#✅ 4. Write a function that takes two numbers as input and returns the larger one.
def larger(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2
larger(1,2)


# In[62]:


#✅ 1. Check Even or Odd
def oddeve(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")
oddeve(3)


# In[63]:


#✅ 2. Find Factorial of a Number
def factorial(num):
    factorial=1
    for i in range(num,0,-1):
        factorial*=i
    return factorial
factorial(5)


# In[67]:


#✅ 3. Count Vowels in a String
def countvow(string1):
    count=0
    for i in string1:
        if(i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U"):
            count+=1
    return count
countvow("shabaul")


# In[68]:


#✅ 4. Find the Maximum Number in a List
def maxnum(mylist):
    maxx=mylist[0]
    for i in range(len(mylist)):
        if(mylist[i]>maxx):
            maxx=mylist[i]
    return maxx
maxnum([3,2,4,5,6,787654,23])


# In[70]:


# ✅ 5. Palindrome Checker
# Write a function that checks whether a string is a palindrome
def palcheck(string2):
    start=0
    end=len(string2)-1
    count=0
    for i in range(len(string2)//2):
        if(string2[start]!=string2[end]):
            count=1
            break
        start+=1
        end-=1
    if(count==0):
        print("Palindrome")
    else:
        print("Not a palindrome")
palcheck("SARAS")


# In[71]:


# 1. Write a program to print all natural numbers from 1 to n. – using while loop
def natural(n):
    for i in range(1,n+1):
        print(i,end=" ")
natural(6)


# In[87]:


def nat(n):
    i=1
    while(i<=n):
        print(i,end=" ")
        i+=1
nat(10)


# In[72]:


#2. Write a program to print all natural numbers in reverse (from n to 1).
def rev(n):
    for i in range(n,0,-1):
        print(i,end=" ")
rev(6)


# In[86]:


def rev(n):
    i=1
    while(n>=i):
        print(n,end=" ")
        n-=1
rev(10)


# In[79]:


#3. Write a program to print all alphabets from a to z.
def alpha(alp):
    for i in range(alp,123):
        print(chr(i),end=" ")
alpha(97)


# In[84]:


def alppr(alp):
    while(alp<=122):
        print(chr(alp),end=" ")
        alp+=1
alppr(97)


# In[82]:


#4. Write a program to print all even numbers between 1 to 100.
def eve(num):
    for i in range(1,num+1):
        if(i%2==0):
            print(i,end=" ")
eve(100)


# In[83]:


def eve(num):
    i=1
    while(i<num):
        if(i%2==0):
            print(i,end=" ")
        i+=1
eve(100)


# In[90]:


#5. Write a program to find the sum of all odd numbers between 1 to n.
def summodd(n):
    summ=0
    i=1
    while(i<=n):
        if(i%2!=0):
            summ+=i
        i+=1
    return summ
summodd(100)


# In[91]:


#6. Write a program to count the number of digits in a number.
def countdig(num):
    count=0
    while(num>0):
        count+=1
        num=num//10
    return(count)
countdig(3456789)


# In[92]:


#7. Write a program to calculate the sum of digits of a number.
def sumdig(num):
    summ=0
    while(num>0):
        digit=num%10
        summ+=digit
        num=num//10
    return summ
sumdig(23456)


# In[94]:


#8. Write a program to find the first and last digit of a number.
def fld(num):
    last_digit=num%10
    while(num>0):
        if(num<10):
            print("first_digit is:",num)
        num=num//10
    print("last_digit is:",last_digit)
fld(234567)


# In[95]:


num=int(input("enter the number:"))
last_digit=num%10
while(num>=10):
    num=num//10
print("first digit is:",num)
print("last digit is:",last_digit)


# In[96]:


def digitcheck(num):
    last_digit=num%10
    while(num>=10):
        num=num//10
    print("first digit is:",num)
    print("last digit is:",last_digit)
digitcheck(98632498632)


# In[97]:


#9. Write a program to find the sum of first and last digit of a number.
def flds(num):
    last_digit=num%10
    while(num>=10):
        num=num//10
    first_digit=num
    print("first_digit is:",first_digit)
    print("last_digit is:",last_digit)
    summ=first_digit+last_digit
    return summ
flds(3456789)


# In[1]:


#10.Write a program to enter a number and print its reverse.
def revnum(num):
    while(num>0):
        digit=num%10
        print(digit,end=" ")
        num=num//10
revnum(2345678)


# In[2]:


#11.Write a program to find the power of a number.
def pownum(number,degree):
    power=number**degree
    return power
pownum(2,3)



# In[5]:


num=int(input("enter the number:"))
degree=int(input("enter the degree"))
power=1
while(degree>0):
    power*=num
    degree-=1
print(power)


# In[2]:


#12.Write a program to find all factors of a number.
def factors(num):
    i=1
    while(i<=num):
        if(num%i==0):
            print(i,end=" ")
        i+=1
factors(100)


# In[4]:


#13.Write a program to calculate the factorial of a number.
def factoriall(num):
    factorial=1
    i=1
    while(i<=num):
        factorial*=i
        i+=1
    return(factorial)
factoriall(5)


# In[7]:


#14.Write a program to find LCM of two numbers.(using for loop and max function)
def lcm(n,m):
    a=n
    b=m
    LCM=1
    for i in range(2,max(m,n)+1):
        while(a%i==0 or b%i==0):
            LCM*=i
            if(a%i==0):
                a=a//i
            if(b%i==0):
                b=b//i
    print(LCM)
lcm(2,4)




# In[20]:


#15.Write a program to check whether a number is Prime number or not.
def isprime(num):
    count=0
    if(num<=1):
        print("prime number is not less than or equal to 1")
    else:
        for i in range(2,num):
            if(num%i==0):
                count=1
                break
        if(count==0):
            print("prime")
        else:
            print("not a prime")
isprime(4)


# In[23]:


# 16.Write a program to print all Prime numbers between 1 to n.
def primerange(n):
    for i in range(2,n+1):
        count=0
        for j in range(2,i):
            if(i%j==0):
                count=1
                break
        if(count==0):
            print(i,end=" ")
primerange(7)


# In[25]:


#17.Write a program to find all prime factors of a number.
def primefact(num):
    for i in range(2,num):
        if(num%i==0):
            count=0
            for j in range(2,i):
                if(i%j==0):
                    count=1
                    break
            if(count==0):
                print(i)
primefact(8)


# In[36]:


# 18.Write a program to check whether a number is an Armstrong number or not.
# a. An Armstrong number is a n-digit number that is equal to the sum
# of the nth power of its digits. For example –
# 6 = 61 = 6
# 371 = 33 + 73 + 13 = 371
def armstrong(num):
    sum_power_digit=0
    original=num
    while(num>0):
        digit=num%10
        power_digit=digit**(len(str(original)))
        sum_power_digit+=power_digit
        num=num//10
    if(sum_power_digit==original):
        print("Armstrong")
    else:
        print("Not an armstrong")
armstrong(371)


# In[3]:


# 19.Write a program to check whether a number is Strong number or not
# a. Strong number is a special number whose sum of factorial of digits is equal to the original number.
# For example: 145 is a strong number. Since, 1! + 4! + 5! = 145
def strong(num):
    original=num
    sum_factorial=0
    while(num>0):
        digit=num%10
        factorial=1
        while(digit>0):
            factorial*=digit
            digit-=1
        sum_factorial+=factorial
        num=num//10
    if(sum_factorial==original):
        print("Strong number")
    else:
        print("Not a strong number")
strong(145)


# In[7]:


# #20.Write a program to check whether a number is perfect number or not
# a. Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
# For example: 6 is the first perfect number
# Proper divisors of 6 are 1, 2, 3
# Sum of its proper divisors = 1 + 2 + 3 = 6.
# Hence 6 is a perfect number.
def perfect(num):
    original=num
    i=1
    summ=0
    while(i<num):
        if(num%i==0):
            summ+=i
        i+=1
    if(summ==original):
        print("Perfect number")
    else:
        print("Not a perfect number")
perfect(6)


# For a perfect number, we use proper divisors, which means:
# All positive divisors of the number excluding the number itself

# So for 6:
# Divisors of 6:1,2,3,6

# But proper divisors:1,2,3
# We exclude 6 itself.


# In[12]:


# 21.Write a program to print fibonacci series upto n terms
# a. Fibonacci series is a series of numbers where the current number is the sum of the previous two terms. 
# For Example: 0, 1, 1, 2, 3, 5,8, 13, 21, ... , (n-1th + n-2th)
def fibo(n):
    first_term=0
    second_term=1
    print(first_term,end=" ")
    print(second_term,end=" ")
    for i in range(2,n):
        next_term=first_term+second_term
        print(next_term,end=" ")
        first_term=second_term
        second_term=next_term
fibo(8)    



# In[20]:


# 22.Write a program to find ones complement of a binary number
# a. One's complement of a binary number is defined as value obtained by inverting all binary bits. It is the result of swapping all
# 1s to 0s and all 0s to 1s.
def binary(num):
    binary=bin(num)[2:]
    print(binary)
    complement=""
    for bit in binary:
        if(bit=="0"):
            complement+="1"
        else:
            complement+="0"
    print(complement)
binary(8)


# In[ ]:




