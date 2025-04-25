
import tkinter as tk
from tkinter import messagebox

class ResearcherRegistrationView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        
        self.controller = controller

        tk.Label(self, text="Researcher Registration", font=("Helvetica", 20)).pack(pady=20)

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Label(self, text="Confirm Password").pack()
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.pack()

        tk.Label(self, text="Name").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()
        
        tk.Label(self, text="Email").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        register_btn = tk.Button(self, text="Submit", command=self.register_researcher)
        register_btn.pack(pady=10)
        
        self.pack(fill='both', expand=True)
    
    def register_researcher(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        success = self.controller.register_researcher(username, password, name, email)    
        
    
        
    
        
