

import hashlib
import sqlite3
from tkinter import Tk, messagebox

class CuratorRegistration():
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        # self.create_researcher_table()

    def register_researcher(self, username, password, name, email):
        """Register a new curator in the database"""
        if not username or not password or not name or not email:
            messagebox.showerror("Error", "All fields are required!")
            return False

        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Secure password storage

        try:
            self.cursor.execute("INSERT INTO curator (Username, Password, Name, Email) VALUES (?, ?, ?, ?)", 
                                ( username, hashed_password, name, email))
            self.conn.commit()
            self.cursor.execute("SELECT cur_id from curator where username = ? AND password = ?", 
                                ( username, hashed_password))
            user = self.cursor.fetchone()
            messagebox.showinfo("Success", f"Curator registered successfully! Curator User ID is {user}")
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
            return False
