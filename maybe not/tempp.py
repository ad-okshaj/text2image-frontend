

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
        global counter
        try:
                if entered_text == "":
                        warning()
        except NameError:
                warning()
                return
        try:
                counter -= 1
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
                        counter += 1              
                        return
                else:
                        print("Failed to download image, status code:", response.status_code)
                        messagebox.showinfo('Server Issue!', 'Cannot connect to Server.')
                        return
        except FileNotFoundError:
                messagebox.showinfo('Zip File or Image Not Found!', 'Please Generate Image before using Upscale / Downscale Image function.')                
                return

def display_upscale():
        global counter
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
                counter -= 1
                upscaled_image = Image.open(f".\{counter}_upscaled.jpg")
                counter += 1
                resized = upscaled_image.resize((300, 300))
                toDisplay = ImageTk.PhotoImage(resized)
                label  = Label(frame, image = toDisplay)
                label.image = toDisplay
                label.pack(side="right")
        except shutil.ReadError:
                messagebox.showinfo('Error', 'Error')
                return
