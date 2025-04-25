from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import sqlite3
from collections import Counter
import os

class pendingRequest(ttk.Frame):
    def __init__(self,user_id,master = None, **kwargs):
        super().__init__(master, **kwargs)
        self.res_id = user_id
        self.master = master
        self.create_widgets()

    def generate_research(self,research_id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM research_product WHERE prod_id = ?",(research_id, ))
        res_prod = cursor.fetchone()
        print(res_prod)
        conn.close()
        print(research_id)

        res_prod_window = Toplevel()
        res_prod_window.geometry('600x800')
        label = ttk.Label(res_prod_window, text="Research name: " + res_prod[2])
        label.pack()

        image = Image.open(res_prod[4])
        image = image.resize((400,400))
        photo = ImageTk.PhotoImage(image)
        label_picture = ttk.Label(res_prod_window,image=photo)
        label_picture.image = photo
        label_picture.pack()

        status = ttk.Label(res_prod_window, text="Approved : " + res_prod[5], font=('bold',20))
        status.pack()

        ttk.Label(res_prod_window, text="Comment Research", font=('bold', 12)).pack()

        self.res_comment = Text(res_prod_window,width=40,height=5,font=("Halvetica",12))
        if res_prod[6]:
            explain_text = open(res_prod[6], 'r')
            words = explain_text.read()
            self.res_comment.insert(END, words)
            explain_text.close()
        self.res_comment.pack()

    def create_widgets(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT prod_id,image_path 
                       FROM research_product
                       WHERE res_id = ?
                       LIMIT 9
                       """,(self.res_id, ))
        record = cursor.fetchall()
        if not record:
            messagebox.showinfo("YOW", "You have not researched anything yet")
            conn.close()
            return
        conn.close()
        print(record)

        buttons = []
        ttk.Label(self, text="Research Section", font=('bold', 20)).pack()
        item_frame = ttk.Frame(self)
        item_frame.pack()

        for y in range(3):
            for x in range(3):
                number = x+(3*y)
                if(number < len(record)):
                    print(number)
                    temp_research = record[number]
                    file_path = temp_research[1]
                    res_id = temp_research[0]

                    image = Image.open(file_path)
                    image = image.resize((150,150))
                    photo = ImageTk.PhotoImage(image)

                    button_temp = tk.Button(item_frame)
                    buttons.append(button_temp)
                    print(res_id)
                    buttons[number] = tk.Button(item_frame,image=photo,
                                                command=lambda res_id = res_id:self.generate_research(res_id))
                    buttons[number].image = photo
                    buttons[number].grid(row = y,column = x)
