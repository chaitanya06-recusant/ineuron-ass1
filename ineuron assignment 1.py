#!/usr/bin/env python
# coding: utf-8

# In[6]:


l = list(range(2000,3200))
m = []

for i in l:
        if i % 5 == 0:
            continue
        elif i % 7 == 0 : 
            m.append(i)
            
print(m) 


           


# In[10]:


a = input("enter first name: ")
b = input("enter the last name: ")

print("hello " + b + " " + a )

 
    


# In[11]:


d = int(input("enter the diameter: "))
pi = 22/7
r = d/2
v = (4/3)*pi*r**3

print("hence, the volume is ", v)


# In[ ]:


print("enter a sequence of numbers")
i = int(input())
l = [i]
for i in l:
    print('enter the next number')
    i = int(input(l))
    l.append(i)
print(l)    
    


# In[1]:


for i in range(0, 11):
    if i<=5:
        for j in range(0, i+1):
            print("* ",end="")
    else:
        for j in range(11,i,-1):
            print("* ",end="")
    print()        

    


# In[4]:


s = input()
j = " "

for i in s:
    j = i + j
    
print("The reversed word is: ",j)


# In[5]:


print("WE THE PEOPLE OF INDIA,", end="")
print()
print("      having solemnly resolved to constitute India into a SOVEREIGN,!", end="")
print()
print("            SOCIAlIST, SECULAR, DEMOCRATIC REPUBLIC", end="")
print()
print("              and secure to all its citizens", end="")


# In[ ]:





# In[ ]:




