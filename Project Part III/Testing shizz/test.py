import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

images = {}

def upload_image():
  global images
  file_path = filedialog.askopenfilename(
    initialdir="/",
    title="Select an image",
    filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"))
  )
  if file_path:
    image = Image.open(file_path)
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)
    images[file_path] = photo
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

root = tk.Tk()
root.title("Image Uploader")

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

root.mainloop()