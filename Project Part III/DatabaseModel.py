from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk 
import sqlite3
import View as View

class DbModel:
    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        self.create_user_table()

    def create_user_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS General_User (
                User_ID INTEGER PRIMARY KEY CHECK(User_ID BETWEEN 0 AND 9999),
                Username TEXT UNIQUE NOT NULL,
                Password TEXT NOT NULL,
                Name TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def register(username,password,email,name,view,self):
        pass
        