import os
import shutil
from tkinter import Tk, Button, Label, filedialog, messagebox

# Function to handle the file import
def import_picture():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),
            ("All Files", "*.*"),  # Fallback to allow any file type
            ("PNG", "*png"),
            ("JPG", "*jpg")
        ]
    )
    
    if file_path:
        # Check if the images directory exists, if not, create it
        if not os.path.exists("images"):
            os.makedirs("images")
        
        # Get the file name from the path
        file_name = os.path.basename(file_path)
        
        # Define the destination path
        destination_path = os.path.join("images", file_name)
        
        try:
            # Copy the file to the images directory
            shutil.copy(file_path, destination_path)
            
            # Show a success message
            messagebox.showinfo("Success", f"Image '{file_name}' has been imported to 'images/' directory.")
        except Exception as e:
            # Show an error message if something goes wrong
            messagebox.showerror("Error", f"Failed to import image: {e}")

# Create the main window
root = Tk()
root.title("Image Importer")
root.geometry("300x100")

# Create a label
label = Label(root, text="Click the button to import an image")
label.pack(pady=10)

# Create a button to trigger the import
import_button = Button(root, text="Import Image", command=import_picture)
import_button.pack(pady=10)

# Run the application
root.mainloop()