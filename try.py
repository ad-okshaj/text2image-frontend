import tkinter as tk
from tkinter import PhotoImage

def show_image():
    image = PhotoImage(file="spider.png")
    label = tk.Label(root, image=image)
    label.image = image  # Keep a reference to the image to avoid garbage collection
    label.pack()

root = tk.Tk()

button = tk.Button(root, text="Show Image", command=show_image)
button.pack()

root.mainloop()
