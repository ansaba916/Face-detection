# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:46:38 2023

@author: 91974
"""

import cv2

cam=cv2.VideoCapture("http://100.73.34.113:4747/video")


while True:
    check, frame = cam.read()
    cv2.imshow('video',frame)
    key=cv2.waitKey(1)
    if key==27:
        break
    
cam.release()
cv2.destroyAllWindows
    