def display():
        global counter
        if counter == 29:
                counter = 0
        try:
                if entered_text == "":
                        warning()
                        return
        except NameError:
                warning()
                return
                
        if os.path.exists('./images_generated_from_text'):
                shutil.rmtree("./images_generated_from_text")
        shutil.unpack_archive('./download.zip')
        frame = Frame(root, bg="white", bd=2, highlightbackground="black", highlightthickness=2, padx=10, pady=10)
        frame.pack(pady=20)
        frame.place(x=50, y=347)

        toDisplay = ImageTk.PhotoImage(Image.open(f".\images_generated_from_text\\0\\{counter}.jpg"))
        label  = Label(frame, image = toDisplay)
        label.image = toDisplay
        label.pack(side="left")
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
        response = requests.get(output)
        with open(f"{counter}_upscaled.jpg", "wb") as f:
                f.write(response.content)
        upscaled_image = Image.open(f".\{counter}_upscaled.jpg")
        counter += 1
        resized = upscaled_image.resize((300, 300))
        toDisplay = ImageTk.PhotoImage(resized)
        label  = Label(frame, image = toDisplay)
        label.image = toDisplay
        label.pack(side="right")