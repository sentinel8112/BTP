import tkinter as tk
from tkinter import Button, Label
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import cv2
import numpy as np
from PIL import Image,ImageTk

minima = []
# Function to update the graph
def update_graph():
    #Data to plot
    x = gray[240]
    minimum = min(x)
    for i in range(len(x)):
       if x[i] == minimum:
          print(i)
          min_pos=i
          minima.append(i)

    # Clear the previous plot
    ax.clear()

    # Plot the new data
    ax.plot(minima)
    ax.set_title("Live Graph")

    # Update the graph
    canvas.draw()
    root.after(10, update_graph)
    return minima,minimum

# Function to update the live image
def update_image():
    # Capture a frame from the camera
    global ret,frame
    global gray
    ret, frame = cap.read()

    if ret:
        # Convert the frame to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # print(frame.shape[1] )
        # print(frame.shape[0] )

        # Resize the frame to fit the display
        frame = cv2.resize(frame, (400, 300))

        # Convert the frame to a Tkinter image
        # img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        img = frame
        img = Image.fromarray(img)
        img_tk = ImageTk.PhotoImage(image=img)

        # Update the label with the new image
        image_label.imgtk = img_tk
        image_label.config(image=img_tk)

    # Schedule the next update
    root.after(10, update_image)

# Create the main window
root = tk.Tk()
root.title("SPR Imager")

# Create a frame for the graph
graph_frame = ttk.Frame(root)
graph_frame.grid(row = 0, column = 1)
#graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a Matplotlib figure
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
ax.set_title("Live Graph")

# Add the figure to the Tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().grid(row = 0, column = 1)
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create buttons
button_frame = ttk.Frame(root)
button_frame.grid(row=2,column=1)
# button_frame.pack(side=tk.BOTTOM, pady=10)

btn_update_graph = Button(button_frame, text="Update Graph", command=update_graph)
btn_update_graph.pack(side=tk.LEFT, padx=10)


# btn_start_camera = Button(button_frame, text="Start Camera", command=lambda: cap.release())
# btn_start_camera.pack(side=tk.LEFT, padx=10)

btn_calibrate = Button(button_frame, text="Calibrate")
btn_calibrate.pack(side=tk.LEFT, padx=10)

btn_exit = Button(button_frame, text="Exit", command=root.destroy)
btn_exit.pack(side=tk.LEFT, padx=10)

# Create a label for the live image
image_label = Label(root)
image_label.grid(row=1,column=1)
# image_label.pack()

# #creating a frame
# frame1 = tk.LabelFrame(root, text = "Results",padx= 50,pady=50)
# frame1.grid(row = 1, column = 2)
# myLabel = Label(frame1, text = "Minima:")
# myLabel.pack()
# myLabel = Label(frame1, text = pos)
# myLabel.pack()
# fwhm = Label(frame1,text = "FWHM:" )
# fwhm.pack()
# ri = Label(frame1,text="Refractive Index:")
# ri.pack()

# Open the camera
cap = cv2.VideoCapture(0)

# Start updating the live image
update_image()
minima,pos = update_graph()

#creating a frame
frame1 = tk.LabelFrame(root, text = "Results",padx= 50,pady=50)
frame1.grid(row = 1, column = 2)
myLabel = Label(frame1, text = "Minima:")
myLabel.pack()
myLabel = Label(frame1, text = pos)

myLabel.pack()
fwhm = Label(frame1,text = "FWHM:" )
fwhm.pack()
ri = Label(frame1,text="Refractive Index:")
ri.pack()


# Run the Tkinter event loop
root.mainloop()

# Release the camera
cap.release()
