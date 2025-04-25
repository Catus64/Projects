from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import sqlite3
from collections import Counter
import os

class reviewRequest(ttk.Frame):
    def __init__(self,master = None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.create_widgets()
    
    def save_comment(self,prod_id,prod_name):
        new_comment = self.res_comment.get("1.0", "end-1c")
        comment_file_path = os.path.join("Res_Comment", f"{prod_name}.txt")
        if os.path.exists(comment_file_path):
            os.remove(comment_file_path)

        with open(comment_file_path, "w") as comm_file:
            comm_file.write(new_comment)
        
        messagebox.showinfo("YOW","Commenting done")

    def generate_request(self,prod_id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM research_product WHERE prod_id = ?",(prod_id, ))
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
        image = image.resize((200,200))
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

        ttk.Label(res_prod_window, text="Comment Research", font=('bold', 12)).pack()

        self.res_comment = Text(res_prod_window,width=40,height=5,font=("Halvetica",12))
        if res_prod[6]:
            explain_text = open(res_prod[6], 'r')
            words = explain_text.read()
            self.res_comment.insert(END, words)
            explain_text.close()
        self.res_comment.pack()

        comment_button = Button(res_prod_window,text="Save Comment",command=lambda:self.save_comment(prod_id,res_prod[2]))
        comment_button.pack()

    def create_widgets(self):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT prod_id,image_path FROM research_product")
        record = cursor.fetchall()
        if not record:
            messagebox.showinfo("YOW","No research currently applied")
            conn.close()
            return
        conn.close()

        buttons = []

        ttk.Label(self, text="Review Research", font=('bold', 20)).pack()
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