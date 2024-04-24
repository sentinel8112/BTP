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
cam = cv2.VideoCapture(0)
if not cam.isOpened():
   print("Cannot open camera")
   exit()

#plt.ion()

min_pos = 0
rep =[]

while True:
   
   #clearing the previous plot
    plt.cla()

   # Capture frame-by-frame
    ret, frame = cam.read()
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
    #print(gray.shape)

    
    list = gray[240]  
    minima = min(list)
    for i in range(len(list)):
       if list[i]==minima:
          print(i)
          min_pos=i
          rep.append(i)
    #print(minima)

    
    #print(list[320])
    #print(len(list))
    plt.plot(rep)
    #plt.show()
    plt.pause(0.1)

    #time.sleep(0.5)
    # plt.close()

    
    if cv2.waitKey(1) == ord('q'):
        break
    
plt.show()
    
# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()