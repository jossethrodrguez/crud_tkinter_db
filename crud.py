# Python CRUD SQlite APP.

# import dependencies
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import sqlite3

# GUI setup:

root = Tk()
root.title("SQlite App")
root.geometry("600x350")

# Variables:

employeeID = StringVar()
employeeName = StringVar()
employeeJobTitle = StringVar()
employeeSalary = StringVar()

appOption = StringVar()
appVersion = 1.0

appData = employeeName.get(), employeeJobTitle.get(), employeeSalary.get() 
appTree = ttk.Treeview(height=10, columns=('#0', '#1', '#2'))


userRecord = appTree.get_children()

# Desing:

appTree.place(x=0, y =130)

# Column 0
appTree.column("#0", width=100 )
appTree.heading("#0", text='ID', anchor=CENTER)

# Column 1
appTree.column("#01")
appTree.heading("#1", text='Name', anchor=CENTER)

# Column 2
appTree.column("#2")
appTree.heading("#2", text='Job', anchor=CENTER)

# Column 3
appTree.column("#3", width=100 )
appTree.heading("#3", text='Salary', anchor=CENTER)





# Functions:

def connect():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()

    try:
        cursor.execute(''' 

            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                job_title TEXT NOT NULL,
                salary INT NOT NULL
            )
        ''')

        messagebox.showinfo("Connection", "Created table employees")
    except:
        messagebox.showinfo("Connection", "Connection to database Success")

def remove():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()

    if messagebox.askyesno("Delete", "Are you sure you want to remove the table employees?"):
        cursor.execute("DROP TABLE employees")

        messagebox.showinfo("Connection", "Deleted table employees")
    else:
        pass

def close():
    appOption = 'Are you sure you to close the App ?'
    userValue = messagebox.askquestion(appOption)

    if userValue == 'yes':
        root.destroy()
    else:
        pass

def clean():
    employeeID.set("")
    employeeName.set("")
    employeeJobTitle.set("")
    employeeSalary.set("")

def message():
    appHelp = 'Welcome to SQlite App v', appVersion,'.\n\n','Python CRUD SQlite APP.\n\n Author: Josseth Rodriguez '
    

#### CRUD Methods ################################################# 
def create():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO employees VALUES(NULL,?,?,?)', (appData))
        connection.commit()
    except:
        messagebox.showwarning("Error", "Error in adding record to database")
        pass
    clean()
    read()
    
def read():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()

    for element in userRecord:
        appTree.remove(element)

    try:
        cursor.execute(' SELECT * employees')
        for row in cursor:
            appTree.insert('', 0, text=row[0], values=(row[1], row[2], row[3]))
    except:
        pass

def update():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()

    try:
        cursor.execute('UPDATE employees SET name = ?, job_title = ?, salary = ? ,WHERE id =' + employeeID.get(), (appData))
        connection.commit()
    except:
        messagebox.showwarning("Error", "Error in updating record to database")
        pass
    clean()
    read()

def delete():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()

    try:
        if messagebox.askyesno("Delete record from database", "Are you sure?"):
            cursor.execute('DELETE FROM employees WHERE id =' + employeeID.get())
            connection.commit()
    except:
        messagebox.showwarning("Error", "Error in deleting record from database")
        pass
    clean()
    read()

# widget:

menubar = Menu(root)

# Menu
menuBaseData = Menu(menubar, tearoff=0)

menuBaseData.add_command(label="New", command=connect)
menuBaseData.add_command(label="Remove", command=remove)
menuBaseData.add_command(label="Exit", command=close)
menubar.add_cascade(label="Start", menu=menuBaseData)

menuHelpData = Menu(menubar, tearoff=0)

menuHelpData.add_command(label="Clean", command= clean)
menuHelpData.add_command(label="About", menu=message())
menubar.add_cascade(label="Help", menu= menuHelpData)

# Labels and Textbox

# e  = entries
# l  = labels

e1 = Entry(root, textvariable=employeeID)

l2 = Label(root, text="Name")
l2.place(x=50, y=10)
e2 = Entry(root, textvariable=employeeName, width=50)
e2.place(x=100, y=10)

l3 = Label(root, text="Job")
l3.place(x=50, y=40)
e3 = Entry(root, textvariable=employeeJobTitle)
e3.place(x=100, y=40)

l4 = Label(root, text="Salary  ")
l4.place(x=280, y=40)
e4 = Entry(root, textvariable= employeeSalary, width=10)
e4.place(x=320, y=40)

l5 = Label(root, text="USD")
l5.place(x=380, y=40)

# Buttons

b1 = Button(root, text="Create", command=create)
b1.place(x=30, y=90)

b2 = Button(root, text="Show", command= read)
b2.place(x=180, y=90)

b3 = Button(root, text="Update", command=update)
b3.place(x=330, y=90)

b4 = Button(root, text="Delete", command=delete, bg='red')
b4.place(x=480, y=90)





root.config(menu=menubar)


root.mainloop()

            
