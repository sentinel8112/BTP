import cv2
import matplotlib.pyplot as plt

def grab_frame(cap):
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)



#Initiate the two cameras
cap1 = cv2.VideoCapture(0)
gray = cv2.cvtColor(cap1, cv2.COLOR_BGR2GRAY)
#cap2 = cv2.VideoCapture(1)

#create two subplots
ax1 = plt.plot(gray[200])
#ax2 = plt.subplot(1,2,2)

#create two image plots
im1 = ax1.show(grab_frame(cap1))
# im2 = ax2.imshow(grab_frame(cap2))

plt.ion()



while True:
    im1.set_data(grab_frame(cap1))
    # im2.set_data(grab_frame(cap2))
    plt.pause(0.2)

plt.ioff() # due to infinite loop, this gets never called.
plt.show()