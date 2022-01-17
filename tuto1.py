""" OpenCV读取图片，视频"""

import cv2

# image
""" 
# img = cv2.imread("C:/Users/cugbl/Desktop/girl.jpg")
img = cv2.imread("res/colorcolor.jpg")
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
cv2.imshow('dog',img)
cv2.waitKey(0) 
 """

# # Video

# 读取视频信息
# video = cv2.VideoCapture("res/Guide Dogs.mp4")
# 读取相机镜头
video = cv2.VideoCapture(0)
while True:
    next, frame = video.read()
    if next:
        frame = cv2.resize(frame,(0,0),fx = 1, fy = 1)
        cv2.imshow('img', frame)
    else:
        break
    ## 键盘按下q才会终止
    if cv2.waitKey(20) == ord('q'):
        break