from tkinter import *

def display_image():
    text_widget.config(state=NORMAL)
    text_widget.image_create(END, image=img)
    text_widget.config(state=DISABLED)

root = Tk()

text_widget = Text(root, height=20, width=150, state=DISABLED)
text_widget.pack()

img = PhotoImage(file="sheep.gif")

display_button = Button(root, text="Display Image", command=display_image)
display_button.pack()

root.mainloop()
