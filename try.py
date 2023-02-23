import tkinter as tk
import concurrent.futures
import requests
from openai import Client

def process_data():
    message_window = tk.Toplevel(root)
    message_window.title("Processing Data")
    message_window.geometry("200x100")
    label = tk.Label(message_window, text="Processing, Please Wait...")
    label.pack(padx=20, pady=10)
    return message_window

def upscale_image():
    message_window = process_data()
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
    message_window.destroy()

def start_processing():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(upscale_image)

root = tk.Tk()

button = tk.Button(root, text="Start Processing", command=start_processing)
button.pack(padx=20, pady=10)

root.mainloop()