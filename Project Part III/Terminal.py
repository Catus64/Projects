from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk
from tkinter import ttk 

from tkinter import Tk
import View as view_module
import Controller as controller_module
import DatabaseModel as db_model_module

# Initialize database model first
dbModel = db_model_module.DbModel()

# Pass the database model to the controller
cntrl = controller_module.Controller(dbModel)

# Pass the controller to the view
view = view_module.View(cntrl)

# Run the GUI
view.mainloop()



