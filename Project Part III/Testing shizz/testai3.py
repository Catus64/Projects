import os
import sqlite3
from tkinter import Tk, Label, Entry, Button, OptionMenu, StringVar, Text, filedialog, messagebox
from tkinter import ttk
from PIL import Image

# Function to handle saving the exhibition data
def save_exhibition():
    # Get the input values
    curator_id = curator_var.get()
    researcher_id = researcher_var.get()
    name = name_entry.get()
    likes = likes_entry.get()
    description = desc_text.get("1.0", "end-1c")  # Get text from the Text widget

    # Validate inputs
    if not name or not description or not image_path:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Save the description to a text file in Ex_descriptions/
    desc_file_path = os.path.join("Ex_description", f"{name}.txt")
    if not os.path.exists("Ex_description"):
        os.makedirs("Ex_description")
    with open(desc_file_path, "w") as desc_file:
        desc_file.write(description)

    # Save the image to the images directory
    if image_path:
        image_name = f"{name}.{image_path.split('.')[-1]}"  # Preserve the original extension
        image_dest_path = os.path.join("images", image_name)
        if not os.path.exists("images"):
            os.makedirs("images")
        try:
            # Open the image to ensure it's valid
            with Image.open(image_path) as img:
                img.save(image_dest_path)  # Save the image to the destination
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image: {e}")
            return

    # Insert data into the SQLite database
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO exhibitions (cur_id, res_id, desc_path, image_path, likes, name)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (curator_id, researcher_id, desc_file_path, image_dest_path, likes, name)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Exhibition data saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data to database: {e}")

# Function to handle importing an image
def import_image():
    global image_path
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg"),("jpeg files", "*.jpg"), ("png files", "*.png")]
    )
    if file_path:
        image_path = file_path
        messagebox.showinfo("Success", "Image selected successfully!")

# Create the main window
root = Tk()
root.title("Exhibition Data Entry")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Global variable to store the image path
image_path = None

# Create a main frame for better organization
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# Create and place widgets
Label(main_frame, text="Curator ID:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
curator_var = StringVar(root)
curator_var.set("1")  # Default value
OptionMenu(main_frame, curator_var, "1", "2", "3").grid(row=0, column=1, padx=10, pady=10, sticky="ew")

Label(main_frame, text="Researcher ID:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
researcher_var = StringVar(root)
researcher_var.set("1")  # Default value
OptionMenu(main_frame, researcher_var, "1", "2", "3").grid(row=1, column=1, padx=10, pady=10, sticky="ew")

Label(main_frame, text="Name:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
name_entry = ttk.Entry(main_frame, width=30)
name_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

Label(main_frame, text="Likes:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
likes_entry = ttk.Entry(main_frame, width=30)
likes_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

Label(main_frame, text="Description:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=10, sticky="nw")
desc_text = Text(main_frame, width=40, height=5, font=("Arial", 12))
desc_text.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

# Buttons
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=20)

import_button = ttk.Button(button_frame, text="Import Image", command=import_image)
import_button.pack(side="left", padx=10)

save_button = ttk.Button(button_frame, text="Save Exhibition", command=save_exhibition)
save_button.pack(side="left", padx=10)

# Create the SQLite database and table if they don't exist
try:
    conn = sqlite3.connect("exhibition.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS exhibition (
            ex_id INTEGER PRIMARY KEY AUTOINCREMENT,
            curator_id INTEGER,
            researcher_id INTEGER,
            desc_path TEXT,
            image_path TEXT,
            likes INTEGER,
            name TEXT
        )
        """
    )
    conn.commit()
    conn.close()
except Exception as e:
    messagebox.showerror("Error", f"Failed to initialize database: {e}")

# Run the application
root.mainloop()