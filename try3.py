import tkinter as tk
from PIL import Image, ImageTk

# Create the tkinter window
window = tk.Tk()

# Open the image and resize it to 300x300 pixels
image = Image.open("1_upscaled.jpg")
resized_image = image.resize((300, 300))

# Convert the resized image to a format that tkinter can display
tk_image = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
label = tk.Label(window, image=tk_image)
label.pack()

# Start the tkinter event loop
window.mainloop()
