from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import sqlite3
from collections import Counter
import os

class editProfile(ttk.Frame):
    def __init__(self,user_id,mode,master = None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.user_id = user_id
        self.mode = mode
        print("haha")
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.fetch_user_details()
        self.create_widgets()

    def fetch_user_details(self):
        # Fetch the user's current details from the database
        if(self.mode == "none"):
            self.cursor.execute("SELECT username, password, email, name FROM generalUser WHERE usr_id = ?", (self.user_id,))
            self.user_details = self.cursor.fetchone()

            if not self.user_details:
                messagebox.showerror("Error", "User not found!")
                return
        else:
            self.cursor.execute("SELECT username, password, email, name FROM researcher WHERE res_id = ?", (self.user_id,))
            self.user_details = self.cursor.fetchone()

            if not self.user_details:
                messagebox.showerror("Error", "Researcher not found!")
                return

    def create_widgets(self):

        Label(self, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        Label(self, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Label(self, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Label(self, text="Name:").grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.username_entry = Entry(self, width=30)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.username_entry.insert(0, self.user_details[0])

        self.password_entry = Entry(self, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        self.password_entry.insert(0, self.user_details[1])

        self.email_entry = Entry(self, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)
        try:
            self.email_entry.insert(0, self.user_details[2])
        except Exception as e:
            pass

        self.name_entry = Entry(self, width=30)
        self.name_entry.grid(row=3, column=1, padx=10, pady=10)
        self.name_entry.insert(0, self.user_details[3])

        Button(self, text="Save Changes", command=self.save_changes).grid(row=4, column=0, columnspan=2, pady=20)

    def save_changes(self):
        if(self.mode == "none"):
            # Get the updated values from the entry fields
            new_username = self.username_entry.get()
            new_password = self.password_entry.get()
            new_email = self.email_entry.get()
            new_name = self.name_entry.get()

            # Validate inputs
            if not new_username or not new_password or not new_email or not new_name:
                messagebox.showerror("Error", "All fields are required!")
                return

            # Update the database
            try:
                self.cursor.execute(
                    """
                    UPDATE generalUser
                    SET username = ?, password = ?, email = ?, name = ?
                    WHERE usr_id = ?
                    """,
                    (new_username, new_password, new_email, new_name, self.user_id)
                )
                self.conn.commit()
                messagebox.showinfo("Success", "User details updated successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update user details: {e}")
            finally:
                self.conn.close()
        else:
            new_username = self.username_entry.get()
            new_password = self.password_entry.get()
            new_email = self.email_entry.get()
            new_name = self.name_entry.get()

            # Validate inputs
            if not new_username or not new_password or not new_email or not new_name:
                messagebox.showerror("Error", "All fields are required!")
                return

            # Update the database
            try:
                self.cursor.execute(
                    """
                    UPDATE researcher
                    SET username = ?, password = ?, email = ?, name = ?
                    WHERE res_id = ?
                    """,
                    (new_username, new_password, new_email, new_name, self.user_id)
                )
                self.conn.commit()
                messagebox.showinfo("Success", "Researcher details updated successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update researcher details: {e}")
            finally:
                self.conn.close()