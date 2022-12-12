#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Muhammet\Desktop\foto.jpeg")
kernel = np.ones((5,5), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img)
cv2.imshow('Dilation', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

