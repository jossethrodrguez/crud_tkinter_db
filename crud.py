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
appHelp = 'Welcome to SQlite App v' + appVersion + '.\n\n' + 'Python CRUD SQlite APP.\n\n' + 'Author: Josseth Rodriguez '
appData = employeeName.get(), employeeJobTitle.get(), employeeSalary.get() 
appTree = ttk.Treeview(height=10, columns=('0', '1', '2'))
appTree.place(x=0, y =130)

userValue = messagebox.askquestion(appOption)
userRecord = appTree.get_children()

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

def delete():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()

    if messagebox.askyesno("Delete", "Are you sure you want to delete the table employees?"):
        cursor.execute("DROP TABLE employees")

        messagebox.showinfo("Connection", "Deleted table employees")
    else:
        pass

def close():
    appOption = 'Are you sure you to close the App ?'

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
    appHelp
    

#### CRUD Methods ################################################# 

def show():
    connection = sqlite3.connect("employees.db")
    cursor = connection.cursor()

    for element in userRecord:
        appTree.delete(element)

    try:
        cursor.execute(' SELECT * employees')
        for row in cursor:
            appTree.insert('', 0, text=row[0], values=(row[1], row[2], row[3]))
    except:
        pass

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

root.mainloop()

            
