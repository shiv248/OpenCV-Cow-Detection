"""  ##################################################
#Draw rectangle on camera feed (rectangle disappears when user clicks something else)

import numpy as np
import cv2 

drawing = False
point = (0,0)

def mouse_drawing(event, x, y, flags, params):
    global point, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        point= (x, y)

cap = cv2.VideoCapture(0)
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)

while True:
    _, frame = cap.read()
    if drawing :
        cv2.rectangle(frame,point,(point[0]+80, point[1]+80),(0,0,255),0)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(25)
    
    if key == 13:    
        print('done')
    elif key == 27:
        break

#cap.release()#Draw rectangle on camera feed (rectangle disappears when user clicks something else)
cv2.destroyAllWindows() """

##############################################################
#Draw multiple rectangles on an image
import tkinter as tk # this is in python 3.4. For python 2.x import Tkinter
from PIL import Image, ImageTk
import cv2

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0

        # Create a label with the heading
        self.heading = tk.Label(self, text = "Live Video Feed")
        self.heading.pack()

        # Create shape of cursor
        self.canvas = tk.Canvas(self, width=512, height=512, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)

        # Draw shape based on mouse click
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.rect = None
        self.start_x = None
        self.start_y = None

        self._draw_image()

    def _draw_image(self):
        # Open image
        self.im = Image.open('/Users/aditikisara/Documents/GitHub/OpenCV-Cow-Detection/dice.jpeg')

        #self.cap = cv2.VideoCapture(0)


        self.tk_im = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0,0,anchor="nw",image=self.tk_im)

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1)

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        pass


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()