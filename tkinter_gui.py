from tkinter import *
from tkinter import messagebox

import os
root = Tk()

#Below line will open application in full screen mode
#root.attributes('-fullscreen', True)
#currently using custom screen size
root.geometry("1400x700")
root.title(" Text to Image Synthesis using Generative Adversarial Networks.")

def open_text():
        if (os.path.exists(r".\Data") != True):
                os.mkdir(r".\Data")
        if (os.path.exists(r".\Data\text.txt") != True):
                os.chdir(r".\Data")
                text_file = open("text.txt", "x")
                text_file = open("text.txt", "w")
                text_file.write("a flower with red petals which are pointed\nmany pointed petals\nA yellow flower")
                text_file.close()
                text_file = open("text.txt", "r")
                content = text_file.read()
                inputtext.insert(END, content)
                text_file.close()
                os.chdir(r"..")
        elif (os.path.exists(r".\Data\text.txt") == True):
                os.chdir(r".\Data")
                text_file = open("text.txt", "r")
                content = text_file.read()
                inputtext.insert(END, content)
                text_file.close()
                os.chdir(r"..")
        else:
                print('Something\'s wrong. I can feel it.')

def save_text():
        os.chdir(r".\Data")
        text_file = open("text.txt", "w")
        text_file.write(inputtext.get(1.0, END))
        text_file.close()
        os.chdir(r"..")
        messagebox.showinfo("File Saved.","Your text has been saved.\nPlease proceed with Image Generation.\nClick 'Generate Image' button now.")


def take_input():
        #Below input variable will contain the INPUT of user, which has to be sent to server
	INPUT = inputtext.get("1.0", "end-1c")
	#To check whether the INPUT is passed in separate lines or not
	Output.insert(END, INPUT)
    
	
l = Label(text = "Enter the description of the image to be generated: ")
inputtext = Text(root, height = 10, width = 150, bg = "light yellow")
Output = Text(root, height = 20, width = 150)
open_button = Button(root, height = 2, width = 20, text ="Create / Open Text File", command = lambda:open_text())
save = Button(root, height = 2, width = 20, text="Save File", command = lambda:save_text())
Display = Button(root, height = 2, width = 20, text ="Generate Image", command = lambda:take_input())

l.pack()
inputtext.pack()
open_button.pack()
save.pack()
Display.pack()
Output.pack()

mainloop()
