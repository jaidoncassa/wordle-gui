import tkinter as tk
import sqlite3


gui = tk.Tk()
gui.geometry("600x600")

# create a database por connect to one
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# table
c.execute(""" CREATE TABLE addresses (
          first_name text, 
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer
            )""")

conn.commit()

conn.close()

gui.mainloop()