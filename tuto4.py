""" 画形状和写字 """
import cv2
import numpy as np

img = np.zeros((600,600,3), np.uint8)

# 画直线
cv2.line(img, (0,0),(img.shape[1],img.shape[0]),(0,255,0), 2)

# 画矩形
# cv2.rectangle(img,(10,10), (400,300),(32,56,118),2)
cv2.rectangle(img,(10,10), (400,300),(32,56,118),cv2.FILLED)

# 画圆
cv2.circle(img, (300, 400), 60, (60, 34, 543), cv2.FILLED)

# 写文字（不支持中文）
cv2.putText(img, "OpenCV", (300,500),cv2.FONT_HERSHEY_DUPLEX, 2, (54,76,12), 3)

cv2.imshow("img", img)
cv2.waitKey(0)