# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:07:42 2023

@author: 91974
"""

import cv2

#black and white (grey scale)

img=cv2.imread("pexel.jpeg",1)
img_resized=cv2.resize(img,(500,500),
                       interpolation=cv2.INTER_NEAREST)


#save image
status=cv2.imwrite("lights.jpeg",img_resized)
cv2.imshow("data",img_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()