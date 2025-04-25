from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import sqlite3
from collections import Counter
import os

class createExhibit(ttk.Frame):
    def __init__(self,user_id,master = None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.create_widgets()
        self.image_selected = None
        self.prod_id = None
        self.user_id = user_id

    def setimage(self,prod_id,filepath,res_id):
        self.res_id = res_id
        self.prod_id = prod_id
        self.image_selected = filepath
        new_image = Image.open(filepath)
        new_image = new_image.resize((150,150))
        new_photo = ImageTk.PhotoImage(new_image)
        self.picture_display.configure(image = new_photo)
        self.picture_display.image = new_photo
        messagebox.showinfo("Success", "Research selected successfully!")
        self.select_window.destroy()

    def save_exhibit(self):
        name = self.name_entry.get()
        description = self.desc_text.get("1.0", "end-1c")
        image_path = self.image_selected
        if not name or not description or not image_path:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        desc_file_path = os.path.join("Ex_description", f"{name}.txt")
        if not os.path.exists("Ex_description"):
            os.makedirs("Ex_description")
        with open(desc_file_path, "w") as desc_file:
            desc_file.write(description)

        image_name = f"{name}.{image_path.split('.')[-1]}"
        image_dest_path = os.path.join("images", image_name)
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
                INSERT INTO exhibitions (exhibit_id,cur_id,res_id,desc_path,image_path,likes,name)
                VALUES (NULL, ?, ?, ?, ?, ?, ?)
                """,
                (self.user_id,self.res_id, desc_file_path, image_dest_path, 0,name )
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Research data saved successfully!")
        except Exception as e:
                messagebox.showerror("Error", f"Failed to save to database: {e}")
                return
    
    def select_research(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT prod_id,image_path,res_id FROM research_product WHERE approval = ?",("approved", ))
        record = cursor.fetchall()
        if not record:
            messagebox.showinfo("YOW","No research currently applied")
            conn.close()
            return
        conn.close()

        buttons = []

        self.select_window = Toplevel()
        self.select_window.geometry('600x800')
        self.select_window.title("Approved Researches")

        ttk.Label(self.select_window, text="Select for exhibit reference", font=('bold', 20)).pack()
        item_frame = ttk.Frame(self.select_window)
        item_frame.pack()
        

        for y in range(3):
            for x in range(3):
                number = x+(3*y)
                if(number < len(record)):
                    print(number)
                    temp_research = record[number]
                    res_id = temp_research[2]
                    file_path = temp_research[1]
                    prod_id = temp_research[0]

                    image = Image.open(file_path)
                    image = image.resize((150,150))
                    photo = ImageTk.PhotoImage(image)

                    button_temp = tk.Button(item_frame)
                    buttons.append(button_temp)
                    print(prod_id)
                    buttons[number] = tk.Button(item_frame,image=photo,
                                                command=lambda prod_id = prod_id:self.setimage(prod_id,file_path,res_id))
                    buttons[number].image = photo
                    buttons[number].grid(row = y,column = x)

    def create_widgets(self):
        button_frame = ttk.Frame(self)
        button_frame.grid(row=0, column=0, columnspan=2, pady=20)
        ttk.Label(button_frame,text="Curating from approved researches",font=('bold',20)).grid(row=0,column=0)
        choose_button = ttk.Button(self,text="Choose Research",command=self.select_research)
        choose_button.grid(row=1,column=0)

        self.name = ttk.Label(self,text = "Name: ", font = ("Arial", 12))
        self.name.grid(row = 2 ,column = 0 ,padx=10, pady=10, sticky="w")
        self.name_entry = ttk.Entry(self,width=30)
        self.name_entry.grid(row = 2, column=1,padx=10, pady=10, sticky="ew")

        self.picture_display = ttk.Label(self)
        default_image = Image.open("images/default.jpg")
        default_image = default_image.resize((150,150))
        default_photo = ImageTk.PhotoImage(default_image)
        self.picture_display.configure(image = default_photo)
        self.picture_display.image = default_photo
        self.picture_display.grid(row = 3, column=1)

        Label(self, text="Description :", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=10, sticky="nw")
        self.desc_text = Text(self, width=40, height=5, font=("Arial", 12))
        self.desc_text.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        button_frame = ttk.Frame(self)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)
        save_button = ttk.Button(button_frame, text="Save Research", command=self.save_exhibit)
        save_button.pack(side="left", padx=10)

        pass