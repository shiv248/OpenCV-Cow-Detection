"""
This code will open up a saved video on a tkinter window. The user can click on the video and a box will appear around that point,
symbolizing a new cow detected.
"""

import tkinter as tk
from tkvideo import tkvideo

# Create a window
window = tk.Tk()
window.title("Video Feed")

# Create heading
heading = tk.Label(window, text = "Live Video Feed")
heading.pack()

# Displays all buttons vertically (need them horizontal)
for i in range (20):
    but = tk.Button(window, text = 'a')
    but.pack()

# Create a label. This will act as a placeholder for where we play the video.
placeholder = tk.Label(window)
placeholder.pack()

# Play the video (this is the path of the video from my laptop. If you want to test it on your laptop:
    # right-click "sampleVid.mov"
    # select "Copy Path"
    # replace the path I have with the one you just copied)
# For demonstration purposes, we can just use the path of whoever is presenting.
video = tkvideo("/Users/aditikisara/Documents/GitHub/OpenCV-Cow-Detection/feeds/feed1.mp4", placeholder, loop = 1, size = (1280,720))
video.play()

window.mainloop()