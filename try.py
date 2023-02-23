import tkinter as tk

# Create the window
window = tk.Tk()
window.title("My Window")

# Set the window size and position it in the center of the screen
window.geometry("300x200+{}+{}".format(int(window.winfo_screenwidth()/2 - 150), int(window.winfo_screenheight()/2 - 100)))

# Set a label to display a message
label = tk.Label(window, text="Hello, World!")
label.pack(pady=50)

# Call the destroy() method on the window after 2000 milliseconds (2 seconds)
window.after(1500, window.destroy)

# Run the main event loop
window.mainloop()
