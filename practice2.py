import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('onepunch2.jpg')
img=cv2.cvtColor(img1,cv2.COLOR_BGRA2GRAY)
edges = cv2.Canny(img, 1, 100)
edges2 = cv2.Canny(img, 5, 100)
edges3 = cv2.Canny(img, 25, 150)
edges4 = cv2.Canny(img, 33, 200)
edges5 = cv2.Canny(img, 50, 255)

plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('Original Image',fontsize=7)
plt.subplot(232), plt.imshow(edges, cmap='gray'), plt.title('Edge Image',fontsize=7)
plt.subplot(233), plt.imshow(edges2, cmap='gray'), plt.title('Edge Image',fontsize=7)
plt.subplot(234), plt.imshow(edges3, cmap='gray'), plt.title('Edge Image',fontsize=7)
plt.subplot(235), plt.imshow(edges4, cmap='gray'), plt.title('Edge Image',fontsize=7)
plt.subplot(236), plt.imshow(edges5, cmap='gray'), plt.title('Best Edge Image',fontsize=7)
plt.subplots_adjust(wspace =0.5, hspace =0.5)

plt.show()