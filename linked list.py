#!/usr/bin/env python
# coding: utf-8

# In[1]:


#single linked list implementation
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
    
class linkedList:
    def __init__(self):
        self.head=None
        
    def add_begin(self,data):
        newNode=Node(data)
        newNode.ref=self.head
        self.head=newNode
        
    def add_end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        last=self.head
        while last.ref is not None:
            last=last.ref
        last.ref=newNode
        
    def add_before_val(self,val,data):
        n=self.head
        if n is None:
            print("linked list is empty.")
        elif n==val:
            add_begin(data)
        else:
            while n is not None:
                if n.ref.data==val:
                    break
                n=n.ref
            newNode=Node(data)
            newNode.ref=n.ref
            n.ref=newNode
            
    def add_after_val(self,val,data):
        n=self.head
        if n is None:
            print("linked list is empty.")
        elif n.ref==None:
            add_end(data)
        else:
            while n is not None:
                if n.data==val:
                    break
                n=n.ref
            newNode=Node(data)
            newNode.ref=n.ref
            n.ref=newNode
            
    def del_begin(self):
        if self.head is None:
            print("linked list is empty.")
        else:
            self.head=self.head.ref
            
    def del_end(self):
        n=self.head
        if n is None:
            print("linked list is empty.")
        elif n.ref is None:
            n=None
        else:
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
            
    def del_by_val(self,val):
        n=self.head
        if n is None:
            print("linked list is empty.")
            return
        elif n.data==val:
            self.head=self.head.ref
            return
        else:
            while n.ref is not None:
                if n.ref.data==val:
                    break
                n=n.ref
            if n.ref is None:
                print("node not found.")
            else:
                n.ref=n.ref.ref
            
    def print_list(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            while self.head is not None:
                print(self.head.data,end="--->")
                self.head=self.head.ref
                
                
ll1=linkedList()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_end(50)
ll1.add_end(40)
ll1.add_after_val(40,80)
ll1.add_before_val(10,90)
ll1.del_begin()
ll1.del_end()
ll1.del_by_val(20)
ll1.print_list()


# In[2]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class linkedList:
    def __init__(self):
        self.head=None
        
    def add_begin(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            n=self.head
            newNode.next=n
            n.prev=newNode
            self.head=newNode
            
    def add_end(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=newNode
            newNode.prev=n
            
    def add_after(self,val,data):
        if self.head is None:
            print("value not fount linked list is empty.")
        else:
            n=self.head
            while n is not None:
                if n.data==val:
                    break
                n=n.next
            if n is None:
                print("value not found.")
            else:
                newNode=Node(data)
                newNode.next=n.next
                newNode.prev=n
                if n.next is not None:
                    n.next.prev=newNode
                n.next=newNode
                
    def add_before(self,val,data):
        if self.head is None:
            print("value not fount linked list is empty.")
        else:
            n=self.head
            while n is not None:
                if n.data==val:
                    break
                n=n.next
            if n is None:
                print("value not found.")
            else:
                newNode=Node(data)
                newNode.next=n
                newNode.prev=n.prev
                if n.prev is not None:
                    n.prev.next=newNode
                else:
                    self.head=newNode
                n.prev=newNode
                
    def del_begin(self):
        if self.head is None:
            print("linked list is empty.")
        else:
            self.head=self.head.next
            self.head.prev=None
            
    def del_end(self):
        if self.head is None:
            print("linked list is empty.")
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None
            
    def del_by_val(self,val):
        if self.head is None:
            print("linked list is empty.")
        if self.head.data==val:
            self.del_begin()
        else:
            n=self.head
            while n is not None:
                if n.data==val:
                    break
                n=n.next
            if n is None:
                print("value not found.")
            elif n.next is None:
                self.del_end()
            else:
                n.next.prev=n.prev
                n.prev.next=n.next
                
    def print_ll_straight(self):
        if self.head is None:
            print("linked list is empty.")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="--->")
                n=n.next
    
    def print_ll_reverse(self):
        if self.head is None:
            print("linked list is empty.")
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            while n is not None:
                print(n.data,end="<---")
                n=n.prev
                
ll1=linkedList()
ll1.del_end()
ll1.add_begin(80)
ll1.add_begin(70)
ll1.add_before(70,50)
ll1.add_after(50,60)
ll1.add_begin(40)
ll1.add_end(90)
ll1.del_begin()
ll1.del_end()
ll1.del_by_val(80)
ll1.print_ll_straight()
print("")
ll1.print_ll_reverse()


# In[ ]:




