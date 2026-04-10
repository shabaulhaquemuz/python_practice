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


# In[32]:


#Q1 Write a program that takes an integer input from the user and checks whether the number is odd or even.
n=int(input("enter any number:"))
if(n%2==0):
    print("even")
else:
    print("odd")
#negative numbers can be even and odd. Also 0 is an even number.


# In[36]:


#Q2 Write a program that takes three numbers as input and prints the largest of the three.
n1=int(input("enter num1:"))
n2=int(input("enter num3:"))
n3=int(input("enter num3:"))
if(n1>n2 and n1>n3):
    print("n1 is largest")
elif(n2>n1 and n2>n3):
    print("n2 is largest")
else:
    print("n3 is largest")


# In[45]:


perc = int(input("Enter your percent: "))

if perc > 100 or perc < 0:
    print("Enter a valid value")
elif perc >= 90:
    print("Grade A")
elif perc >= 80:
    print("Grade B")
elif perc >= 70:
    print("Grade C")
else:
    print("Grade D")


# In[49]:


#Q3 Write a program to check if a given year is a leap year. 
#A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
year=int(input("enter the year:"))
if(year%4==0 and year%100!=0):
    print("leap year")
elif(year%400==0):
    print("leap year")
else:
    print("not a leap year")


# In[52]:


year=int(input("enter the year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not a leap year")


# In[50]:


#Q4 Write a program that takes a percentage (integer) as input and prints the corresponding grade based on the following criteria:
perc=int(input("enter your percent:"))
if(perc>100 or perc<0):
    print("enter a valid value")
elif(perc>=90 and perc<=100):
    print("grade A")
elif(perc>=80 and perc<90):
    print("grade B")
elif(perc>=70 and perc<80):
    print("garde C")
else:
    print("grade D")



# In[64]:


#Q6 Write a basic calculator program that takes two numbers and an operator (+, -, *, /) as input and 
#performs the specified operation. 
#Print the result based on the operation.
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
oper=input("enter operator:")
if(oper=="+"):
    result=num1+num2
    print("result is:", result)
elif(oper=="-"):
    result=num1-num2
    print("result is:", result)
elif(oper=="*"):
    result=num1*num2
    print("result is:", result)
elif(oper=="/"):
    result=num1/num2
    print("result is:", result)
else:
    print("enter the right operator")


# In[70]:


#Q8 Write a program that checks if a username and password entered by the user match the pre-set values
#username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print "Login Failed".
set_username="admin"
set_password="1234"
username=input("enter username:")
password=input("enter password:")
if(username==set_username and password==set_password):
    print("Login successful")
else:
    print("Login failed")


# In[75]:


#Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid
#triangle. A triangle is valid if the sum of any two sides is greater than the third side.
#Check conditions like a + b > c, b + c > a, and a + c > b.
a=int(input("side1:"))
b=int(input("side2:"))
c=int(input("side3:"))
if(a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b):
    print("valid triangle")
else:
    print("invalid triangle")


# In[81]:


#Q11 Write a program that calculates the discount for a product based on its price:
#If price is greater than 1000, discount is 10%
#If price is between 500 and 1000, discount is 5%
#Otherwise, no discount
#Print the final price after applying the discount.
price=int(input("enter the price:"))
if(price>=1000):
    discount=10/100*price
    sp=price-discount
    print("final price is:",sp)
elif(price>=500 and price<1000):
    discount=5/100*price
    sp=price-discount
    print("final price is:",sp)
else:
    print("no discount and price final price is:", price)


# In[90]:


#Q12 Write a program that takes the name of a month as input and prints the number of days in that month. 
#Consider leap years for February.
month=input("enter name of month:")
if(month=="January"):
    print("31 days")
elif(month=="February"):
    year=int(input("enter the year:"))
    if(year%4==0 and year%100!=0) or (year%400==0):
        print("leap year february has 29 days")
    else:
        print("non-leap year february has 28 days")
elif(month=="March"):
    print("31 days")
elif(month=="April"):
    print("30 days")
elif(month=="May"):
    print("31 days")
elif(month=="June"):
    print("30 days")
elif(month=="July"):
    print("31 days")
elif(month=="August"):
    print("31 days")
elif(month=="September"):
    print("30 days")
elif(month=="October"):
    print("31 days")
elif(month=="November"):
    print("30 days")
elif(month=="December"):
    print("31 days")
else:
    print("enter valid month")


# In[96]:


#Q13 Write a program that simulates a simple ATM. The user should be able to:
#Check balance
#Deposit money
#Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's choices.
card_pin = 1234
balance = 10000

choose_option = int(input("enter any option:"))

if (choose_option == 1):
    pin = int(input("enter your pin:"))
    if (pin == card_pin):
        print("your balance is:", balance)

elif (choose_option == 2):
    pin = int(input("enter your pin:"))
    if (pin == card_pin):
        deposit_amount = int(input("enter the deposit amount:"))
        balance = balance + deposit_amount
        print("your amount is deposited and new balance is:", balance)

elif (choose_option == 3):
    pin = int(input("enter your pin:"))
    if (pin == card_pin):
        withdrawl_amount = int(input("enter the withdrawl amount:"))
        if (withdrawl_amount > balance):
            print("you do not have sufficient money in your account")
        else:
            balance = balance - withdrawl_amount
            print("your amount is withdrawn and new balance is:", balance)


# In[ ]:




