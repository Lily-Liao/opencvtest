import numpy as np 
import cv2 

img=np.zeros((512,512,3), np.uint8) 
#img[:,:,2]=255

#draw a line
cv2.line(img,(0,0),(511,511),(255,0,0),5)
#draw a rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#draw a circle
cv2.circle(img,(447,63),63,(0,0,255),-1)
#draw an ellipse
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#write OpenCV on the img picture(p.s don't write chinese or install other library to write)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

cv2.imshow('line',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 