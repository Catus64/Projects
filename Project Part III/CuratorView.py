from tkinter import *
from tkinter import ttk, messagebox
import C_acceptRequest as ar
import C_reviewResearch as rr
import C_createExhibit as ce
import C_editExhibit as ee
import sqlite3

class CuratorView(Toplevel):
    def __init__(self,userid):
        super().__init__()
        self.title("Digital Museum - Curator Menu")
        self.geometry('1000x700')

        self.user_id = userid
        options_frame = ttk.Frame(self)
        options_frame.pack(fill='x', pady=10)

        self.home_btn = ttk.Button(options_frame, text='Home', command=self.home_page)
        self.home_btn.grid(row=0, column=0, padx=10)

        self.curate_btn = ttk.Button(options_frame, text='Curate', command=self.curate_page)
        self.curate_btn.grid(row=0, column=1, padx=10)

        self.review_btn = ttk.Button(options_frame, text='Review', command=self.review_page)
        self.review_btn.grid(row=0, column=2, padx=10)

        self.accept_btn = ttk.Button(options_frame, text='Accept', command=self.accept_page)
        self.accept_btn.grid(row=0, column=3, padx=10)

        self.edit_btn = ttk.Button(options_frame, text='Edit', command=self.edit_page)
        self.edit_btn.grid(row=0, column=4, padx=10)

        self.admin_frame = ttk.Frame(self)
        self.admin_frame.pack(fill='both', expand=True)

        self.home_page()

    def home_page(self):
        self.delete_page()
        home_frame = ttk.Frame(self.admin_frame)
        home_frame.pack(fill='both', expand=True)
        
        ttk.Label(home_frame, text="Welcome Curator", font=('bold', 30)).pack(pady=20)
        
        exit_btn = ttk.Button(home_frame, text="Exit", command=self.confirm_exit)
        exit_btn.pack(side='bottom', pady=20)

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.destroy()

    def curate_page(self):
        self.delete_page()
        #curate_frame = ttk.Frame(self.admin_frame)
        #curate_frame.pack(fill='both', expand=True)
        #ttk.Label(curate_frame, text="Curating from list", font=('bold', 20)).pack()
        createExhibit = ce.createExhibit(self.user_id,self.admin_frame)
        createExhibit.pack()

    def review_page(self):
        self.delete_page()
        #review_frame = ttk.Frame(self.admin_frame)
        #review_frame.pack(fill='both', expand=True)
        #ttk.Label(review_frame, text="Reviewing artwork", font=('bold', 20)).pack()
        review_page = rr.reviewRequest(self.admin_frame)
        review_page.pack()

    def accept_page(self):
        self.delete_page()
        #accept_frame = ttk.Frame(self.admin_frame)
        #accept_frame.pack(fill='both', expand=True)
        #ttk.Label(accept_frame, text="Accepting artwork", font=('bold', 20)).pack()
        accept_page = ar.acceptRequest(self.admin_frame)
        accept_page.pack()


    def edit_page(self):
        self.delete_page()
        #edit_frame = ttk.Frame(self.admin_frame)
        #edit_frame.pack(fill='both', expand=True)
        #ttk.Label(edit_frame, text="Editing content", font=('bold', 20)).pack()
        edit_page = ee.editExhibit(self.admin_frame)
        edit_page.pack()

    def delete_page(self):
        for widget in self.admin_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = CuratorView(0)
    app.mainloop()