

import hashlib
import sqlite3
from tkinter import Tk, messagebox

class ResearcherRegistration():
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        # self.create_researcher_table()

    def register_researcher(self, username, password, name, email):
        """Register a new researcher in the database"""
        if not username or not password or not name or not email:
            messagebox.showerror("Error", "All fields are required!")
            return False

        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Secure password storage

        try:
            self.cursor.execute("INSERT INTO researcher (Username, Password, Name, Email) VALUES (?, ?, ?, ?)", 
                                ( username, hashed_password, name, email))
            self.conn.commit()
            self.cursor.execute("SELECT res_id from researcher where username = ? AND password = ?", 
                                ( username, hashed_password))
            user = self.cursor.fetchone()
            messagebox.showinfo("Success", f"Reseacher registered successfully! Researcher User ID is {user}")
            return True
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
            return False
