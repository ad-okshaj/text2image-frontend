def display():
        Output.config(state=NORMAL)
        Output.delete("1.0", END)
        Output.image_create(END, image=toDisplay)
        Output.config(state=DISABLED)


L = Label(text = "\n\nEnter the description of the image to be generated: ")
Input = Text(root, height = 10, width = 150, bg = "light yellow")
# Output = Text(root, height = 10, width = 20, state=DISABLED)
Open = Button(root, height = 2, width = 20, text ="Create / Open Text File", command = lambda:open_text())
Save = Button(root, height = 2, width = 20, text="Save File", command = lambda:save_text())
Generate = Button(root, height = 2, width = 20, text ="Generate Image", command = lambda:generate())
Display = Button(root, height = 2, width = 20, text ="Display Image", command = lambda:display())

L.pack()
Input.pack()
Open.pack()
Save.pack()
Generate.pack()
Display.pack()
frame = Frame(root)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.6)
toDisplay = ImageTk.PhotoImage(Image.open("0.jpg"))
Label = Label(frame, image = toDisplay)
Label.pack()

mainloop()
