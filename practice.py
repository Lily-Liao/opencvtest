import cv2
import numpy as np
import matplotlib.pylab as plt


img = cv2.imread('1punch.jpg',cv2.COLOR_RGB2BGR)
# rows, cols, ch = img.shape
# print(rows,cols)
# 设置标记点和目标点
markpoint = [[449, 305], [1985, 409], [657, 3809], [2505, 3377]]
dstpoint = [[0, 0], [250, 0], [0, 450], [250, 450]]
# 强调标记点
for i in markpoint:
    cv2.circle(img, tuple(i), 30, (0, 255, 0), -1)
# 转换点的格式
pts1 = np.float32(markpoint)
pts2 = np.float32(dstpoint)

# 生成透视矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)
img1=cv2.cvtColor(img,cv2.COLOR_BGRA2RGB)
# 转换
dst = cv2.warpPerspective(img1, M, (250, 450))
plt.subplot(121), plt.imshow(img1), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

######################################################
# img = cv2.imread('1punch.jpg',cv2.COLOR_RGB2BGR)
# # rows, cols, ch = img.shape
# # print(rows,cols)
# # 设置标记点和目标点
# markpoint = [[449, 305], [1985, 409], [657, 3809], [2505, 3377]]
# dstpoint = [[0, 0], [250, 0], [0, 450], [250, 450]]
# print(img)
# # 强调标记点
# for i in markpoint:
#     cv2.circle(img, tuple(i), 30, (0, 255, 0), -1)

# # 转换点的格式
# pts1 = np.float32(markpoint)
# pts2 = np.float32(dstpoint)

# # 生成透视矩阵
# M = cv2.getPerspectiveTransform(pts1, pts2)

# b,g,r = cv2.split(img)
# img = cv2.merge([r,g,b])   
# img2 = cv2.merge([r,g,b]) 
# print(img)
# # 转换
# dst = cv2.warpPerspective(img2, M, (250, 450))
# plt.subplot(121), plt.imshow(img), plt.title('Input')
# plt.subplot(122), plt.imshow(dst), plt.title('Output')
# plt.show()