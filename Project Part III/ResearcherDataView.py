import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ResearcherDataView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        ttk.Label(self, text="Show Researcher", font=("Helvetica", 20)).pack(pady=10)

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
        
        edit_btn = ttk.Button(btn_frame, text="Edit", command=self.edit_selected_researcher)
        edit_btn.grid(row=0, column=0, padx=5)
        delete_btn = ttk.Button(btn_frame, text="Delete", command=self.delete_selected_researcher)
        delete_btn.grid(row=0, column=1, padx=5)
        
        self.load_researcher()
        self.pack(fill='both', expand=True)

    def load_researcher(self):
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT res_id, username, name, email, password FROM researcher")
        researchers = cursor.fetchall()
        conn.close()
        for researcher in researchers:
            self.tree.insert('', 'end', values=(researcher[0], researcher[1], researcher[2], researcher[3], researcher[4]))

    def edit_selected_researcher(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a researcher to edit.")
            return
        researcher_id = self.tree.item(selected_item)['values'][0]
        self.edit_researcher(researcher_id)

    def edit_researcher(self, researcher_id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username, name, email, password FROM researcher WHERE res_id=?", (researcher_id,))
        researcher = cursor.fetchone()
        conn.close()
        
        if not researcher:
            messagebox.showerror("Error", "Researcher not found!")
            return
        
        edit_window = tk.Toplevel(self)
        edit_window.title("Edit Researcher")
        edit_window.geometry("300x300")

        ttk.Label(edit_window, text="Select Field to Edit:").pack(pady=5)
        field_options = {"Username": "username", "Name": "name", "Email": "email", "Password": "password"}
        field_var = tk.StringVar(value="Username")
        field_dropdown = ttk.Combobox(edit_window, textvariable=field_var, values=list(field_options.keys()), state="readonly")
        field_dropdown.pack(pady=5)
        
        ttk.Label(edit_window, text="New Value:").pack(pady=5)
        new_value_entry = ttk.Entry(edit_window)
        new_value_entry.pack(pady=5)
        
        def update_researcher():
            selected_field = field_var.get()
            field_name = field_options[selected_field]
            new_value = new_value_entry.get()

            if new_value:
                conn = sqlite3.connect("data.db")
                cursor = conn.cursor()
                cursor.execute(f"UPDATE researcher SET {field_name}=? WHERE res_id=?", (new_value, researcher_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Researcher details updated!")
                self.load_researcher()
                edit_window.destroy()
            else:
                messagebox.showwarning("Warning", "New value cannot be empty.")

        ttk.Button(edit_window, text="Update", command=update_researcher).pack(pady=10)

    def delete_selected_researcher(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a researcher to delete.")
            return
        researcher_id = self.tree.item(selected_item)['values'][0]
        self.delete_researcher(researcher_id)
    
    def delete_researcher(self, researcher_id):
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this researcher?")
        if confirm:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM researcher WHERE res_id=?", (researcher_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Researcher deleted successfully!")
            self.load_researcher()