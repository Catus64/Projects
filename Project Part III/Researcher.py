from tkinter import *
from tkinter import ttk, messagebox
import R_ResearchStation as rs
import R_pending_request as pr
import R_publishedWork as pw
import GR_editProfile as ep
import sqlite3

class ResearcherView(Toplevel):
    def __init__(self,user_id):
        super().__init__()
        self.title("Digital Museum - Researcher Menu")
        self.geometry('1000x700')
        self.user_id = user_id 

        options_frame = ttk.Frame(self)
        options_frame.pack(fill='x', pady=10)

        self.home_btn = ttk.Button(options_frame, text='Home', command=self.home_page)
        self.home_btn.grid(row=0, column=0, padx=10)

        self.research_btn = ttk.Button(options_frame, text='Research', command=self.research_page)
        self.research_btn.grid(row=0, column=1, padx=10)

        self.pending_btn = ttk.Button(options_frame, text='Pending Requests', command=self.pending_page)
        self.pending_btn.grid(row=0, column=2, padx=10)

        self.edit_btn = ttk.Button(options_frame, text='Edit Profile', command=self.edit_profile)
        self.edit_btn.grid(row=0, column=3, padx=10)

        self.published_btn = ttk.Button(options_frame, text='Published Work', command=self.published_page)
        self.published_btn.grid(row=0, column=4, padx=10)

        self.admin_frame = ttk.Frame(self)
        self.admin_frame.pack(fill='both', expand=True)

        self.home_page()

    def home_page(self):
        self.delete_page()
        home_frame = ttk.Frame(self.admin_frame)
        home_frame.pack(fill='both', expand=True)
        
        ttk.Label(home_frame, text="Welcome Researcher "+str(self.user_id), font=('bold', 30)).pack(pady=20)
        
        exit_btn = ttk.Button(home_frame, text="Exit", command=self.confirm_exit)
        exit_btn.pack(side='bottom', pady=20)

    def confirm_exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.destroy()

    def research_page(self):
        self.delete_page()
        researchStation = rs.researchStation(self.user_id,self.admin_frame)
        researchStation.pack()

    def pending_page(self):
        self.delete_page()
        pending_page = pr.pendingRequest(self.user_id,self.admin_frame)
        pending_page.pack()

    def edit_profile(self):
        self.delete_page()
        #edit_frame = ttk.Frame(self.admin_frame)
        #edit_frame.pack(fill='both', expand=True)
        #ttk.Label(edit_frame, text="Edit Profile", font=('bold', 20)).pack()
        edit_frame = ep.editProfile(self.user_id,"Researcher",self.admin_frame)
        edit_frame.pack()

    def published_page(self):
        self.delete_page()
        published_page = pw.publishedWork(self.user_id,self.admin_frame)
        published_page.pack()
        #published_frame = ttk.Frame(self.admin_frame)
        #published_frame.pack(fill='both', expand=True)
        #ttk.Label(published_frame, text="Published Work", font=('bold', 20)).pack()

    def delete_page(self):
        for widget in self.admin_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = ResearcherView(1)
    app.mainloop()