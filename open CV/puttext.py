# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:33:27 2023

@author: 91974
"""

import cv2

image=cv2.imread('pexel.jpeg',1)
position=(800,300)
cv2.putText(
    image,#image on which text is written
    "python Example",#text)
    position,
    cv2.FONT_HERSHEY_SIMPLEX,#font family
    1, #font size
    (0,0,255,255),#font color
    3)#font stroke


cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyallwindows()