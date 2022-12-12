# Python CRUD SQlite APP.

# import dependencies
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

# Connections:

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

