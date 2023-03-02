# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:21:02 2023

@author: 91974
"""

import cv2

img=cv2.imread('pexel.jpeg',1)
print(img.shape)

img_resized=cv2.resize(img,(500,500),
                       interpolation=cv2.INTER_NEAREST)
print(img_resized.shape)

image=cv2.rotate(img_resized,cv2.ROTATE_90_COUNTERCLOCKWISE)
status=cv2.imwrite("rotated img.png",image)
cv2.imshow("img",image)
cv2.waitKey(0)
cv2.destroyAllWindows()