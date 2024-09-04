#!/usr/bin/env python
# coding: utf-8

# In[4]:


num = int(input("enter a number : "))
if num%2 == 0:
    print("Even")
else:
    print("Odd")


# In[8]:


num = int(input("enter a number : "))
if num>=0:
    print("Positive")
else:
    print("Negative")


# In[12]:


list1 = [12,58,95,64,76]
temp = list1[0]
list1[0] = list1[-1]
list1[-1] = temp
print(list1)


# In[14]:


num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
if num1>num2:
    print(num1,"is the largest number among the given numbers")
else:
    print(num2,"is the largest number among the given numbers")


# In[56]:


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
print(matrix)
print("\n")
print("the matrix for the given inputs : ")
for i in range(R):
    for j in range(C):
        print(matrix[i][j],end="\t")
    print()  


# In[54]:


dict1 = {"name":["pavan","arjun"],"age":[21,20],"m1":[98,95],"m2":[96,94],"m3":[97,96]}
print(dict1)

std1_total = dict1["m1"][0] + dict1["m2"][0] + dict1["m3"][0]
std1_avg = std1_total/3

std2_total = dict1["m1"][1] + dict1["m2"][1] + dict1["m3"][1]
std2_avg = std2_total/3

dict1.update({"average":[std1_avg,std2_avg]})
print(dict1)


# In[ ]:




