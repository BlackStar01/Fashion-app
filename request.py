# import required module
import os
import cv2
import requests
import base64
import sys
import simplejson
from PIL import Image
from io import BytesIO


def cast_bytes_to_str(mess):
    return mess.__str__().rpartition("b'")[2].rpartition("'")[0]

activationSignal = -0.7
urlS = 'http://localhost:5000/predict?minPredictionValue='+ str(activationSignal)
urlR = 'https://upscaler.zyro.com/v1/ai/image-upscaler'

# assign directory
directory = 'input/0001'
 
files = {
    'Content-Type': 'image/jpeg'
}
# iterate over files in
# that directory

for file in os.scandir(directory):
    if file.is_file(): 
        files['file1'] = (file.path, open(file.path, 'rb'))
        break

files['file2'] = ("input/0001/0001.jpg", open("input/0001/0001.jpg", 'rb'))
files['file3'] = ("input/0001/0001.jpg", open("input/0001/0001.jpg", 'rb'))
files['file4'] = ("input/0001/0001.jpg", open("input/0001/0001.jpg", 'rb'))

        
r = requests.post(urlS, files=files)

rawbytes = r.content

stream = BytesIO(rawbytes)

image = Image.open(stream).convert("RGBA")
stream.close()
image.save("converted.png", format="png")


img = cv2.imread('converted.png', cv2.IMREAD_UNCHANGED)

height = img.shape[0]
width = img.shape[1]

cv2.imwrite("converted.png", img[:int(height/2), :int(width/2)])



with open("converted.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

r = requests.post(urlR, json={'image_data':cast_bytes_to_str(encoded_string)})

response_image = r.json()["upscaled"].__str__().rpartition("data:image/PNG;base64,")[2]
print(response_image)
""" with open("result.png",'wb') as f:
   f.write(bytes(response_image,'utf-8'))
 """

Image.open(BytesIO(base64.b64decode(response_image))).save('result.png', 'PNG')