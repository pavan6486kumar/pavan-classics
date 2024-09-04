#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky = E+W)

def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def add():
    first_number = e.get()
    global f_num
    global symbol
    symbol = "add"
    f_num = int(first_number)
    e.delete(0, END)

def sub():
    first_number = e.get()
    global f_num
    global symbol
    symbol = "sub"
    f_num = int(first_number)
    e.delete(0, END)

def mul():
    first_number = e.get()
    global f_num
    global symbol
    symbol = "mul"
    f_num = int(first_number)
    e.delete(0, END)

def div():
    first_number = e.get()
    global f_num
    global symbol
    symbol = "div"
    f_num = int(first_number)
    e.delete(0, END)

def mod():
    first_number = e.get()
    global f_num
    global symbol
    symbol = "mod"
    f_num = int(first_number)
    e.delete(0, END)

def power():
    first_number = e.get()
    global f_num
    global symbol
    symbol = "power"
    f_num = int(first_number)
    e.delete(0, END)
    
def equal():
    l_num = e.get()
    e.delete(0, END)
    if symbol == "add":
        e.insert(0, str(f_num + int(l_num)))
    elif symbol == "sub":
        e.insert(0, str(f_num - int(l_num)))
    elif symbol == "mul":
        e.insert(0, str(f_num * int(l_num)))
    elif symbol == "div":
        e.insert(0, str(f_num / int(l_num)))
    elif symbol == "mod":
        e.insert(0, str(f_num % int(l_num)))
    else:
        e.insert(0, str(f_num ** int(l_num)))

status = Label(root, text = "pavan's arthmetic calculator",relief = SUNKEN, anchor = E)    

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=add)
button_sub = Button(root, text="-", padx=40, pady=20, command=sub)
button_mul = Button(root, text="*", padx=40, pady=20, command=mul)
button_div = Button(root, text="/", padx=40, pady=20, command=div)
button_mod = Button(root, text="%", padx=40, pady=20, command=mod)
button_pow = Button(root, text="^", padx=40, pady=20, command=power)
button_clear = Button(root, text="Clear", padx=80, pady=20, command=clear)
button_equal = Button(root, text="=", padx=87, pady=20, command=equal)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_mod.grid(row=4, column=0)
button_pow.grid(row=4, column=2)
button_clear.grid(row=5, column=0, columnspan=2)
button_equal.grid(row=5, column=2, columnspan=2)
status.grid(row=6,column=0,columnspan=4,sticky = W+E)

root.mainloop()


# In[ ]:




