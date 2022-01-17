"""常用函数"""

import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('res/colorcolor.jpg')

img= cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

# RGB 转成灰度值图片
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 高斯模糊, kernel, 标准差
# blur = cv2.GaussianBlur(img,(3,3),5)
blur = cv2.GaussianBlur(img,(9,9),5)

# 边缘检测
canny = cv2.Canny(img, 250, 300)

# 图片膨胀(边界变粗)
dilate = cv2.dilate(canny, kernel, iterations=1)

# 图片侵蚀(边界变细)
erode = cv2.erode(dilate, kernel, iterations=1)

# cv2.imshow("img", img)
# cv2.imshow("gray", gray)
# cv2.imshow("blur", blur)
cv2.imshow("canny", canny)
cv2.imshow("dilate", dilate)
cv2.imshow("errode", erode)
cv2.waitKey(0)
