import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class CuratorDataView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        ttk.Label(self, text="Show Curator", font=("Helvetica", 20)).pack(pady=10)

        columns = ('ID', 'Username', 'Name', 'Email', 'Password')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Username', text='Username')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Password', text='Password')
        self.tree.pack(fill='both', expand=True, padx=20, pady=10)
        
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        
        edit_btn = ttk.Button(btn_frame, text="Edit", command=self.edit_selected_curator)
        edit_btn.grid(row=0, column=0, padx=5)
        delete_btn = ttk.Button(btn_frame, text="Delete", command=self.delete_selected_curator)
        delete_btn.grid(row=0, column=1, padx=5)
        
        self.load_curator()
        self.pack(fill='both', expand=True)

    def load_curator(self):
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT cur_id, username, name, email, password FROM curator")
        curators = cursor.fetchall()
        conn.close()
        for curator in curators:
            self.tree.insert('', 'end', values=(curator[0], curator[1], curator[2], curator[3], curator[4]))

    def edit_selected_curator(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a curator to edit.")
            return
        curator_id = self.tree.item(selected_item)['values'][0]
        self.edit_curator(curator_id)

    def edit_curator(self, curator_id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username, name, email, password FROM curator WHERE cur_id=?", (curator_id,))
        curator = cursor.fetchone()
        conn.close()
        
        if not curator:
            messagebox.showerror("Error", "Curator not found!")
            return
        
        edit_window = tk.Toplevel(self)
        edit_window.title("Edit Curator")
        edit_window.geometry("300x300")

        ttk.Label(edit_window, text="Select Field to Edit:").pack(pady=5)
        field_options = {"Username": "username", "Name": "name", "Email": "email", "Password": "password"}
        field_var = tk.StringVar(value="Username")
        field_dropdown = ttk.Combobox(edit_window, textvariable=field_var, values=list(field_options.keys()), state="readonly")
        field_dropdown.pack(pady=5)
        
        ttk.Label(edit_window, text="New Value:").pack(pady=5)
        new_value_entry = ttk.Entry(edit_window)
        new_value_entry.pack(pady=5)
        
        def update_curator():
            selected_field = field_var.get()
            field_name = field_options[selected_field]
            new_value = new_value_entry.get()

            if new_value:
                conn = sqlite3.connect("data.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE curator SET {field_name}=? WHERE cur_id=?", (new_value, curator_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Curator details updated!")
                self.load_curator()
                edit_window.destroy()
            else:
                messagebox.showwarning("Warning", "New value cannot be empty.")

        ttk.Button(edit_window, text="Update", command=update_curator).pack(pady=10)

    def delete_selected_curator(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a curator to delete.")
            return
        curator_id = self.tree.item(selected_item)['values'][0]
        self.delete_curator(curator_id)
    
    def delete_curator(self, curator_id):
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this curator?")
        if confirm:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM curator WHERE cur_id=?", (curator_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Curator deleted successfully!")
            self.load_curator()