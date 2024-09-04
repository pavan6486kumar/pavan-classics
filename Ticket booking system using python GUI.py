#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import messagebox
import openpyxl

def book_ticket():
    total_tck = 58
    details = {"names":[],"ages":[],"route":[],"price":[],"no of tickets":[]}
    count = 0
    
    def submit():
        nonlocal total_tck, count
        name = name_entry.get()
        age = int(age_entry.get())
        no_of_tickets = int(tickets_entry.get())
        from_place = from_var.get()
        to_place = to_var.get()
        
        route = f"{from_place} to {to_place}"
        
        price = calculate_price(from_place, to_place)
        
        if total_tck >= no_of_tickets:
            amount = price * no_of_tickets
            gst = amount * 0.08
            total_amount = amount + gst
            
            details["names"].append(name)
            details["ages"].append(age)
            details["route"].append(route)
            details["price"].append(int(total_amount))
            details["no of tickets"].append(no_of_tickets)
            
            ticket_label.config(text=f"Total amount: {total_amount}")
            count += 1
            total_tck -= no_of_tickets
            tickets_left_label.config(text=f"Tickets left: {total_tck}")
            
            show_details()
        else:
            ticket_label.config(text="Tickets not available!")
    
    def calculate_price(from_place, to_place):
        if (from_place == "Anantapur" and to_place == "Kadiri") or (from_place == "Kadiri" and to_place == "Anantapur"):
            return 140
        elif (from_place == "Anantapur" and to_place == "Dharmavaram") or (from_place == "Dharmavaram" and to_place == "Anantapur"):
            return 70
        elif (from_place == "Anantapur" and to_place == "Bathalapalli") or (from_place == "Bathalapalli" and to_place == "Anantapur"):
            return 40
        elif (from_place == "Anantapur" and to_place == "Mudigubba") or (from_place == "Mudigubba" and to_place == "Anantapur"):
            return 90
        elif (from_place == "Kadiri" and to_place == "Mudigubba") or (from_place == "Mudigubba" and to_place == "Kadiri"):
            return 50
        elif (from_place == "Kadiri" and to_place == "Dharmavaram") or (from_place == "Dharmavaram" and to_place == "Kadiri"):
            return 100
        elif (from_place == "Kadiri" and to_place == "Bathalapalli") or (from_place == "Bathalapalli" and to_place == "Kadiri"):
            return 85
        elif (from_place == "Bathalapalli" and to_place == "Mudigubba") or (from_place == "Mudigubba" and to_place == "Bathalapalli"):
            return 45
        elif (from_place == "Bathalapalli" and to_place == "Dharmavaram") or (from_place == "Dharmavaram" and to_place == "Bathalapalli"):
            return 30
        elif (from_place == "Dharmavaram" and to_place == "Mudigubba") or (from_place == "Mudigubba" and to_place == "Dharmavaram"):
            return 60
        else:
            return 0
    
    def show_details():
        msg = ""
        for i in range(count):
            msg += f"\nBooking Details of passenger {i+1}\n"
            msg += "**********************************\n"
            msg += f"name : {details['names'][i]}\n"
            msg += f"age : {details['ages'][i]}\n"
            msg += f"route : {details['route'][i]}\n"
            msg += f"number of tickets booked : {details['no of tickets'][i]}\n"
            msg += f"price : {details['price'][i]}\n\n"
        messagebox.showinfo("Booking Details", msg)
    
    def save_to_excel():
        wb = openpyxl.Workbook()
        sheet = wb.active
        
        sheet.append(["Name", "Age", "Route", "Tickets", "Price"])
        
        for i in range(count):
            name = details["names"][i]
            age = details["ages"][i]
            route = details["route"][i]
            tickets = details["no of tickets"][i]
            price = details["price"][i]
            
            sheet.append([name, age, route, tickets, price])
        
        wb.save("booking_details.xlsx")
        messagebox.showinfo("Save Successful", "Booking details saved to booking_details.xlsx")

    root = tk.Tk()
    root.title("Ticket Booking System")
    
    tk.Label(root, text="Name:").grid(row=0, column=0)
    tk.Label(root, text="Age:").grid(row=1, column=0)
    tk.Label(root, text="No. of Tickets:").grid(row=2, column=0)
    tk.Label(root, text="From:").grid(row=3, column=0)
    tk.Label(root, text="To:").grid(row=4, column=0)
    tk.Label(root, text="Ticket Info:").grid(row=5, column=0)
    tk.Label(root, text="Tickets Left:").grid(row=6, column=0)
    
    name_entry = tk.Entry(root)
    age_entry = tk.Entry(root)
    tickets_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)
    age_entry.grid(row=1, column=1)
    tickets_entry.grid(row=2, column=1)
    
    from_var = tk.StringVar()
    to_var = tk.StringVar()
    
    places = ["Anantapur", "Kadiri", "Dharmavaram", "Bathalapalli", "Mudigubba"]
    
    from_dropdown = tk.OptionMenu(root, from_var, *places)
    from_dropdown.grid(row=3, column=1)
    
    to_dropdown = tk.OptionMenu(root, to_var, *places)
    to_dropdown.grid(row=4, column=1)
    
    ticket_label = tk.Label(root, text="")
    tickets_left_label = tk.Label(root, text=total_tck)
    
    ticket_label.grid(row=5, column=1)
    tickets_left_label.grid(row=6, column=1)
    
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=7, column=0, columnspan=2)
    
    save_button = tk.Button(root, text="Save", command=save_to_excel)
    save_button.grid(row=8, column=0, columnspan=2)
    
    root.mainloop()

book_ticket()


# In[ ]:




