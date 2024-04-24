# import cv2 as cv 

# def testDevice(source):
#    cap = cv.VideoCapture(source) 
#    if cap is None or not cap.isOpened():
#        print('Warning: unable to open video source: ', source)

# testDevice(0) # no printout
# testDevice(1) # prints message
# testDevice(2)

import numpy as np
import cv2

video_capture_0 = cv2.VideoCapture(0)
video_capture_1 = cv2.VideoCapture(1)

while True:
    ret0, frame0 = video_capture_0.read()
    ret1, frame1 = video_capture_1.read()

    if (ret0):
        cv2.imshow('Cam 0', frame0)

    if (ret1):
        cv2.imshow('Cam 1', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture_0.release()
video_capture_1.release()
cv2.destroyAllWindows()