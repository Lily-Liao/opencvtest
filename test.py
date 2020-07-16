import cv2
import numpy as np 
from matplotlib import pyplot as plt
#####################################
img=cv2.imread('dog3.jpg')
aa=img[100:300,100:300]
bb=img[300:500,300:500]
dst=cv2.addWeighted(aa,0.7,bb,0.3,0)
img[200:400,200:400]=dst
print(img)

cv2.imshow('dog3',img) #開啟新視窗名稱為res的視窗
cv2.waitKey(0) 
cv2.destroyAllWindows()

#####################################
# img=cv2.imread('dog3.jpg')
# img[100:150,100:150,1]=127
# aa=img[:,300:500]
# img[:,100:300]=aa
# img[:,:,2]=0
# # dst=cv2.addWeighted(img,0.7,aa,0.3,0)

# print(img)

# cv2.imshow('dog',img) #開啟新視窗名稱為res的視窗
# cv2.waitKey(0) 
# cv2.destroyAllWindows()

#########################################
# img=cv2.imread('dog.jpg')
# img[100:150,100:150,1]=127
# # img[100:150,100:150,1]=0
# # img[:,:,1]=0
# img[:,:,2]=0
# print(img)

# cv2.imshow('dog',img) #開啟新視窗名稱為res的視窗
# cv2.waitKey(0) 
# cv2.destroyAllWindows()

########################################
# img=cv2.imread('dog.jpg',cv2.IMREAD_GRAYSCALE)

# #cv2.imwrite('dog5.jpg',img)
# img2=cv2.imread('dog2.jpg')
# img3=cv2.imread('dog3.jpg')
# print(img)
# cv2.imshow('dog',img) #開啟新視窗名稱為res的視窗
# cv2.imshow('dog2',img2)
# cv2.imshow('dog3',img3) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows()


#######################################

# img3=cv2.imread('dog3.jpg')
# plt.imshow(img3,cmap='gray',interpolation='bicubic')
# plt.title('dog')
# plt.xticks([])
# plt.yticks([])
# plt.show()

#######################################
