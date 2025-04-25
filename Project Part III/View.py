from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
import sqlite3
import Controller as c
class View(Tk):
    def __init__(self,cntrl = c.Controller):
        super().__init__()

        # Store controller reference properly
        self.controller = cntrl  

        self.title("Digital Museum")
        self.iconbitmap()
        self.geometry('1000x700')

        self.welcome = Label(self, text = "Welcome to Digital Museum",
                             font=("Helvetica", 42))
        self.welcome.place(relx=0.15,rely=0.3)

        ## use userEntry.get() to get values
        self.loginUser = Label(self, text = "Username",
                           font=("Helvetica", 12))
        self.loginUser.place(relx=0.45,rely=0.52)

        userEntry = Entry(self)
        userEntry.place(relx=0.45,rely=0.55)

        self.loginPass = Label(self, text = "Password",
                           font=("Helvetica", 12))
        self.loginPass.place(relx=0.45,rely=0.62)

        passEntry = Entry(self)
        passEntry.place(relx=0.45,rely=0.65)

        user_type = StringVar()
        drop = OptionMenu(self, user_type, "General User", "Admin", "Curator", "Researcher")
        user_type.set("General User")
        drop.place(relx=0.45,rely=0.7)

        button = Button(self,text="login", command=lambda: cntrl.login(cntrl,userEntry.get(),passEntry.get(),user_type.get(),self))
        button.place(relx=0.5,rely=0.75)

        register_button = Button(self, text="Register", command=self.open_registration_page)
        register_button.place(relx=0.5, rely=0.8)

    def open_registration_page(self):
        registration_window = RegistrationView(self.controller)
        registration_window.mainloop()

    def show_error(error_string1,error_string2):
        messagebox.showerror(error_string1,error_string2)
        return
    
class RegistrationView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("User Registration")
        self.geometry("600x400")

        tk.Label(self, text="Register", font=("Helvetica", 20)).pack(pady=20)

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

        register_btn = tk.Button(self, text="Submit", command=self.register_user)
        register_btn.pack(pady=10)

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        name = self.name_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        success = self.controller.register_user(username, password, name)

        if success:
            self.destroy()  # Close the registration window
    
