from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import sqlite3
from collections import Counter
import os

class researchStation(ttk.Frame):
    def __init__(self,user_id,master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.user_id = user_id
        self.master = master
        self.create_widgets()

    def save_research(self):
        name = self.name_entry.get()
        description = self.desc_text.get("1.0", "end-1c")

        if not name or not description or not image_path:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        desc_file_path = os.path.join("Res_Explain", f"{name}.txt")
        if not os.path.exists("Res_Explain"):
            os.makedirs("Res_Explain")
        with open(desc_file_path, "w") as desc_file:
            desc_file.write(description)

        comment_file_path = os.path.join("Res_Comment", f"{name}.txt")
        with open(comment_file_path, "w") as desc_file:
            desc_file.write("nothing")

        if image_path:
            image_name = f"{name}.{image_path.split('.')[-1]}"
            image_dest_path = os.path.join("images", image_name)
            if not os.path.exists("images"):
                os.makedirs("images")
            try:
                with Image.open(image_path) as img:
                    img.save(image_dest_path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process image: {e}")
                return
        
        try:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO research_product (prod_id,res_id,name,explain_path,image_path,approval,comment_path)
                VALUES (NULL, ?, ?, ?, ?, ?, ?)
                """,
                (self.user_id, name, desc_file_path,image_dest_path,"false",comment_file_path, )
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Research data saved successfully!")
        except Exception as e:
                messagebox.showerror("Error", f"Failed to save to database: {e}")
                return

    def import_image(self):
        global image_path
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg"),("jpeg files", "*.jpg"), ("png files", "*.png")]
        )
        if file_path:
            image_path = file_path
            new_image = Image.open(file_path)
            new_image = new_image.resize((150,150))
            new_photo = ImageTk.PhotoImage(new_image)
            self.picture_display.configure(image=new_photo)
            self.picture_display.image = new_photo
            messagebox.showinfo("Success", "Image selected successfully!")
    
    def create_widgets(self):


        self.label = ttk.Label(self, text = "Research Section",font = ('bold',12))
        self.label.grid(row=0,column=0,padx=10, pady=10, sticky="w")

        image_path = None

        self.name = ttk.Label(self,text = "Name: ", font = ("Arial", 12))
        self.name.grid(row = 1 ,column = 0 ,padx=10, pady=10, sticky="w")
        self.name_entry = ttk.Entry(self,width=30)
        self.name_entry.grid(row = 1, column=1,padx=10, pady=10, sticky="ew")

        self.picture_display = ttk.Label(self)
        default_image = Image.open("images/default.jpg")
        default_image = default_image.resize((150,150))
        default_photo = ImageTk.PhotoImage(default_image)
        self.picture_display.configure(image = default_photo)
        self.picture_display.image = default_photo
        self.picture_display.grid(row = 2, column=1)

        Label(self, text="Explaination:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="nw")
        self.desc_text = Text(self, width=40, height=5, font=("Arial", 12))
        self.desc_text.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        button_frame = ttk.Frame(self)
        button_frame.grid(row=5, column=0, columnspan=2, pady=20)

        import_button = ttk.Button(button_frame, text="Import Image", command=self.import_image)
        import_button.pack(side="left", padx=10)

        save_button = ttk.Button(button_frame, text="Save Research", command=self.save_research)
        save_button.pack(side="left", padx=10)