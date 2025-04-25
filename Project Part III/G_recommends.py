from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk
import sqlite3
import random
from collections import Counter

class recommend(tk.Frame):
    def __init__(self,gen_view,user_id, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.create_widgets(gen_view)
        self.user_id = user_id
        self.showbutton = ttk.Button(self)
    
    def like(self,ex_id,button):
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_likes WHERE usr_id = ? AND exhibit_id = ?", (self.user_id, ex_id, ))
            like_exist = cursor.fetchone()
            if like_exist:
                #print(like_exist[0])
                cursor.execute("DELETE FROM user_likes WHERE like_id = ?", (like_exist[0], ) )
                conn.commit()
                self.check_like(ex_id,button)
                conn.close()
                return
            cursor.execute("INSERT INTO user_likes (like_id, usr_id ,exhibit_id) VALUES (NULL, ?, ?)", (self.user_id, ex_id))
            conn.commit()
            self.check_like(ex_id,button)
            conn.close()
        
    def check_like(self,ex_id,button):
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_likes WHERE usr_id = ? AND exhibit_id = ?", (self.user_id, ex_id, ))
            like_exist = cursor.fetchone()
            if like_exist:
                button.configure(bg = "green")
            else:
                button.configure(bg = "white")
                
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

            image_like = Image.open("images/like.png")
            image_like = image_like.resize((100,100))
            photo_like = ImageTk.PhotoImage(image_like)
            temp_id = exhibit[0]
            like_button = Button(exhibition_window,image=photo_like,command= lambda temp_id = temp_id:self.like(temp_id,like_button))
            like_button.image = photo_like
            self.check_like(temp_id,like_button)
            like_button.pack()

    def most_repeated_tag(self,tuple):
        # Extract the strings from the second element (index 1) of each tuple
        strings = [t[1] for t in tuple]
        
        # Count the occurrences of each string
        count = Counter(strings)
        
        # Find the maximum count value
        max_count = max(count.values())
        
        # Find all strings that have the maximum count
        most_repeated = [string for string, cnt in count.items() if cnt == max_count]
        
        # Return the first string in the list of most repeated strings
        return most_repeated[0]
    
    def get_tag_id(self,tagname):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT tag_id FROM tags WHERE tag_name = ?",(tagname, ))
        temp = cursor.fetchone()
        temp_tag = temp[0]
        return temp_tag
    
    def show_rec(self,gen_view):
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT e.exhibit_id,t.tag_name
                       FROM exhibitions AS e
                       INNER JOIN user_likes AS ul
                       ON e.exhibit_id = ul.exhibit_id
                       INNER JOIN tags AS t
                       ON e.tag_id = t.tag_id
                       WHERE ul.usr_id = ?
                      """,(self.user_id, ))
        all_likes = cursor.fetchall()
        favourite_tag = self.most_repeated_tag(all_likes)
        print(favourite_tag)

        tag_id = self.get_tag_id(favourite_tag)

        cursor.execute("""
                        SELECT exhibit_id,name,image_path
                        FROM exhibitions 
                        WHERE tag_id = ?
                        """, (tag_id, ))
        temp_list = cursor.fetchall()
        print(temp_list)

        cursor.execute("""
                        SELECT * FROM user_likes
                        WHERE usr_id = 0;
                        """)
        likes = cursor.fetchall()
        cursor.close()

        liked_exhibit_ids = {like[2] for like in likes} 

        unliked_exhibits = [exhibit for exhibit in temp_list if exhibit[0] not in liked_exhibit_ids]

        if unliked_exhibits:  # Check if there are any unliked exhibits
            selected_exhibit = random.choice(unliked_exhibits)
            print("Selected Exhibit:", selected_exhibit)
        else:
            print("No unliked exhibits found.")
        print(selected_exhibit)
        image = selected_exhibit[2]
        ex_id = selected_exhibit[0]
        print(image)

        image_temp = Image.open(image)
        image_temp = image_temp.resize((150,150))
        photo = ImageTk.PhotoImage(image_temp)
        self.showbutton.destroy()
        self.showbutton = ttk.Button(self,command=lambda: self.generate_exhibit(ex_id),image=photo)
        self.showbutton.image = photo
        self.showbutton.pack()
    
    def create_widgets(self,gen_view):
        # Add widgets to the frame
        self.label = tk.Label(self, text="Recommended Exhibit for you to look at!!!", font=("bold", 20))
        self.label.pack(pady=10)

        self.button = tk.Button(self, text=">", command=lambda: self.on_button_click(gen_view))
        self.button.pack(pady=10)

    def on_button_click(self,gen_view):
        self.show_rec(gen_view)
        print("Button clicked!")


    