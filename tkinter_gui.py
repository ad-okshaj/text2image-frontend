import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()

#Below line will open application in full screen mode
# root.attributes('-fullscreen', True)
root.state("zoomed")
#currently using custom screen size
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# root.geometry(f"{screen_width}x{screen_height}")

root.title(" Text to Image Synthesis using Generative Adversarial Networks")

def open_text():
        # if (os.path.exists(r".\text.txt") != True):
        #         text_file = open("text.txt", "x")
        #         text_file = open("text.txt", "w")
        #         text_file.write("a flower with red petals which are pointed\nmany pointed petals\nA yellow flower")
        #         text_file.close()
        #         text_file = open("text.txt", "r")
        #         content = text_file.read()
        #         inputtext.insert(END, content)
        #         text_file.close()
        #         os.chdir(r"..")
        # elif (os.path.exists(r".\Data\text.txt") == True):
        #         os.chdir(r".\Data")
        #         text_file = open("text.txt", "r")
        #         content = text_file.read()
        #         inputtext.insert(END, content)
        #         text_file.close()
        #         os.chdir(r"..")
        # else:
        #         print('Something\'s wrong. I can feel it.')
        #################################
 
        #################################
        if (os.path.exists(r".\\text.txt") != True):
                import paramiko
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(
                hostname="gpu.nmamit.in",
                port=202,
                username="4nm19is120",
                password="27102022"
                )
                sftp = ssh.open_sftp()
                sftp.get('/home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/Data/text.txt', 'text.txt')
                sftp.close()
                ssh.close()
                text_file = open("text.txt", "r")
                content = text_file.read()
                Input.insert(END, content)
                text_file.close()
        elif (os.path.exists(r".\\text.txt") == True):
                text_file = open("text.txt", "r")
                content = text_file.read()
                Input.insert(END, content)
                text_file.close()
        else:
                print('Something\'s wrong. I can feel it.')


def save_text():
        # os.chdir(r".\Data")
        # text_file = open("text.txt", "w")
        # text_file.write(inputtext.get(1.0, END))
        # text_file.close()
        # os.chdir(r"..")
        # messagebox.showinfo("File Saved","Your text has been saved.\nPlease proceed with Image Generation.\nClick 'Generate Image' button now.")
        text_file = open("text.txt", "w")
        text_file.write(Input.get(1.0, END))
        text_file.close()
        ###################################################
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
                hostname="gpu.nmamit.in",
                port=202,
                username="4nm19is120",
                password="27102022"
                )
        sftp = ssh.open_sftp()
        sftp.put('text.txt', '/home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/Data/text.txt')
        sftp.close()
        ssh.close()
        ###################################################
        messagebox.showinfo("File Saved","Your text has been saved and uploaded.\nPlease proceed with Image Generation.\nClick 'Generate Image' button now.")


def generate():
        # #Below input variable will contain the INPUT of user, which has to be sent to server
	# INPUT = inputtext.get("1.0", "end-1c")
	# #To check whether the INPUT is passed in separate lines or not
	# Output.insert(END, INPUT)
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
        stdin, stdout, stderr = ssh.exec_command("docker exec lightningsliver sh -c 'cd home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/text_to_image/Text-to-Image-Using-GAN-master/ && python3 generate_images_original.py --data_set=flowers --t_dim=100 --image_size=128 --data_set=flowers --z_dim=100 --n_classes=24 --caption_vector_length=4800 --batch_size=128  --checkpoints_dir=Data/training/TAC_128/checkpoints --images_per_caption=30 --data_dir=Data && cd Data && rm download.zip && zip -r download.zip images_generated_from_text/* && ls'")
        print(stdout.read().decode())

        sftp = ssh.open_sftp()
        sftp.get('/home/4nm19is120/text_to_image/Text-to-Image-Using-GAN-master/Data/download.zip', 'download.zip')
        sftp.close()
        ssh.close()

        import shutil
        shutil.unpack_archive('./download.zip')
        ################################################

        # messagebox.showinfo('Success!', 'Your images have been successfully generated!\n\nCLICK \'OK\' TO SEE YOUR IMAGE.')

def display():
        frame = Frame(root)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.6)
        toDisplay = ImageTk.PhotoImage(Image.open("0.jpg"))
        label  = Label(frame, image = toDisplay)
        label.image = toDisplay
        label.pack()


L = Label(text = "\n\nEnter the description of the image to be generated: ")
L.pack()
Input = Text(root, height = 10, width = 150, bg = "light yellow")
Input.pack()
# Output = Text(root, height = 10, width = 20, state=DISABLED)
Open = Button(root, height = 2, width = 20, text ="Open Text File", command = lambda:open_text())
Open.pack()
Save = Button(root, height = 2, width = 20, text="Save & Upload Text File", command = lambda:save_text())
Save.pack()
Generate = Button(root, height = 2, width = 20, text ="Generate Image", command = lambda:generate())
Generate.pack()
Display = Button(root, height = 2, width = 20, text ="Display Image", command = lambda:display())
Display.pack()

root.mainloop()
