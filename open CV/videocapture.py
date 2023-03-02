# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 12:39:37 2023

@author: 91974
"""

import cv2
cam=cv2.VideoCapture(0)
while True:
    check,frame=cam.read()
    #cv2.imshow('video',frame)
    e=0
    for i in range(0,50):
        e=e+i
        c=str(i)
        cv2.imwrite('i/'+c+'.jpg',frame)
        cv2.imshow('video',frame)
        if (e==10):
            cam.release()
            cv2.destroyAllWindows