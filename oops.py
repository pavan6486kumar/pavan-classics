#!/usr/bin/env python
# coding: utf-8

# In[2]:


#creating class
class student:
    #defining init constructor
    def __init__(self,name,rollno,year_branch):
        self.name = name
        self.rollno = rollno
        self.year_branch = year_branch
        
    def introduction(self):
        print("hello my name is",self.name)
        print("my roll no is",self.rollno)
        print("i am studying",self.year_branch)
        print("\n")
        
s1 = student("pavan",101,"btech 3rd year CSE")
s2 = student("mohan",102,"btech 3rd year CSE") 
s3 = student("sharfuddin",103,"btech 3rd year CSE")
s4 = student("ansar",104,"btech 3rd year ECE")
s5 = student("sabeer",105,"btech 3rd year EEE")
s6 = student("musharaf",106,"btech 2nd year CSE")

s1.introduction()
s2.introduction()
s3.introduction()
s4.introduction()
s5.introduction()
s6.introduction()


# In[1]:


class employee:
    def __init__(self,name,empid,salary):
        self.name = name
        self.empid = empid
        self.salary = salary
    
    def sal_allocation(self):
        if self.salary>70000:
            print("name :",self.name,"employee id :",self.empid,"salary :",self.salary,"bonus :",self.salary*0.15,"net salary :",(self.salary+self.salary*0.15))
        else:
            print("name :",self.name,"employee id :",self.empid,"salary :",self.salary,"bonus :",self.salary*0.1,"net salary :",(self.salary+self.salary*0.1))
            
            
e1 = employee("pavan",101,60000)
e2= employee("mohan",102,80000)
e3= employee("sharfu",103,75000)
e4= employee("basha",104,70000)

e1.sal_allocation()
e2.sal_allocation()
e3.sal_allocation()
e4.sal_allocation()


# In[ ]:




