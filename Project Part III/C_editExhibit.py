from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox
import sqlite3
from collections import Counter
import os

class editExhibit(ttk.Frame):
    def __init__(self,master = None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.create_widgets()
    
    def save_change(self,exhibition_id,name):
        new_desc = self.res_text.get("1.0", "end-1c")
        desc_file_path = os.path.join("Ex_description", f"{name}.txt")
        if os.path.exists(desc_file_path):
            os.remove(desc_file_path)
        
        with open(desc_file_path, "w") as desc_file:
            desc_file.write(new_desc)
        
        new_tag = self.get_tag_id(self.selected_tag.get())

        try:
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("""
                        UPDATE exhibitions
                        SET tag_id = ?
                        WHERE exhibit_id = ?
                            """,(new_tag, exhibition_id, ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Exhibit sucessfully edited")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save to database: {e}")
            return
        


    def get_tag_id(self, tag_name):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT tag_id FROM tags WHERE tag_name = ?" , (tag_name, ))
        temp = cursor.fetchone()
        temp_id = temp[0]
        conn.close()
        return temp_id

    def fetch_tag_names(self):
        try:
            # Connect to the database
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()

            # Fetch all tag names from the tags table
            cursor.execute("SELECT tag_name FROM tags")
            tags = cursor.fetchall()

            # Extract tag names from the result (each row is a tuple)
            tag_names = [tag[0] for tag in tags]

            # Close the connection
            conn.close()

            return tag_names
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch tags: {e}")
            return []

    def generate_edit(self,exhibition_id):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exhibitions WHERE exhibit_id = ?",(exhibition_id, ))
        res_prod = cursor.fetchone()
        print(res_prod)
        conn.close()
        print(exhibition_id)

        res_prod_window = Toplevel()
        res_prod_window.geometry('600x800')
        res_prod_window.title("Exhibition")

        label = tk.Label(res_prod_window,text="Exhibit name: "+res_prod[6])
        label.pack()

        image = Image.open(res_prod[4])
        image = image.resize((200,200))
        photo = ImageTk.PhotoImage(image)
        label_picture = ttk.Label(res_prod_window,image=photo)
        label_picture.image = photo
        label_picture.pack()



        self.res_text = Text(res_prod_window,width=40,height=10,font=("Halvetica",12))
        explain_text = open(res_prod[3], 'r')
        words = explain_text.read()
        self.res_text.insert(END, words)
        explain_text.close()
        self.res_text.pack()

        self.selected_tag = StringVar()
        tag_names = self.fetch_tag_names()
        option_menu = OptionMenu(res_prod_window, self.selected_tag, *tag_names)
        self.selected_tag.set(tag_names[0])
        option_menu.pack(pady=20)

        comment_button = Button(res_prod_window,text="Save Changes",command=lambda: self.save_change(res_prod[0],res_prod[6]))
        comment_button.pack()

    def create_widgets(self):
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT exhibit_id,image_path FROM exhibitions LIMIT 9")
            record = cursor.fetchall()
            conn.close()
            print(record)

            buttons = []
            ttk.Label(self, text="Editing Exhibitions", font=('bold', 20)).pack()
            item_frame = ttk.Frame(self)
            item_frame.pack()

            for y in range(3):
                #print(y)
                for x in range(3):
                    number = x+(3*y)
                    #print(x)
                    if(number < len(record)):
                        print(number)
                        temp_exhibition = record[number]
                        file_path = temp_exhibition[1]
                        exhibition_id = temp_exhibition[0]

                        image = Image.open(file_path)
                        image = image.resize((150,150))
                        photo = ImageTk.PhotoImage(image)

                        button_temp = Button(item_frame)
                        buttons.append(button_temp)
                        print(exhibition_id)
                        buttons[number] = tk.Button(item_frame,image=photo,
                                                    command=lambda exhibition_id = exhibition_id:self.generate_edit(exhibition_id))
                        buttons[number].image = photo
                        #button_temp.grid(row =y,column=x) 
                        #buttons.append(button_temp)
                        buttons[number].grid(row =y,column=x) 