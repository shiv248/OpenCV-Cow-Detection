import tkinter as tk
from tkinter import *
from tkvideo import tkvideo

window = tk.Tk()
window.title("Video Feed")

# Create heading
heading = tk.Label(window, text = "Live Video Feed")
heading.grid(row = 0, column = 0, columnspan = 2, pady = 10)

# Sidebar Decoration
dec = tk.Label(window, bg = "pink", width = 10, height = 45)
dec.grid(row = 0, rowspan = 4, column = 3, columnspan = 2)

# Insert video into grid
"""player = tkvideo("/Users/aditikisara/Documents/GitHub/sampleVid.mov", window, loop = True)
player.grid(row = 1, column = 0, sticky = "NSEW", padx = 2, pady = 2)"""

# Slots for the video feeds (currently labels, but will switch to different widget to be more interactive)
video1 = tk.Label(window, text = "Feed #1", borderwidth = 3, relief = "ridge", height = 10, width = 20)
video1.grid(row = 1, column = 0, sticky = "NSEW", padx = 2, pady = 2)

video2 = tk.Label(window, text = "Feed #2", borderwidth = 3, relief = "ridge", height = 10, width = 20)
video2.grid(row = 1, column = 1, sticky = "NSEW", padx = 2, pady = 2)

video3 = tk.Label(window, text = "Feed #3", borderwidth = 3, relief = "ridge", height = 10, width = 20)
video3.grid(row = 2, column = 0, sticky = "NSEW", padx = 2, pady = 2)

video4 = tk.Label(window, text = "Feed #4", borderwidth = 3, relief = "ridge", height = 10, width = 20)
video4.grid(row = 2, column = 1, sticky = "NSEW", padx = 2, pady = 2)

video5 = tk.Label(window, text = "Feed #5", borderwidth = 3, relief = "ridge", height = 10, width = 20)
video5.grid(row = 3, column = 0, sticky = "NSEW", padx = 2, pady = 2)

video6 = tk.Label(window, text = "Feed #6", borderwidth = 3, relief = "ridge", height = 10, width = 20)
video6.grid(row = 3, column = 1, sticky = "NSEW", padx = 2, pady = 2)

# Create a scrollbar
"""sb = Scrollbar(window).grid(
    column = 3,
    rowspan = 3,
    sticky = "NS")
sb.config( command = heading.yview )"""

window.mainloop()