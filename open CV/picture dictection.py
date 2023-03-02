# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:41:12 2023

@author: 91974
"""

import cv2
image=cv2.imread("photo.jpg",1)
resized=cv2.resize(image,(800,800),
                       interpolation=cv2.INTER_NEAREST)
while True:
    check, image=resized.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.3, 4)
for x,y,w,h in faces:
    #x=x+1
    #f=str(x)
   
    cv2.rectangle(resized,(x,y),(x+w,y+h),(0,255,255),2)
    x=x+1
    f=str(x)
    
    #cv2.rectangle(image,(x,y),(x+w , y+h) , (255,0,0),2)
    
    
    status= cv2.imwrite('Z/'+f+'.png',faces)
    cv2.imshow("image", faces)
#status= cv2.imwrite('w.png',faces)
cv2.waitKey(0)
cv2.destroyAllWindows()