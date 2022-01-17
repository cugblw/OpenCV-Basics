""" numpy与图片的关系 """

from random import randint
import cv2
from matplotlib import image
import  numpy as np

img = cv2.imread("res/colorcolor.jpg")

print(type(img))
print(img.shape)

""" 
图像存储顺序
红 绿 蓝
R  G  B
OpenCV顺序
B  G  R 
"""

""" # 自定义一张图

img_self = np.empty((300, 300, 3), np.uint8)

for row in range(300):
    for col in range( ):
        # OpenCV顺序(B G R)
        # img_self[row][col] = [255,randint(0,255),randint(0,255)]
        img_self[row][col] = [15,160,255]

cv2.imshow("img_self", img_self)
cv2.waitKey(0) """


# 图片裁剪

new_img = img[:150,:200]

cv2.imshow("img", img)
cv2.imshow("new_img", new_img)
cv2.waitKey(0)