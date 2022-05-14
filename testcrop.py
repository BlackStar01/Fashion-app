import cv2

img = cv2.imread('./output/0001/segmentated.png', cv2.IMREAD_UNCHANGED)
# start vertical devide image
height = img.shape[0]
width = img.shape[1]
# Cut the image in half
width_cutoff = width // 2
left1 = img[:, :width_cutoff]
right1 = img[:, width_cutoff:]
# finish vertical devide image


#save

cv2.imwrite("img_spliced.png", img[:int(height/2), :int(width/2)])