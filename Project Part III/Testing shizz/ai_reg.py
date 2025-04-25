import tkinter as tk
from tkinter import messagebox
import sqlite3



def register():
  #usr_id = usr_id_entry.get()
  username = username_entry.get()
  password = password_entry.get()
  email = email_entry.get()
  name = name_entry.get()

  if not all([username, password, email, name]):
    messagebox.showerror("Error", "Please fill all fields.")
    return

  try:
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
      "INSERT INTO generalUser (usr_id, username, password, email, name) VALUES (NULL, ?, ?, ?, ?)",
      (username, password, email, name)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Registration successful!")

    # Clear the entry fields
    #usr_id_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
  except sqlite3.Error as e:
    messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Registration")

# Labels and entry fields
#usr_id_label = tk.Label(root, text="User ID:")
#usr_id_label.pack()
#usr_id_entry = tk.Entry(root)
#usr_id_entry.pack()

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Register button
register_button = tk.Button(root, text="Register", command=register)
register_button.pack()

root.mainloop()