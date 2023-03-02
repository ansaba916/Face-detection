# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:40:29 2023

@author: 91974
"""

import cv2

#black and white (grey scale)

img=cv2.imread("form.jpeg",1)

cv2.imshow("Data",img)

cv2.waitKey(0)

#cv2.waitKey(2000)

cv2.destroyallwindows()
