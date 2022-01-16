import cv2

# image
""" 
img = cv2.imread("C:/Users/wsm/Desktop/xRZ2dGS.jpg")
img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
cv2.imshow('Scenery',img)
cv2.waitKey(0) 
"""

# Video

# video = cv2.VideoCapture("E:/Coding/Python/OpenCV/Guide Dogs.mp4")
video = cv2.VideoCapture(0)
while True:
    next, frame = video.read()
    if next:
        frame = cv2.resize(frame,(0,0),fx = 1, fy = 1)
        cv2.imshow('img', frame)
    else:
        break

    if cv2.waitKey(20) == ord('q'):
        break