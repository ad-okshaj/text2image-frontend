import os
import paramiko
import requests
import shutil
from replicate import Client
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()

counter = 0

#Below line will open application in full screen mode
# root.attributes('-fullscreen', True)
# root.state("zoomed")
#currently using custom screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

root.title("Text to Image Synthesis using Generative Adversarial Networks")

def warning():
        messagebox.showwarning("Warning", "Enter and Save some text first.")

def save_text():
        global entered_text
        entered_text = entry1.get()
        if entered_text == "":
                warning()
        else:
                print(entered_text)
                entered_text=entered_text.replace(" ","_")
                print(entered_text)
                messagebox.showinfo("File Saved","Your text has been saved. \nPlease CLEAR CACHE before starting the image generation process.")

def clear_cache():
        try:
                #print('inside first try block')
                if entered_text == "":
                        warning()
                        return
        except NameError:
                #print('inside NameError Block')
                warning()
                return
        try:
                #print('inside 2nd try block')
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
        except TimeoutError:
                #print('inside TimeoutError block')
                messagebox.showinfo('Server Issue!', 'Cannot connect to Server.')
                return
        else:
                #print('inside else block')
                messagebox.showinfo('Success!', 'Server Cache been successfully cleared!\n\nCLICK \'Generate Image Now\'.')

def generate():
        try:
                if entered_text == "":
                        warning()
                        return
        except NameError:
                warning()
                return
        try:
                # print(entered_text)
                messagebox.showinfo('WAITING.....', 'Read the following instructions carefully:\n\nThe image generation process will begin once you press the \'OK\' button.\n\nPlease wait patiently for 5 - 10 minutes.\n\nA new dialog box will appear on your screen as soon as the image generation process finishes.\n\nCLICK \'OK\' TO START THE PROCESS.')
                ################################################
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
        except TimeoutError:
                print('inside TimeoutError block')
                messagebox.showinfo('Server Issue!', 'Cannot connect to Server.')
                return

#red flower
def display():
        global counter
        if counter == 29:
                counter = 0
        try:
                if entered_text == "":
                        warning()
        except NameError:
                warning()
                return
        try:
                #import shutil
                shutil.unpack_archive('./download.zip')
                # print(entered_text)
                # frame = Frame(root)
                # frame.pack()
                # frame.place(anchor='center', relx=0.5, rely=0.6)
                toDisplay = ImageTk.PhotoImage(Image.open(f".\images_generated_from_text\\0\\{counter}.jpg"))
                counter += 1
                label  = Label(frame, image = toDisplay)
                label.image = toDisplay
                label.pack(side="left")
        except shutil.ReadError:
                messagebox.showinfo('Zip File or Image Not Found!', 'Please Generate Image before using Display Image function.')
                return

def upscale():
        try:
                if entered_text == "":
                        warning()
        except NameError:
                warning()
                return
        try:
                api_token = '9f1515e50373ad39d9512502109fbc3333be2644'
                replicate = Client(api_token=api_token)
                model = replicate.models.get("nightmareai/real-esrgan")
                version = model.versions.get("42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b")
                inputs = {
                'image': open(f'images_generated_from_text/0/{counter}.jpg', 'rb'),
                'scale': 5,
                'face_enhance': False,
                }
                output = version.predict(**inputs)
                # print(output)
                response = requests.get(output)
                if response.status_code == 200:
                        with open(f"{counter}_upscaled.jpg", "wb") as f:
                                f.write(response.content)
                        messagebox.showinfo('Success', 'Success')                
                        return
                else:
                        print("Failed to download image, status code:", response.status_code)
                        messagebox.showinfo('Server Issue!', 'Cannot connect to Server.')
                        return
        except FileNotFoundError:
                messagebox.showinfo('Zip File or Image Not Found!', 'Please Generate Image before using Upscale / Downscale Image function.')                
                return

def display_upscale():
        try:
                if entered_text == "":
                        warning()
        except NameError:
                warning()
                return
        try:
                # frame = Frame(root)
                # frame.pack()
                # frame.place(anchor='center', relx=0.5, rely=0.6)
                upscaled_image = Image.open(f".\{counter}_upscaled.jpg")
                resized = upscaled_image.resize((300, 300))
                toDisplay = ImageTk.PhotoImage(resized)
                label  = Label(frame, image = toDisplay)
                label.image = toDisplay
                label.pack(side="right")
        except shutil.ReadError:
                messagebox.showinfo('Error', 'Error')
                return


L = Label(text = "\n\nEnter the description of the image to be generated: \n")
L.pack()

input_text = StringVar()
entry1 = Entry(root, textvariable = input_text, justify = CENTER)
entry1.focus_force()
entry1.pack(side = TOP, ipadx = 30, ipady = 6, pady=20)

Save = Button(root, height = 2, width = 20, text="Save Text", command = lambda:save_text())
Save.pack()
Clear = Button(root, height = 2, width = 20, text="Clear Cache", command = lambda:clear_cache())
Clear.pack()
Generate = Button(root, height = 2, width = 20, text ="Generate Image", command = lambda:generate())
Generate.pack()
Display = Button(root, height = 2, width = 20, text ="Display / Change Image", command = lambda:display())
Display.pack()
Upscale = Button(root, height = 2, width = 20, text ="Upscale / Downscale Image", command = lambda:upscale())
Upscale.pack()
Upscale = Button(root, height = 2, width = 20, text ="Display Upscaled Image", command = lambda:display_upscale())
Upscale.pack()


frame = Frame(root, bg="white", bd=2, highlightbackground="black", highlightthickness=2, padx=10, pady=10)
frame.pack(pady=20)

label = Label(frame, text="This is a label")
button = Button(frame, text="Click me")

# label.pack(side="left")
# button.pack(side="right")

root.mainloop()
