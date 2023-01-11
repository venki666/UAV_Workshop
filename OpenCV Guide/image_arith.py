#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 00:15:57 2023

@author: venkatesanmuthukumar
"""

# image_arith.py

import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])

print("OpenCV 250 + 10: ", cv2.add(x,y)) # 250+10 = 260 => 255
print("Numpy 250 + 10: ", x+y)          # 250+10 = 260 % 256 = 4


img = cv2.imread("images/shapes.jpg")
cv2.imshow("Shapes", img)


print("Initial pixel at [50, 50]\t: ", img[50, 50])
new_pixel =  90 * np.ones(img.shape, dtype = "uint8")

print("Add/subtract 90")

opencv_img = cv2.add(img, new_pixel)
print("OpenCV addition pixel at [50, 50]\t: ", opencv_img[50, 50])
cv2.imshow("OpenCV add", opencv_img)

opencv_img = cv2.subtract(img, new_pixel)
print("OpenCV subtract pixel at [50, 50]\t: ", opencv_img[50, 50])
cv2.imshow("OpenCV subtract", opencv_img)


numpy_img = img + new_pixel
print("Numpy addition pixel at [50, 50]\t: ", opencv_img[50, 50])
cv2.imshow("Numpy add", numpy_img)

numpy_img = img - new_pixel
print("Numpy subtract pixel at [50, 50]\t: ", opencv_img[50, 50])
cv2.imshow("Numpy subtract", numpy_img)

cv2.waitKey(0)
