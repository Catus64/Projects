from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import sqlite3
from collections import Counter
import os

class acceptRequest(ttk.Frame):
    def __init__(self,master = None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.create_widgets()
    
    def accept_research(self,prod_id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        try:
            cursor.execute("""
                           UPDATE research_product
                           SET approval = ?
                           WHERE prod_id = ?
                           """,("approved",prod_id, ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Research Has Been Approved")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save to database: {e}")
            return
        
        for widget in self.winfo_children():
            widget.destroy()
        self.create_widgets()

    def generate_request(self,prod_id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM research_product WHERE prod_id = ? AND approval = ?",(prod_id, "false",  ))
        res_prod = cursor.fetchone()
        print(res_prod)
        conn.close()
        print(prod_id)

        res_prod_window = Toplevel()
        res_prod_window.geometry('600x800')
        res_prod_window.title("Exhibition")
        label = ttk.Label(res_prod_window, text="Research name: " + res_prod[2])
        label.pack()

        image = Image.open(res_prod[4])
        image = image.resize((400,400))
        photo = ImageTk.PhotoImage(image)
        label_picture = ttk.Label(res_prod_window,image=photo)
        label_picture.image = photo
        label_picture.pack()

        res_text = Text(res_prod_window,width=40,height=10,font=("Halvetica",12))
        explain_text = open(res_prod[3], 'r')
        words = explain_text.read()
        res_text.insert(END, words)
        res_text.configure(state="disabled")
        explain_text.close()
        res_text.pack()

        accept = ttk.Button(res_prod_window,text="ACCEPT",command=lambda:self.accept_research(prod_id))
        accept.pack()
        pass

    def create_widgets(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT prod_id,image_path FROM research_product WHERE approval = ?",("false", ))
        record = cursor.fetchall()
        if not record:
            messagebox.showinfo("YOW","No research currently applied")
            conn.close()
            return
        conn.close()

        buttons = []
        ttk.Label(self, text="Accept Research Request", font=('bold', 20)).pack()
        item_frame = ttk.Frame(self)
        item_frame.pack()
        

        for y in range(3):
            for x in range(3):
                number = x+(3*y)
                if(number < len(record)):
                    print(number)
                    temp_research = record[number]
                    file_path = temp_research[1]
                    prod_id = temp_research[0]

                    image = Image.open(file_path)
                    image = image.resize((150,150))
                    photo = ImageTk.PhotoImage(image)

                    button_temp = tk.Button(item_frame)
                    buttons.append(button_temp)
                    print(prod_id)
                    buttons[number] = tk.Button(item_frame,image=photo,
                                                command=lambda prod_id = prod_id:self.generate_request(prod_id))
                    buttons[number].image = photo
                    buttons[number].grid(row = y,column = x)