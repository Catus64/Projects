from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import sqlite3
import hashlib

from CuratorRegistrationController import CuratorRegistration
from CuratorRegistrationView import CuratorRegistrationView
from ResearcherRegistrationController import ResearcherRegistration
from ResearcherRegistrationView import ResearcherRegistrationView
from ResearcherDataView import ResearcherDataView
from CuratorDataView import CuratorDataView

def get_db_connection():
    conn = sqlite3.connect("data.db")
    conn.row_factory = sqlite3.Row
    return conn

class AdminView(Toplevel):
    def __init__(self, userid):
        super().__init__()
        self.title("Digital Museum - Admin Menu")
        self.geometry('1000x700')

        options_frame = ttk.Frame(self)
        options_frame.pack(fill='x', pady=10)

        self.home_btn = ttk.Button(options_frame, text='Home', command=self.home_page)
        self.home_btn.grid(row=0, column=0, padx=10)

        self.curator_btn = ttk.Button(options_frame, text='Curator', command=self.curator_page)
        self.curator_btn.grid(row=0, column=1, padx=10)

        self.researcher_btn = ttk.Button(options_frame, text='Researcher', command=self.researcher_page)
        self.researcher_btn.grid(row=0, column=2, padx=10)

        self.genUser_btn = ttk.Button(options_frame, text='Users', command=self.general_page)
        self.genUser_btn.grid(row=0, column=3, padx=10)

        self.admin_frame = ttk.Frame(self)
        self.admin_frame.pack(fill='both', expand=True)

        self.home_page()

    def home_page(self):
        self.delete_page()
        home_frame = ttk.Frame(self.admin_frame)
        home_frame.pack(fill='both', expand=True)
        
        ttk.Label(home_frame, text="Welcome Admin", font=('bold', 30)).pack(pady=20)
        
        exit_btn = ttk.Button(home_frame, text="Exit", command=self.confirm_exit)
        exit_btn.pack(side='bottom', pady=20)

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.destroy()

    def curator_page(self):
        self.delete_page()
        curator_frame = ttk.Frame(self.admin_frame)
        ttk.Label(curator_frame, text="Curator Page", font=('bold', 20)).pack()
        ttk.Button(curator_frame, text="Register Curator", command=self.register_curator_page).pack()
        ttk.Button(curator_frame, text="Show Curator", command=self.show_curator_data_page).pack()
        curator_frame.pack(pady=20)
        
    def show_curator_data_page(self):
        self.delete_page()
        page = CuratorDataView(self.admin_frame, self)
        page.pack(fill='both', expand=True)
        ttk.Button(page, text="Back", command=self.curator_page).pack()
                
    def register_curator_page(self):
        self.delete_page()
        page = CuratorRegistrationView(self.admin_frame, CuratorRegistration())
        ttk.Button(page, text="Back", command=self.curator_page).pack()

    def researcher_page(self):
        self.delete_page()
        researcher_frame = ttk.Frame(self.admin_frame)
        ttk.Label(researcher_frame, text="Researcher Page", font=('bold', 20)).pack()
        ttk.Button(researcher_frame, text="Register Researcher", command=self.register_researcher_page).pack()
        ttk.Button(researcher_frame, text="Show Researcher", command=self.show_researcher_data_page).pack()
        researcher_frame.pack(pady=20)
        
    def register_researcher_page(self):
        self.delete_page()
        page = ResearcherRegistrationView(self.admin_frame, ResearcherRegistration())
        ttk.Button(page, text="Back", command=self.researcher_page).pack()

    def show_researcher_data_page(self):
        self.delete_page()
        page = ResearcherDataView(self.admin_frame, self)
        page.pack(fill='both', expand=True)
        ttk.Button(page, text="Back", command=self.researcher_page).pack()

    def general_page(self):
        self.delete_page()
        general_frame = ttk.Frame(self.admin_frame)
        general_frame.pack(fill='both', expand=True)

        ttk.Label(general_frame, text="User Management", font=('bold', 20)).pack(pady=10)

        columns = ('User_ID', 'Username', 'Name', 'Email', 'Password')
        self.tree = ttk.Treeview(general_frame, columns=columns, show='headings')
        self.tree.heading('User_ID', text='ID')
        self.tree.heading('Username', text='Username')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Password', text='Password')
        self.tree.pack(fill='both', expand=True, padx=20, pady=10)
        
        btn_frame = ttk.Frame(general_frame)
        btn_frame.pack(pady=10)
        
        edit_btn = ttk.Button(btn_frame, text="Edit", command=self.edit_selected_user)
        edit_btn.grid(row=0, column=0, padx=5)
        delete_btn = ttk.Button(btn_frame, text="Delete", command=self.delete_selected_user)
        delete_btn.grid(row=0, column=1, padx=5)
        
        self.populate_user_table()

    def populate_user_table(self):
        self.tree.delete(*self.tree.get_children())
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT usr_id, username, email, name, password FROM generalUser")
        users = cursor.fetchall()
        conn.close()
        for user in users:
            self.tree.insert('', 'end', values=(user['usr_id'], user['username'], user['email'], user['name'], user['password']))

    def edit_selected_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a user to edit.")
            return
        user_id = self.tree.item(selected_item)['values'][0]
        self.edit_user(user_id)

    def edit_user(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, email, name, password FROM generalUser WHERE usr_id=?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        
        if not user:
            messagebox.showerror("Error", "User not found!")
            return

        edit_window = Toplevel(self)
        edit_window.title("Edit User")
        edit_window.geometry("300x300")

        ttk.Label(edit_window, text="Select Field to Edit:").pack(pady=5)
        field_options = {"Username": "username", "Email": "email", "Name": "name", "Password": "password"}
        field_var = StringVar(value="Username")
        field_dropdown = ttk.Combobox(edit_window, textvariable=field_var, values=list(field_options.keys()), state="readonly")
        field_dropdown.pack(pady=5)
        
        ttk.Label(edit_window, text="New Value:").pack(pady=5)
        new_value_entry = ttk.Entry(edit_window)
        new_value_entry.pack(pady=5)
        
        def update_user():
            selected_field = field_var.get()
            field_name = field_options[selected_field]
            new_value = new_value_entry.get()

            if new_value:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute(f"UPDATE generalUser SET {field_name}=? WHERE usr_id=?", (new_value, user_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "User details updated!")
                self.populate_user_table()
                edit_window.destroy()
            else:
                messagebox.showwarning("Warning", "New value cannot be empty.")

        ttk.Button(edit_window, text="Update", command=update_user).pack(pady=10)

    def delete_user(self, user_id):
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this user?")
        if confirm:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM generalUser WHERE usr_id=?", (user_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User deleted successfully!")
            self.populate_user_table()

    def delete_selected_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a user to delete.")
            return
        user_id = self.tree.item(selected_item)['values'][0]
        self.delete_user(user_id)

    def delete_page(self):
        for widget in self.admin_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = AdminView(1)
    app.mainloop()