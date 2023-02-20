import tkinter as tk

# Create the tkinter window
window = tk.Tk()

# Create a canvas widget
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

# Draw a black box on the canvas
canvas.create_rectangle(50, 50, 150, 150, fill="black")

# Start the tkinter event loop
window.mainloop()
