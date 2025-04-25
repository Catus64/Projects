from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
import sqlite3
import GeneralUserView as g
import AdminView as a
import Researcher as r
import CuratorView as c
import hashlib
import random

class Controller():
    count = 1

    def login(event,self,username,password,type,view):

        if not all([username, password]):
            messagebox.showerror("Error", "Please fill all fields.")
            return

        try:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            print(type)
            if(type == "General User"):
                cursor.execute(
                "SELECT * FROM generalUser WHERE username=? AND password=?",
                (username, password)
                )
                user = cursor.fetchone()
                conn.close()

                if user:
                    messagebox.showinfo("Success", "Login successful!")
                    view.iconify()
                    logged = g.GeneralView(user[0])
                    # You can add logic here to handle successful login
                    # For example, you could open a new window or redirect to another page
                else:
                    messagebox.showerror("Error", "Invalid username or password.")

            #FOR Admin
            elif(type == "Admin"):
                cursor.execute(
                "SELECT * FROM admin WHERE username=? AND password=?",
                (username, password)
                )
                user = cursor.fetchone()
                conn.close()

                if user:
                    messagebox.showinfo("Success", "Login successful!")
                    view.iconify()
                    logged = a.AdminView(user[0])
                else:
                    messagebox.showerror("Error", "Invalid username or password.")

            #For Researcher
            elif(type == "Researcher"):
                cursor.execute(
                "SELECT * FROM researcher WHERE username=? AND password=?",
                (username, password)
                )
                user = cursor.fetchone()
                conn.close()

                if user:
                    messagebox.showinfo("Success", "Login successful!")
                    view.iconify()
                    logged = r.ResearcherView(user[0])
                else:
                    messagebox.showerror("Error", "Invalid username or password.")

            #For Curators
            elif(type == "Curator"):
                cursor.execute(
                "SELECT * FROM curator WHERE username=? AND password=?",
                (username, password)
                )
                user = cursor.fetchone()
                conn.close()

                if user:
                    messagebox.showinfo("Success", "Login successful!")
                    view.iconify()
                    logged = c.CuratorView(user[0])
                else:
                    messagebox.showerror("Error", "Invalid username or password.")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

        print("haha",self.count)
        self.count = self.count + 1

    def __init__(self, db_model):
        self.db = db_model  # Store database model reference
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()

    def generate_unique_user_id(self):
        """Generate a unique User_ID within the range 0-9999"""
        while True:
            user_id = random.randint(0, 9999)
            self.cursor.execute("SELECT User_ID FROM generalUser WHERE User_ID = ?", (user_id,))
            if not self.cursor.fetchone():
                return user_id

    def register_user(self, username, password, name):
        """Register a new user in the database"""
        if not username or not password or not name:
            messagebox.showerror("Error", "All fields are required!")
            return False
        
        #hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Secure password storage
        #user_id = self.generate_unique_user_id()

        try:
            self.cursor.execute("INSERT INTO generalUser (usr_id , username, password, name) VALUES (NULL, ?, ?, ?)", 
                                    (username, password, name, ))
            self.conn.commit()
            messagebox.showinfo("Success", f"User registered successfully!")
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
            return False