import tkinter as tk

# Create the tkinter window
window = tk.Tk()

# Load the two images
image1 = tk.PhotoImage(file="5_upscaled.jpg")
image2 = tk.PhotoImage(file="9_upscaled.jpg")

# Create frames for the images
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)

# Create labels to display the images in the frames
label1 = tk.Label(frame1, image=image1)
label2 = tk.Label(frame2, image=image2)

# Pack the labels inside the frames
label1.pack()
label2.pack()

# Pack the frames side by side
frame1.pack(side="left")
frame2.pack(side="left")

# Start the tkinter event loop
window.mainloop()
