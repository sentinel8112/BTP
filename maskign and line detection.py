import cv2
import numpy as np

def nothing(x):
    pass

# cap = cv2.VideoCapture('Video2.mp4');
cv2.namedWindow('TB')
cv2.createTrackbar('l_h', 'TB', 0, 255, nothing)
cv2.createTrackbar('l_s', 'TB', 0, 255, nothing)
cv2.createTrackbar('l_v', 'TB', 0, 255, nothing)
cv2.createTrackbar('u_h', 'TB', 255, 255, nothing)
cv2.createTrackbar('u_s', 'TB', 255, 255, nothing)
cv2.createTrackbar('u_v', 'TB', 255, 255, nothing)

while True:
    frame = cv2.imread('test123.jpg')
    # _, frame = cap.read()
    # print(cap.get(3))
    # print(cap.get(4))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('l_h', 'TB')
    l_s = cv2.getTrackbarPos('l_s', 'TB')
    l_v = cv2.getTrackbarPos('l_v', 'TB')

    u_h = cv2.getTrackbarPos('u_h', 'TB')
    u_s = cv2.getTrackbarPos('u_s', 'TB')
    u_v = cv2.getTrackbarPos('u_v', 'TB')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(10)
    if key == 27:
        break

# cap.release()
cv2.destroyAllWindows()