import os
import requests
from replicate import Client

api_token = '9f1515e50373ad39d9512502109fbc3333be2644'
replicate = Client(api_token=api_token)

model = replicate.models.get("nightmareai/real-esrgan")
version = model.versions.get("42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b")

# https://replicate.com/nightmareai/real-esrgan/versions/42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b#input
inputs = {
    # Input image
    'image': open("flower.jpeg", "rb"),
    # Factor to scale image by
    # Range: 0 to 10
    'scale': 5,
    # Face enhance
    'face_enhance': False,
}

# https://replicate.com/nightmareai/real-esrgan/versions/42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b#output-schema
output = version.predict(**inputs)
# print(output)

response = requests.get(output)

if response.status_code == 200:
    with open("5x.jpg", "wb") as f:
        f.write(response.content)
else:
    print("Failed to download image, status code:", response.status_code)