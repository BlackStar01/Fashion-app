# import required module
import os
import cv2
import requests
import sys
from PIL import Image
from io import BytesIO

activationSignal = -0.7
url = 'http://localhost:5000/predict?minPredictionValue='+ str(activationSignal);

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

        
r = requests.post(url, files=files)

rawbytes = r.content

stream = BytesIO(rawbytes)

image = Image.open(stream).convert("RGBA")
stream.close()
image.save("converted.png", format="png")


img = cv2.imread('converted.png', cv2.IMREAD_UNCHANGED)

height = img.shape[0]
width = img.shape[1]

cv2.imwrite("converted.png", img[:int(height/2), :int(width/2)])