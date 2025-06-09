from tkinter import *
from tkinter import messagebox

a = Tk()

def add_data():
    name = e1.get()
    phone = e2.get()
    email = e3.get()
    address = e4.get()

    if len(phone) != 10 or not phone.isdigit():
        messagebox.showerror("Invalid number", "Phone number must be exactly 10 digits.")
    else:
        with open('Contact_book.txt', 'a+') as f:
            f.write(f"{name},{phone},{email},{address}\n")
            messagebox.showinfo("Success", "Contact added successfully.")
        reset_fields()
        display_data()

def delete_data():
    name = e1.get()
    phone = e2.get()

    if not name or not phone:
        messagebox.showerror("Input Error", "Please enter both name and phone number to delete.")
        return

    try:
        found = False
        with open('Contact_book.txt', 'r') as f:
            lines = f.readlines()

        with open('Contact_book.txt', 'w') as f:
            for line in lines:
                if not (name in line and phone in line):
                    f.write(line)
                else:
                    found = True

        if found:
            messagebox.showinfo("Deleted", "Contact deleted successfully.")
        else:
            messagebox.showinfo("Not Found", "Contact not found.")
        reset_fields()
        display_data()
    except FileNotFoundError:
        messagebox.showerror("File Error", "Contact book file not found.")

def update_data():
    name = e1.get()
    phone = e2.get()
    email = e3.get()
    address = e4.get()

    if not name or not phone:
        messagebox.showerror("Input Error", "Please enter name and phone number to update.")
        return

    try:
        updated = False
        with open('Contact_book.txt', 'r') as f:
            lines = f.readlines()

        with open('Contact_book.txt', 'w') as f:
            for line in lines:
                if name in line and phone in line:
                    f.write(f"{name},{phone},{email},{address}\n")
                    updated = True
                else:
                    f.write(line)

        if updated:
            messagebox.showinfo("Updated", "Contact updated successfully.")
        else:
            messagebox.showinfo("Not Found", "Contact not found.")
        reset_fields()
        display_data()
    except FileNotFoundError:
        messagebox.showerror("File Error", "Contact book file not found.")

def view_data():
    name = e1.get()
    phone = e2.get()

    try:
        with open('Contact_book.txt', 'r') as f:
            for line in f:
                if name in line or phone in line:
                    messagebox.showinfo("Contact Found", line.strip())
                    return
        messagebox.showinfo("Not Found", "No matching contact found.")
    except FileNotFoundError:
        messagebox.showerror("File Error", "Contact book file not found.")

def reset_fields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def display_data():
    listbox.delete(0, END)
    try:
        with open('Contact_book.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                listbox.insert(END, line.strip())
    except FileNotFoundError:
        messagebox.showerror("File Error", "Contact book file not found.")

# GUI Layout
Label(a, text="Contact Book", font="Lucida 14 bold").grid(row=0, column=1, pady=10)

Label(a, text="Name", font="Lucida 12").grid(row=1, column=0, padx=10, pady=5, sticky=E)
e1 = Entry(a, font=("Lucida 10"))
e1.grid(row=1, column=1)

Label(a, text="Phone Number", font="Lucida 12").grid(row=2, column=0, padx=10, pady=5, sticky=E)
e2 = Entry(a, font=("Lucida 10"))
e2.grid(row=2, column=1)

Label(a, text="Email", font="Lucida 12").grid(row=3, column=0, padx=10, pady=5, sticky=E)
e3 = Entry(a, font=("Lucida 10"))
e3.grid(row=3, column=1)

Label(a, text="Address", font="Lucida 12").grid(row=4, column=0, padx=10, pady=5, sticky=E)
e4 = Entry(a, font=("Lucida 10"))
e4.grid(row=4, column=1)

# Buttons
Button(a, text="Add", font="Lucida 10", command=add_data).grid(row=5, column=0, pady=10)
Button(a, text="Delete", font="Lucida 10", command=delete_data).grid(row=5, column=1, pady=10)
Button(a, text="Update", font="Lucida 10", command=update_data).grid(row=6, column=0, pady=5)
Button(a, text="View", font="Lucida 10", command=view_data).grid(row=6, column=1, pady=5)
Button(a, text="Reset", font="Lucida 10", command=reset_fields).grid(row=7, column=0, columnspan=2, pady=10)

# Listbox to show data
listbox = Listbox(a, width=60, height=10, font=("Lucida 10"))
listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

display_data()

a.geometry("600x500")
a.mainloop()
