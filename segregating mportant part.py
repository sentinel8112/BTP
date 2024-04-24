import numpy as np

import cv2

# cX = []
# cY = []

b = [0,0,0,0]

while True:
    frame = cv2.imread('picr2.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = 21
    l_s = 141
    l_v = 76
    u_h = 80
    u_s = 255
    u_v = 245

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    l_b = np.array([33,80,0])
    u_b = np.array([135,255,255])

    mask = cv2.inRange(hsv, l_b, u_b)
    # cv2.imshow('mask1', mask)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(res, contours, 51, (0, 0, 255), 3)
    # print("Number of contours = " + str(len(contours)))
    cv2.imshow('res1', res)

    # # Select ROI
    # r = cv2.selectROI(mask)
    # # Crop image
    # imCrop = frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    # cv2.imshow('roi', imCrop)

    if len(contours)>0:
        area = max(contours, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(area)
        cv2.rectangle(frame,(xg,yg),(xg+wg, yg+hg),(0,0,255),2)
        roi = frame[yg:yg+hg, xg:xg+wg]
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # mask = np.zeros_like(frame1)
    # cv2.rectangle(mask, (xg,yg),(xg+wg, yg+hg), (255,255,255), -1)
    # cv2.circle(frame1, (xg, yg), 5, (0, 255, 0), -1)
    # cv2.circle(frame1, (xg+wg, yg+hg), 5, (255, 255, 0), -1)
    # masked_image = cv2.bitwise_and(frame1, mask)

    count = wg/4

    l_h = 64
    l_s = 0
    l_v = 0
    u_h = 255
    u_s = 255
    u_v = 255

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # l_b = np.array([90,165,70])
    # u_b = np.array([255,255,255])


    mask = cv2.inRange(hsv, l_b, u_b)
    # cv2.imshow('mask2', mask)
    res1 = cv2.bitwise_and(roi, roi, mask=mask)
    cv2.imshow('res2', res1)

    
    imgray = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 10, 255, 0)
    kernal = np.ones((2,2), np.uint8)
    erosion = cv2.erode(thresh, kernal, iterations=1)
    cv2.imshow('thresh', thresh)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(roi, contours, 51, (0, 0, 255), 3)
    a=0
    for c in contours:
        M = cv2.moments(c)
        if M["m00"] == 0:
            continue
        else:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(roi, (cX, cY), 5, (255, 255, 255), -1)  
            if cY > (hg/5) and cY < (4*hg/5):
              if  cX< count:
               b[3] = 1
              if cX> count and cX< 2*count:
               b[2] = 1 
              if cX>2*count and cX< 3*count:
               b[1] = 1 
              if cX> 3*count and cX< 4*count:
               b[0] = 1 
    cv2.imshow("res", frame)
    cv2.imshow('res_roi',roi)

    key = cv2.waitKey(10)
    if key == 27:
        break

# for i in range(0,a):
#     print(cX[i], ' , ', cY[i])
a = b[0] + 2*b[1] + 4*b[2] + 8*b[3]
print(a)

cv2.destroyAllWindows()