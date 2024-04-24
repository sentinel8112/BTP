from tkinter import *

root = Tk()
root.title("SPR Imager")

def Calibrate():
    lab1 = Label(root, text="Calibrated")
    lab1.pack()

#creating a label widget
myLabel = Label(root, text = "SPR Imager",padx = 50,pady=30)                  #.grid(row = 0,column = 2)

#creating a frame
frame1 = LabelFrame(root, text = "Controls", padx = 10, pady=20)
frame1.pack(padx = 50, pady = 50)

#creating buttons
calibrate = Button(root,text = "Calibrate",padx = 50,pady=30, command=Calibrate)

button_quit = Button(frame1, text = "Exit Program", command = root.quit)


#display on screen
#myLabel.grid(row = 0,column = 2)
#calibrate.grid(row = 1,column=1)
myLabel.pack()
calibrate.pack()
button_quit.pack()

root.mainloop()