#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


# In[3]:


for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()


# In[5]:


for i in range(1,4):
    print("student",i)
    for j in range(1,4):
        print("subject",j)


# In[12]:


for i in range(1,4):
    print("student",i)
    for j in range(1,4):
        print("subject",j,end=" ")
    print()


# In[13]:


for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()


# In[14]:


for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")
    print()


# In[16]:


# 1111
# 2222
# 3333
for i in range(1,4):
    for j in range(1,5):
        print(i,end="")
    print()


# In[19]:


# 3333
# 2222
# 1111
for i in range(3,0,-1):
    for j in range(1,5):
        print(i,end="")
    print()





# In[22]:


# 234
# 234
# 234
for i in range(1,4):
    for j in range(2,5):
        print(j,end="")
    print()


# In[24]:


# 123
# 456
# 789
num=1
for i in range(1,4):
    for j in range(1,4):
        print(num,end="")
        num+=1
    print()


# In[40]:


# 987
# 654
# 321
num=9
for i in range(1,4):
    for j in range(1,4):
        print(num,end="")
        num-=1
    print()


# In[42]:


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[44]:


# 5
# 55
# 555
# 5555
num=5
for i in range(1,5):
    for j in range(1,i+1):
        print("5",end="")
    print()



# In[47]:


# 1
# 12
# 123
for i in range(1,4):
    num=1
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()


# In[50]:


# 7
# 65
# 432
num=7
for i in range(1,4):
    for j in range(1,i+1):
        print(num,end="")
        num-=1
    print()


# In[54]:


# 7
# 66
# 555
# 4444
num=7
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end="")
    num-=1
    print()



# In[56]:


# 1
# 23
# 456
# 78910
num=1
for i in range(1,5):
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()


# In[57]:


# 65
# 6566
# 656667
# 65666768
for i in range(1,5):
    num=65
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()


# In[58]:


# ****
# ***
# **
# *
for i in range(1,5):
    for j in range(1,6-i):
        print("*",end="")
    print()



# In[60]:


# 1111
# 222
# 33
# 4
num=1
for i in range(1,5):
    for j in range(1,6-i):
        print(num,end="")
    num+=1
    print()


# In[65]:


# 1234
# 123
# 12
# 1
for i in range(1,5):
    num=1
    for j in range(1,6-i):
        print(num,end="")
        num+=1
    print()



# In[67]:


# 4321
# 432
# 43
# 4
for i in range(1,5):
    num=4
    for j in range(1,6-i):
        print(num,end="")
        num-=1
    print()


# In[69]:


# 1234
# 567
# 89
# 10
num=1
for i in range(1,5):
    for j in range(1,6-i):
        print(num,end="")
        num+=1
    print()


# In[72]:


# A
# AB
# ABC
for i in range(1,4):
    alpha=65
    for j in range(1,i+1):
        print(chr(alpha),end="")
        alpha+=1
    print()


# In[73]:


# ABCD
# ABC
# AB
# A
for i in range(1,5):
    alpha=65
    for j in range(1,6-i):
        print(chr(alpha),end="")
        alpha+=1
    print()



# In[86]:


# ---*
# --**
# -***
# ****
for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


# In[88]:


#    * 
#   * * 
#  * * * 
# * * * * 
for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[89]:


# ****
# -***
# --**
# ---*
for i in range(1,5):
    for j in range(1,i):
        print("-",end="")
    for j in range(1,6-i):
        print("*",end="")
    print()


# In[90]:


# * * * * 
#  * * * 
#   * * 
#    * 
for i in range(4,0,-1):
    for j in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[95]:


# *
# **
# * *
# *  *
# *****
for i in range(1,6):
    for j in range(1,i+1):
        if(i==5 or j==1 or i==j):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[97]:


# *
# **
# * *
# *  *
# *   *
# *    *
# *     *
# *      *
# *       *
# *        *
# *         *
# *          *
# *           *
# *            *
# *             *
# *              *
# *               *
# *                *
# *                 *
# ********************
for i in range(1,21):
    for j in range(1,i+1):
        if(i==20 or j==1 or i==j):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[129]:


# ******
# *---*
# *--*
# *-*
# **
# *
for i in range(1,7):
    for j in range(1,8-i):
        if(i==1 or j==1 or j==7-i):
            print("*",end="")
        else:
            print("-",end="")
    print()


# In[130]:


# ----*
# ---**
# --***
# -****
# *****
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


# In[131]:


# ----*
# ---**
# --*?*
# -*??*
# *****
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,i+1):
        if(i==5 or j==1 or i==j):
            print("*",end="")
        else:
            print("?",end="")
    print()


# In[133]:


#    * 
#   * * 
#  * * * 
# * * * * 
for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[134]:


# ****
# -***
# --**
# ---*
for i in range(1,5):
    for j in range(1,i):
        print("-",end="")
    for j in range(1,6-i):
        print("*",end="")
    print()


# In[135]:


# * * * * 
#  * * * 
#   * * 
#    * 
for i in range(4,0,-1):
    for j in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[137]:


#        * 
#       * * 
#      * * * 
#     * * * * 
#    * * * * * 
#   * * * * * * 
#  * * * * * * * 
# * * * * * * * * 
for i in range(1,9):
    for j in range(1,9-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[138]:


# * * * * * * * 
#  * * * * * * 
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 
for i in range(8,0,-1):
    for j in range(1,9-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[143]:


# 1 2 3 4 
#  1 2 3 
#   1 2 
#    1 
for i in range(4,0,-1):
    for j in range(1,5-i):
        print(" ",end="")
    num=1
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()


# In[144]:


#   A 
#  A B 
# A B C 
for i in range(1,4):
    for j in range(1,4-i):
        print(" ",end="")
    alpha=65
    for j in range(1,i+1):
        print(chr(alpha),end=" ")
        alpha+=1
    print()


# In[147]:


# *
# **
# ***
# ****
# ***
# **
# *
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,5):
    for j in range(1,6-i):
        print("*",end="")
    print()


# In[150]:


# *****
# -****
# --***
# ---**
# ----*
# ---**
# --***
# -****
# *****
for i in range(1,5):
    for j in range(1,i):
        print("-",end="")
    for j in range(1,7-i):
        print("*",end="")
    print()
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


# In[151]:


# ****
# -****
# --****
# ---****
for i in range(1,5):
    for j in range(1,i):
        print("-",end="")
    for j in range(1,5):
        print("*",end="")
    print()


# In[152]:


# ******
# *    *
# *    *
# ******
for i in range(1,5):
    for j in range(1,7):
        if(i==1 or i==4 or j==1 or j==6):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[153]:


# A
# AB
# ABC
# ABCD
# ABCDE
for i in range(1,6):
    alpha=65
    for j in range(1,i+1):
        print(chr(alpha),end="")
        alpha+=1
    print()



# In[154]:


# A
# BB
# CCC
# DDDD
# EEEEE
alpha=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(alpha),end="")
    alpha+=1
    print()



# In[162]:


# E
# DE
# CDE
# BCDE
# ABCDE

for i in range(1,6):
    alpha=70-i
    for j in range(1,i+1):
        print(chr(alpha),end="")
        alpha+=1
    print()



# In[163]:


# ----*
# ---**
# --***
# -****
# *****
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


# In[164]:


# ----1
# ---12
# --123
# -1234
# 12345
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    num=1
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()


# In[165]:


# 12345
# -1234
# --123
# ---12
# ----1
for i in range(1,6):
    for j in range(1,i):
        print("-",end="")
    num=1
    for j in range(1,7-i):
        print(num,end="")
        num+=1
    print()


# In[166]:


# ABCDE
# -ABCD
# --ABC
# ---AB
# ----A
for i in range(1,6):
    for j in range(1,i):
        print("-",end="")
    alpha=65
    for j in range(1,7-i):
        print(chr(alpha),end="")
        alpha+=1
    print()


# In[168]:


# ----* * * * * 
# ---* * * * * 
# --* * * * * 
# -* * * * * 
# * * * * *
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,6):
        print("*",end=" ")
    print()


# In[169]:


# ----1 2 3 4 5 
# ---1 2 3 4 5 
# --1 2 3 4 5 
# -1 2 3 4 5 
# 1 2 3 4 5 
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    num=1
    for j in range(1,6):
        print(num,end=" ")
        num+=1
    print()


# In[170]:


# ----A B C D E 
# ---A B C D E 
# --A B C D E 
# -A B C D E 
# A B C D E 
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    alpha=65
    for j in range(1,6):
        print(chr(alpha),end=" ")
        alpha+=1
    print()


# In[172]:


#    *   
#   ***  
#  ***** 
# *******
for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()


# In[174]:


# *******
# -*****
# --***
# ---*
for i in range(4,0,-1):
    for j in range(1,5-i):
        print("-",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()


# In[196]:


# ---*
# --* *
# -*   *
# *******
for i in range(1,5):
    for j in range(1,5-i):
        print("-",end="")
    for j in range(1,2*i):
        if(i==4 or j==1 or j==2*i-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[197]:


# *******
# -*   *
# --* *
# ---*
for i in range(4,0,-1):
    for j in range(1,5-i):
        print("-",end="")
    for j in range(1,2*i):
        if(i==4 or j==1 or j==2*i-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[200]:


# *
# **
# ***
# ****
# ***
# **
# *
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,5):
    for j in range(1,6-i):
        print("*",end="")
    print()


# In[203]:


# ---*
# --**
# -***
# ****
# -***
# --**
# ---*
for i in range(1,4):
    for j in range(1,5-i):
        print("-",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,5):
    for j in range(1,i):
        print("-",end="")
    for j in range(1,6-i):
        print("*",end="")
    print()


# In[206]:


# ---*
# --***
# -*****
# *******
# -*****
# --***
# ---*
for i in range(1,4):
    for j in range(1,5-i):
        print("-",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(4,0,-1):
    for j in range(1,5-i):
        print("-",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()


# In[207]:


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
for i in range(1,6):
    num=1
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()



# In[208]:


# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
for i in range(1,6):
    num=1
    for j in range(1,7-i):
        print(num,end=" ")
        num+=1
    print()



# In[210]:


# 1 
# 1 2 
# 1   3 
# 1     4 
# 1 2 3 4 5 
for i in range(1,6):
    num=1
    for j in range(1,i+1):
        if(i==5 or j==1 or i==j):
            print(num,end=" ")
        else:
            print(" ",end=" ")
        num+=1
    print()


# In[211]:


# ----1 
# ---1 2 
# --1   3 
# -1     4 
# 1 2 3 4 5 
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    num=1
    for j in range(1,i+1):
        if(j==1 or i==5 or i==j):
            print(num,end=" ")
        else:
            print(" ",end=" ")
        num+=1
    print()



# In[214]:


# 12345
# 2  5
# 3 5
# 45
# 5
for i in range(1,6):
    num=i
    for j in range(1,7-i):
        if(i==1 or j==1 or j==6-i):
            print(num,end="")
        else:
            print(" ",end="")
        num+=1
    print()


# In[217]:


# ----*
# ---***
# --*****
# -*******
# *********
# -*******
# --*****
# ---***
# ----*
for i in range(1,5):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()


# In[221]:


# ----1
# ---123
# --12345
# -1234567
# 123456789
# -1234567
# --12345
# ---123
# ----1

for i in range(1,5):
    for j in range(1,6-i):
        print("-",end="")
    num=1
    for j in range(1,2*i):
        print(num,end="")
        num+=1
    print()
for i in range(5,0,-1):
    for j in range(1,6-i):
        print("-",end="")
    num=1
    for j in range(1,2*i):
        print(num,end="")
        num+=1
    print()


# In[228]:


# *********
# -*******
# --*****
# ---***
# ----*
# ---***
# --*****
# -*******
# *********
for i in range(5,1,-1):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()


# In[230]:


# 123456789
# -1234567
# --12345
# ---123
# ----1
# ---123
# --12345
# -1234567
# 123456789
for i in range(5,1,-1):
    for j in range(1,6-i):
        print("-",end="")
    num=1
    for j in range(1,2*i):
        print(num,end="")
        num+=1
    print()
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    num=1
    for j in range(1,2*i):
        print(num,end="")
        num+=1
    print()


# In[231]:


# ABCDEFGHI
# -ABCDEFG
# --ABCDE
# ---ABC
# ----A
# ---ABC
# --ABCDE
# -ABCDEFG
# ABCDEFGHI
for i in range(5,1,-1):
    for j in range(1,6-i):
        print("-",end="")
    alpha=65
    for j in range(1,2*i):
        print(chr(alpha),end="")
        alpha+=1
    print()
for i in range(1,6):
    for j in range(1,6-i):
        print("-",end="")
    alpha=65
    for j in range(1,2*i):
        print(chr(alpha),end="")
        alpha+=1
    print()


# In[232]:


# *****
# *   *
# *   *
# *   *
# *****
for i in range(1,6):
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[234]:


# 12345
# 1   5
# 1   5
# 1   5
# 12345
for i in range(1,6):
    num=1
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print(num,end="")
        else:
            print(" ",end="")
        num+=1
    print()


# In[235]:


# ABCDE
# A   E
# A   E
# A   E
# ABCDE
for i in range(1,6):
    alpha=65
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print(chr(alpha),end="")
        else:
            print(" ",end="")
        alpha+=1
    print()


# In[248]:


#     * 
#    * *   
#   *   *     
#  *     *       
# *       *         
#  *     *       
#   *   *     
#    * *   
#     * 
for i in range(1,5):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        if(j==1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        if(j==1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



# In[253]:


#     A 
#    A B 
#   A   C 
#  A     D 
# A       E 
#  A     D 
#   A   C 
#    A B 
#     A 
for i in range(1,5):
    for j in range(1,6-i):
        print(" ",end="")
    alpha=65
    for j in range(1,i+1):
        if(j==1 or i==j):
            print(chr(alpha),end=" ")
        else:
            print(" ",end=" ")
        alpha+=1
    print()
for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ",end="")
    alpha=65
    for j in range(1,i+1):
        if(j==1 or i==j):
            print(chr(alpha),end=" ")
        else:
            print(" ",end=" ")
        alpha+=1
    print()


# In[255]:


# ----*
# ---* *
# --*   *
# -*     *
# *       *
# -*     *
# --*   *
# ---* *
# ----*
for i in range(1,5):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,2*i):
        if(j==1 or j==2*i-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(5,0,-1):
    for j in range(1,6-i):
        print("-",end="")
    for j in range(1,2*i):
        if(j==1 or j==2*i-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# In[259]:


# ----A
# ---A C
# --A   E
# -A     G
# A       I
# -A     G
# --A   E
# ---A C
# ----A

for i in range(1,5):
    for j in range(1,6-i):
        print("-",end="")
    alpha=65
    for j in range(1,2*i):
        if(j==1 or j==2*i-1):
            print(chr(alpha),end="")
        else:
            print(" ",end="")
        alpha+=1
    print()
for i in range(5,0,-1):
    for j in range(1,6-i):
        print("-",end="")
    alpha=65
    for j in range(1,2*i):
        if(j==1 or j==2*i-1):
            print(chr(alpha),end="")
        else:
            print(" ",end="")
        alpha+=1
    print()


# In[265]:


# *--------*
# **------**
# ***----***
# ****--****
# **********
# ****--****
# ***----***
# **------**
# *--------*
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,11-2*i):
        print("-",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,11-2*i):
        print("-",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


# In[271]:


# **********
# ****--****
# ***----***
# **------**
# *--------*
# **------**
# ***----***
# ****--****
# **********
for i in range(5,1,-1):
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,11-2*i):
        print("-",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,11-2*i):
        print("-",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


# In[ ]:




