from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import sqlite3
from collections import Counter
import os

class publishedWork(ttk.Frame):
    def __init__(self,user_id,master = None, **kwargs):
        super().__init__(master, **kwargs)
        self.res_id = user_id
        self.master = master
        self.create_widgets()

    def generate_exhibit(self,exhibit_id):
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM exhibitions WHERE exhibit_id = ?",(exhibit_id, ))
            exhibit = cursor.fetchone()
            print(exhibit)
            conn.close()

            exhibition_window = Toplevel()
            exhibition_window.geometry('600x800')
            exhibition_window.title("Exhibition")
            label = tk.Label(exhibition_window,text="Exhibit name: "+exhibit[6])
            label.pack()

            print(exhibit[3])
            image = Image.open(exhibit[4])
            image = image.resize((400,400))
            photo = ImageTk.PhotoImage(image)
            label_picture = tk.Label(exhibition_window,image=photo)
            label_picture.image = photo
            label_picture.pack()

            exhibition_text = Text(exhibition_window,width=40,height=10,font=("Halvetica",12))
            description_text = open(exhibit[3], 'r')
            words = description_text.read()
            exhibition_text.insert(END, words)
            exhibition_text.configure(state="disabled")
            description_text.close()
            exhibition_text.pack(pady=20)

    def create_widgets(self):
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT exhibit_id,image_path FROM exhibitions WHERE res_id = ? LIMIT 9", (self.res_id, ))     
            record = cursor.fetchall()
            conn.close()
            print(record)

            buttons = []

            for y in range(3):
                for x in range(3):
                    number = x+(3*y)
                    if(number < len(record)):
                        print(number)
                        temp_exhibition = record[number]
                        file_path = temp_exhibition[1]
                        exhibition_id = temp_exhibition[0]

                        image = Image.open(file_path)
                        image = image.resize((150,150))
                        photo = ImageTk.PhotoImage(image)

                        button_temp = Button(self)
                        buttons.append(button_temp)
                        print(exhibition_id)
                        buttons[number] = tk.Button(self,image=photo,
                                                    command=lambda exhibition_id = exhibition_id:self.generate_exhibit(exhibition_id))
                        buttons[number].image = photo
                        buttons[number].grid(row =y,column=x) 
        
