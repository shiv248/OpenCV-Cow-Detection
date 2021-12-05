"""
This code will open up a saved video on a tkinter window. The user can click on a button, signalling that a nozzle should be turned on.
"""

import tkinter as tk
from tkvideo import tkvideo

# This function will handle the button colors and the prompts (nozzle open/closed)
def onclick(btnNum, btn):
    # Check the color of the button. If it's white, then turn it green. Else, turn it back to white.
    if (btn["highlightbackground"] == "white"):
        btn.config(highlightbackground = "green")

        # Check for the button value. If it's on top, then it's less than 25.
        # Prompt1 refers to the top buttons' prompt.
        # Prompt2 refers to the bottom buttons' prompt.
        if (int(btnNum) < 5):
            prompt1.configure(text = "Section " + btnNum + " is open.")
        else:
            prompt2.configure(text = "Section " + btnNum + " is open.")
    else:
        btn.config(highlightbackground = "white")
        if (int(btnNum) < 5):
            prompt1.configure(text = "Section " + btnNum + " is closed.")
        else:
            prompt2.configure(text = "Section " + btnNum + " is closed.")

    

# Create a window
window = tk.Tk()
window.title("Video Feed")

space = tk.Label(window)
space.pack()

# Create heading
heading = tk.Label(window, text = "Live Video Feed\n", font = "sans 16")
heading.pack()

# Top section for buttons
frame1 = tk.Frame(window)
frame1.pack()

# Prompt tells if nozzle is open or not
prompt1 = tk.Label(frame1, text = " ")
prompt1.pack()

space1 = tk.Label(frame1)
space1.pack()

# Displays all TOP ROW buttons
btn1 = tk.Button(frame1, text = "                   1                 ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("1", btn1))
btn1.pack(side = tk.LEFT, padx = "45px")

btn2 = tk.Button(frame1, text = "                   2                   ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("2", btn2))
btn2.pack(side = tk.LEFT, padx = "45px")

btn3 = tk.Button(frame1, text = "                   3                   ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("3", btn3))
btn3.pack(side = tk.LEFT, padx = "45px")

btn4 = tk.Button(frame1, text = "                   4                   ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("4", btn4))
btn4.pack(side = tk.LEFT, padx = "45px")

space2 = tk.Label(frame1)
space2.pack()

# Create a label. This will act as a placeholder for where we play the video.
placeholder = tk.Label(window)
placeholder.pack()

# Play the video (this is the path of the video from my laptop. If you want to test it on your laptop:
    # right-click "sampleVid.mov"
    # select "Copy Path"
    # replace the path I have with the one you just copied)
# For demonstration purposes, we can just use the path of whoever is presenting.
video = tkvideo("/Users/aditikisara/Documents/GitHub/OpenCV-Cow-Detection/feeds/feed1.mp4", placeholder, loop = 1, size = (889,500))
video.play()

space3 = tk.Label(window)
space3.pack()

# Bottom section for buttons
frame2 = tk.Frame(window)
frame2.pack()

# Prompt tells if nozzle is open or not
prompt2 = tk.Label(frame2, text = " ")
prompt2.pack()

space4 = tk.Label(frame2)
space4.pack()

# Displays BOTTOM ROW buttons
btn5 = tk.Button(frame2, text = "                     5                     ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("5", btn5))
btn5.pack(side = tk.LEFT, padx = "45px")

btn6 = tk.Button(frame2, text = "                     6                     ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("6", btn6))
btn6.pack(side = tk.LEFT, padx = "45px")

btn7 = tk.Button(frame2, text = "                     7                     ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("7", btn7))
btn7.pack(side = tk.LEFT, padx = "45px")

btn8 = tk.Button(frame2, text = "                     8                     ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("8", btn8))
btn8.pack(side = tk.LEFT, padx = "45px")

space5 = tk.Label(frame2, text = " ")
space5.pack()

window.mainloop()