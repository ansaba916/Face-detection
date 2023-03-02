# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:54:26 2023

@author: 91974
"""

import cv2

#using imread("path")and 1 denotes read as color image

img=cv2.imread('form.jpeg',1)
print(img.shape)
img_resized=cv2.resize(img,(500,500),
                       interpolation=cv2.INTER_NEAREST)

print(img_resized.shape)
cv2.imshow('Resized',img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()