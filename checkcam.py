import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import cv2
import matplotlib.pyplot as plt

fig = plt.figure()
cap = cv2.VideoCapture(0)


x1 = np.linspace(0.0, 640)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)


line1, = plt.plot(y1, 'ko-')        # so that we can update data later

for i in range(1000):

    # display camera feed

    ret,frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(frame)
    # Display the resulting frame
    cv2.imshow('frame',gray)

    #print(gray)
    print(gray.shape)

    #list = gray[240]

    # update data
    line1.set_ydata(gray[240])

    # redraw the canvas
    fig.canvas.draw()

    # convert canvas to image
    img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
            sep='')
    img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # img is rgb, convert to opencv's default bgr
    #img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)


    # display image with opencv or any operation you like
    cv2.imshow("plot",img)

    # display camera feed
    # ret,frame = cap.read()
    # cv2.imshow("cam",frame)

    k = cv2.waitKey(10) #& 0xFF
    if k == 27:
        break