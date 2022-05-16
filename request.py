# import required module
import os
import requests
import sys
import cv2
import numpy as np
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

files['file2'] = ("input/0001/0001 (copy).jpg", open("input/0001/0001 (copy).jpg", 'rb'))
files['file3'] = ("input/0001/0001 (copy).jpg", open("input/0001/0001 (copy).jpg", 'rb'))
files['file4'] = ("input/0001/0001 (copy).jpg", open("input/0001/0001 (copy).jpg", 'rb'))

        
r = requests.post(url, files=files)

rawbytes = r.content

stream = BytesIO(rawbytes)


nparr = np.fromstring(rawbytes, np.uint8)
image = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR in OpenCV 3.1
cv2.imwrite("converted.png", image[0:int(image.shape[0]/2),0:int(image.shape[1]/2)])
