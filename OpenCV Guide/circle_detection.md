```python

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('mp.jpeg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    area = cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(approx)
    
    if len(approx) > 8 and area > 1000:  # Adjust the conditions based on your specific case
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

plt.imshow(img)
plt.show()
```


```python

import numpy as np
import cv2

img = cv2.imread('mp.jpeg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection using Canny
edges = cv2.Canny(imgGray, 50, 150)

# Circle detection using HoughCircles
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=50, param2=30, minRadius=10, maxRadius=50)

if circles is not None:
    circles = np.uint16(np.around(circles))
    
    for i in circles[0, :]:
        center = (i[0], i[1])
        cv2.circle(img, center, i[2], (0, 0, 0), 5)
        cv2.putText(img, "Circle", (i[0]-30, i[1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


plt.imshow(img)
plt.show()
```
