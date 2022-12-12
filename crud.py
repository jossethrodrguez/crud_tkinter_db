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

