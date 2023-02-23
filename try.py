from tkinter import *

root = Tk()

# create a Frame widget to hold the image
image_frame = Frame(root)
image_frame.pack()

counter = 0
# create an initial image and add it to the image frame
image = PhotoImage(file=f"{counter}.gif")
image_label = Label(image_frame, image=image)
image_label.pack()

def prev_img():
    global counter
    counter -= 1
    if counter < 0:
        counter = 0
    new_image = PhotoImage(file=f"{counter}.gif")
    image_label.config(image=new_image)
    image_label.image = new_image
    
def next_img():
    global counter
    counter += 1
    new_image = PhotoImage(file=f"{counter}.gif")
    image_label.config(image=new_image)
    image_label.image = new_image

# button = Button(root, text="Change Image", command=change_image)
# button.pack()

prevButton = Button(root, text="Previous Image", height = 2, width = 20, bd=1, relief="solid", highlightthickness=1, highlightbackground="black", command = lambda:prev_img())
prevButton.pack(side=LEFT, padx=4, pady=5)

nextButton = Button(root, text="Next Image", height = 2, width = 20, bd=1, relief="solid", highlightthickness=1, highlightbackground="black", command = lambda:next_img())
nextButton.pack(side=LEFT, padx=4, pady=5)

root.mainloop()

# import tkinter as tk

# root = tk.Tk()

# # create a Frame widget to hold the image
# image_frame = tk.Frame(root)
# image_frame.pack()

# # create an initial image and add it to the image frame
# initial_image = tk.PhotoImage(file="image1.gif")
# new_image = tk.PhotoImage(file="image2.gif")
# current_image = initial_image  # keep track of the current image being displayed
# image_label = tk.Label(image_frame, image=current_image)
# image_label.pack()

# # create a function to toggle between the images
# def change_image():
#     global current_image  # use the global keyword to modify the current_image variable
#     if current_image == initial_image:
#         current_image = new_image
#     else:
#         current_image = initial_image
#     image_label.config(image=current_image)
#     image_label.image = current_image  # keep a reference to the image to avoid garbage collection

# # create a button to change the image
# button = tk.Button(root, text="Change Image", command=change_image)
# button.pack()

# root.mainloop()

