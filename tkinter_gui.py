import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()

#Below line will open application in full screen mode
# root.attributes('-fullscreen', True)
# root.state("zoomed")
#currently using custom screen size
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# root.geometry(f"{screen_width}x{screen_height}")

root.title(" Text to Image Synthesis using Generative Adversarial Networks")

def open_text():
        pass
        #################################
        #  if (os.path.exists(r".\\text.txt") != True):
        #         import paramiko
        #         ssh = paramiko.SSHClient()
        #         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #         ssh.connect(
        #         hostname="gpu.nmamit.in",
        #         port=202,
        #         username="4nm19is120",
        #         password="27102022"
        #         )
        #         sftp = ssh.open_sftp()
        #         sftp.get('/home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/Data/text.txt', 'text.txt')
        #         sftp.close()
        #         ssh.close()
        #         text_file = open("text.txt", "r")
        #         content = text_file.read()
        #         Input.insert(END, content)
        #         text_file.close()
        # elif (os.path.exists(r".\\text.txt") == True):
        #         text_file = open("text.txt", "r")
        #         content = text_file.read()
        #         Input.insert(END, content)
        #         text_file.close()
        # else:
        #         print('Something\'s wrong. I can feel it.')
        #################################



def save_text():
        global entered_text
        entered_text = entry1.get()
        if entered_text == "":
                messagebox.showwarning("Warning", "Enter some text first.")
        else:
                print(entered_text)
                entered_text=entered_text.replace(" ","_")
                print(entered_text)
                messagebox.showinfo("File Saved","Your text has been saved. \nPlease CLEAR CACHE before starting the image generation process.")

def clear_cache():
        if entered_text == "":
                messagebox.showwarning("Warning", "Enter some text first.")
        else:
                print(entered_text)
                import paramiko
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(
                        hostname="gpu.nmamit.in",
                        port=202,
                        username="4nm19is120",
                        password="27102022"
                        )
                stdin, stdout, stderr = ssh.exec_command("docker exec lightningsliver sh -c 'cd home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/text_to_image/Text-to-Image-Using-GAN-master/Data/ && ls && rm download.zip && rm -rf images_generated_from_text && rm enc_text.pkl && ls'")
                print(stdout.read().decode())
                ssh.close()
                messagebox.showinfo('Success!', 'Server Cache been successfully cleared!\n\nCLICK \'Generate Image Now\'.')


def generate():
        if entered_text == "":
                messagebox.showwarning("Warning", "Enter some text first.")
        else:
                print(entered_text)
                messagebox.showinfo('WAITING.....', 'Read the following instructions carefully:\n\nThe image generation process will begin once you press the \'OK\' button.\n\nPlease wait patiently for 5 - 10 minutes.\n\nA new dialog box will appear on your screen as soon as the image generation process finishes.\n\nCLICK \'OK\' TO START THE PROCESS.')
                ################################################
                import paramiko
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(
                hostname="gpu.nmamit.in",
                port=202,
                username="4nm19is120",
                password="27102022"
                )
                stdin, stdout, stderr = ssh.exec_command(f"docker exec lightningsliver sh -c 'cd home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/text_to_image/Text-to-Image-Using-GAN-master/ && python3 connection.py --data_set=flowers --t_dim=100 --image_size=128 --data_set=flowers --z_dim=100 --n_classes=24 --caption_vector_length=4800 --batch_size=128  --checkpoints_dir=Data/training/TAC_128/checkpoints --images_per_caption=30 --data_dir=Data --text={entered_text} && cd Data && zip -r download.zip images_generated_from_text/* && ls'")
                print(stdout.read().decode())
                sftp = ssh.open_sftp()
                sftp.get('/home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/Data/download.zip', 'download.zip')
                sftp.close()
                ssh.close()
                ################################################
                messagebox.showinfo('Success!', 'Your images have been successfully generated!\n\nCLICK \'Display Image Button\' TO SEE YOUR IMAGE.')

def display():
        if entered_text == "":
                messagebox.showwarning("Warning", "Enter some text first.")
        else:
                import shutil
                shutil.unpack_archive('./download.zip')
                print(entered_text)
                frame = Frame(root)
                frame.pack()
                frame.place(anchor='center', relx=0.5, rely=0.6)
                toDisplay = ImageTk.PhotoImage(Image.open(".\images_generated_from_text\\0\\0.jpg"))
                label  = Label(frame, image = toDisplay)
                label.image = toDisplay
                label.pack()


L = Label(text = "\n\nEnter the description of the image to be generated: \n")
L.pack()
# Input = Text(root, height = 10, width = 150, bg = "light yellow")
# Input.pack()
# Open = Button(root, height = 2, width = 20, text ="Open Text File", command = lambda:open_text())
# Open.pack()

###############################################
# This is used to take input from user
# and show it in Entry Widget.
# Whatever data that we get from keyboard
# will be treated as string.
input_text = StringVar()
entry1 = Entry(root, textvariable = input_text, justify = CENTER)
# focus_force is used to take focus
# as soon as application starts
entry1.focus_force()
entry1.pack(side = TOP, ipadx = 30, ipady = 6)
###############################################

Save = Button(root, height = 2, width = 20, text="Save Text", command = lambda:save_text())
Save.pack()
Clear = Button(root, height = 2, width = 20, text="Clear Cache", command = lambda:clear_cache())
Clear.pack()
Generate = Button(root, height = 2, width = 20, text ="Generate Image", command = lambda:generate())
Generate.pack()
Display = Button(root, height = 2, width = 20, text ="Display Image", command = lambda:display())
Display.pack()

root.mainloop()
