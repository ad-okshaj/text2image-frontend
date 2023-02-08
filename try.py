import tkinter as tk

def save_text():
    entered_text = entry.get()
    print(entered_text)

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

save_button = tk.Button(root, text="Save Entered Text", command=save_text)
save_button.pack()

root.mainloop()
