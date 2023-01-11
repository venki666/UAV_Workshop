# access_modify_pixel.py


import cv2
import numpy as np


# read image
img = cv2.imread("images/shapes.jpg")


# pixel at point [10, 10] = white i.e. 255, 255, 255
px = img[10, 10]
print("original pixel: ", px) # [255 255 255]
cv2.imshow("Shapes", img)


# modify pixel to red : a dot can be seen in the image
img[10, 10] = (0, 0, 255)
px = img[10, 10]
print("Modified pixel: ", px) # [255 0 0]
cv2.imshow("Red dot at (10 10)", img)


# access the shape of the image
(h, w) = img.shape[:2] # height and width of image
print("height={}, width={}".format(h,w)) # height=360, width=640

print("Image size = ", img.size) # size of image = h*w*3 = 691200


cv2.waitKey(0)