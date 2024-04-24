import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
import time 

def roll_avg(list, window):
  ln = len(list)
  window = int(window/2)
  sum = np.zeros(ln)
  for i in range(window,ln - window):
    for j in range (0,window):
      sum[i] = list[i+j] + list[i-j] 
    sum[i] = (sum[i]+list[i])/((window-1)*2 +1)
  return sum

#cam input
# cam = cv2.VideoCapture(0)
# if not cam.isOpened():
#    print("Cannot open camera")
#    exit()

# #plt.ion()

# while True:
#     #plt.close()
#    # Capture frame-by-frame
#     ret, frame = cam.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     #print(frame)
#     # Display the resulting frame
#     cv2.imshow('frame',frame)

#     print(frame)

#     # list = gray[10]
#     # print(len(list))
#     # plt.plot(list)
#     # plt.show()

#     time.sleep(3)

    
#     if cv2.waitKey(1) == ord('q'):
#         break
    
# # When everything done, release the capture
# cam.release()
# cv2.destroyAllWindows()

frame = cv2.imread("line_thick.jpg",0)
#bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# print(frame)

wid = frame.shape[1] 
hgt = frame.shape[0]
list = frame[1000]
#print(list)
print(len(list))

min = 255
pos =[]
for i in range (350,len(list)):
    if list[i] <= min:
        min = list[i]
for i in range (350,len(list)):
  if list[i] == min:
    pos.append(i)
print(min)
print(pos)


# plt.plot(list[400:600])
plt.plot(list)
plt.title('intensityPlot')
plt.show()

# print(wid)
# print(hgt)
# print(len(frame[1000]))

# deriv = np.zeros(len(list))
# for i in range (400,600):
#    deriv[i] = (list[i+1]-list[i-1])/2
# plt.plot(deriv[400:600])
# plt.show()

smooth = roll_avg(list,10)
plt.plot(smooth)
plt.title('rollingAvgPlot')
plt.show()

deriv = np.zeros(len(smooth))
for i in range (400,600):
   deriv[i] = (smooth[i+1]-smooth[i-1])/2
# plt.plot(deriv[400:600])
plt.plot(deriv)
plt.title('derivativePlot')
plt.show()


# list[list > 57] = 255 # thresholding value was decided by the mask code with the trakerbars


while True:
    cv2.imshow("img", frame)
    key = cv2.waitKey(10)
    if key == 27:
        break


cv2.destroyAllWindows()