from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import GR_editProfile as ep
import tkinter as tk
from tkinter import ttk
import sqlite3
import Exhibit
import G_recommends
#import Controller as c

class GeneralView(Toplevel):
    def __init__(self,user_id):
        super().__init__()
        ##Toplevel window
        self.title("Digital Museum-User Menu")
        self.iconbitmap()
        self.geometry('1000x800')

        def hide_indicators():
            home_btn.config(bg = 'white')
            explore_btn.config(bg = 'white')
            liked_btn.config(bg = 'white')
            edit_btn.config(bg = 'white')
            rec_btn.config(bg = 'white')
        
        def delete_page():
            for frame in user_frame.winfo_children():
                frame.destroy()

        def indicate(bt,page,mode):
            hide_indicators()
            delete_page()
            bt.config(bg = 'gray')
            page(mode)

        def home_page(mode):
            home_page = tk.Frame(user_frame)

            lb = tk.Label(home_page,text="Welcome User\n\n"+str(user_id),font=('bold,30'))
            lb.pack()

            home_page.pack(pady=20)

        def like(ex_id,button):
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_likes WHERE usr_id = ? AND exhibit_id = ?", (user_id, ex_id, ))
            like_exist = cursor.fetchone()
            if like_exist:
                #print(like_exist[0])
                cursor.execute("DELETE FROM user_likes WHERE like_id = ?", (like_exist[0], ) )
                conn.commit()
                check_like(ex_id,button)
                conn.close()
                return
            cursor.execute("INSERT INTO user_likes (like_id, usr_id ,exhibit_id) VALUES (NULL, ?, ?)", (user_id, ex_id))
            conn.commit()
            check_like(ex_id,button)
            conn.close()
        
        def check_like(ex_id,button):
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_likes WHERE usr_id = ? AND exhibit_id = ?", (user_id, ex_id, ))
            like_exist = cursor.fetchone()
            if like_exist:
                button.configure(bg = "green")
            else:
                button.configure(bg = "white")
                
        def generate_exhibit(exhibit_id):
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
            like_button = Button(exhibition_window,image=photo_like,command= lambda temp_id = temp_id:like(temp_id,like_button))
            like_button.image = photo_like
            check_like(temp_id,like_button)
            like_button.pack()

            

        def intitate_frame(picture_wall,state):
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            if(state == "explore"):
                cursor.execute("SELECT exhibit_id,image_path FROM exhibitions LIMIT 9")
            else:
                cursor.execute("""SELECT user_likes.exhibit_id,image_path 
                                FROM user_likes INNER JOIN  exhibitions
                                ON user_likes.exhibit_id = exhibitions.exhibit_id
                                WHERE user_likes.usr_id = ? 
                                LIMIT 9;""",(user_id, ))
            
            record = cursor.fetchall()
            if not record:
                    messagebox.showinfo("Hey", "you have not liked anything yet")
                    conn.close()
                    return
            conn.close()
            print(record)

            buttons = []

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

                        button_temp = Button(picture_wall)
                        buttons.append(button_temp)
                        print(exhibition_id)
                        buttons[number] = tk.Button(picture_wall,image=photo,
                                                    command=lambda exhibition_id = exhibition_id:generate_exhibit(exhibition_id))
                        buttons[number].image = photo
                        buttons[number].grid(row =y,column=x) 
            

        def explore_page(mode):
            explore_page = tk.Frame(user_frame)
            picture_wall = tk.Frame(explore_page,background="")
            picture_wall.configure(width=800,height = 400)
            picture_wall.pack()
            intitate_frame(picture_wall,mode)

            browse_nav = tk.Frame(explore_page,background="")
            browse_nav.configure(width=800,height = 30)
            browse_nav.pack()
            explore_page.pack(pady=20)


        def edit_profile(mode):
            #edit_profile = tk.Frame(user_frame)
            #lb = tk.Label(edit_profile,text="Editing = ...",font=('bold,30'))
            #lb.pack()
            #edit_profile.pack(pady=20)
            edit_profile = ep.editProfile(user_id,mode,user_frame)
            edit_profile.pack()

        def rec_page(mode):
            
            rec = G_recommends.recommend(self,user_id,user_frame)
            rec.pack()
    


        ##top menu
        options_frame = ttk.Frame(self)
        options_frame.pack(fill='x', pady=10)
        options_frame.pack(fill='x', pady=10)
        options_frame.configure(width=1000,height = 100)


        ##home button
        home_btn = tk.Button(options_frame,text='Home', font=('Bold', 16),
                             fg = 'black',bd=0, command=lambda:indicate(home_btn,home_page,"none") )
        home_btn.grid(row=0, column=0, padx=10)

        ##manage explore button
        explore_string = "explore"
        explore_btn = tk.Button(options_frame,text='Explore', font=('Bold', 16),
                             fg = 'black',bd=0, command=lambda:indicate(explore_btn,explore_page,explore_string))
        explore_btn.grid(row=0, column=1, padx=10)

        ##manage liked button
        liked_string = "liked"
        liked_btn = tk.Button(options_frame,text='Liked', font=('Bold', 16),
                             fg = 'black',bd=0, command=lambda:indicate(liked_btn,explore_page,liked_string))
        liked_btn.grid(row=0, column=2, padx=10)

        ##manage edit Users button
        edit_btn = tk.Button(options_frame,text='Edit Profile', font=('Bold', 16),
                             fg = 'black',bd=0, command=lambda:indicate(edit_btn,edit_profile,"none"))
        edit_btn.grid(row=0, column=3, padx=10)

        ##manage Recommended button
        rec_btn = tk.Button(options_frame,text='Recommended', font=('Bold', 16),
                             fg = 'black',bd=0, command=lambda:indicate(rec_btn,rec_page,"none"))
        rec_btn.grid(row=0, column=4, padx=10)


        ##main menu
        user_frame = ttk.Frame(self)
        user_frame.pack(fill='both', expand=True)
        user_frame.pack_propagate(False)
        user_frame.configure(width=1000,height=500)
        home_page("none")

        ##exit
        exitbtn = tk.Button(self,text="EXIT",font=('Bold',16)
                            ,fg='black',command=lambda:self.destroy())
        exitbtn.pack(pady=20)


if __name__ == "__main__":
    view = GeneralView(0)
    view.mainloop()