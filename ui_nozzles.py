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
        if (int(btnNum) < 25):
            prompt1.configure(text = "Nozzle " + btnNum + " is open.")
        else:
            prompt2.configure(text = "Nozzle " + btnNum + " is open.")
    else:
        btn.config(highlightbackground = "white")
        if (int(btnNum) < 25):
            prompt1.configure(text = "Nozzle " + btnNum + " is closed.")
        else:
            prompt2.configure(text = "Nozzle " + btnNum + " is closed.")

    

# Create a window
window = tk.Tk()
window.title("Video Feed")

# Create heading
heading = tk.Label(window, text = "Live Video Feed\n", font = "sans 16")
heading.pack()

# Top section for buttons
frame1 = tk.Frame(window)
frame1.pack()

# Prompt tells if nozzle is open or not
prompt1 = tk.Label(frame1, text = " ")
prompt1.grid(row = 0, column = 12, columnspan = 5)

# Displays all TOP ROW buttons
btn1 = tk.Button(frame1, text = "  1  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("1", btn1))
btn1.grid(row = 1, column = 1)

btn2 = tk.Button(frame1, text = "  2  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("2", btn2))
btn2.grid(row = 1, column = 2)

btn3 = tk.Button(frame1, text = "  3  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("3", btn3))
btn3.grid(row = 1, column = 3)

btn4 = tk.Button(frame1, text = "  4  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("4", btn4))
btn4.grid(row = 1, column = 4)

btn5 = tk.Button(frame1, text = "  5  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("5", btn5))
btn5.grid(row = 1, column = 5)

btn6 = tk.Button(frame1, text = "  6  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("6", btn6))
btn6.grid(row = 1, column = 6)

btn7 = tk.Button(frame1, text = "  7  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("7", btn7))
btn7.grid(row = 1, column = 7)

btn8 = tk.Button(frame1, text = "  8  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("8", btn8))
btn8.grid(row = 1, column = 8)

btn9 = tk.Button(frame1, text = "  9  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("9", btn9))
btn9.grid(row = 1, column = 9)

btn10 = tk.Button(frame1, text = "  10  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("10", btn10))
btn10.grid(row = 1, column = 10)

btn11 = tk.Button(frame1, text = "  11  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("11", btn11))
btn11.grid(row = 1, column = 11)

btn12 = tk.Button(frame1, text = "  12  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("12", btn12))
btn12.grid(row = 1, column = 12)

btn13 = tk.Button(frame1, text = "  13  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("13", btn13))
btn13.grid(row = 1, column = 13)

btn14 = tk.Button(frame1, text = "  14  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("14", btn14))
btn14.grid(row = 1, column = 14)

btn15 = tk.Button(frame1, text = "  15  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("15", btn15))
btn15.grid(row = 1, column = 15)

btn16 = tk.Button(frame1, text = "  16  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("16", btn16))
btn16.grid(row = 1, column = 16)

btn17 = tk.Button(frame1, text = "  17  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("17", btn17))
btn17.grid(row = 1, column = 17)

btn18 = tk.Button(frame1, text = "  18  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("18", btn18))
btn18.grid(row = 1, column = 18)

btn19 = tk.Button(frame1, text = "  19  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("19", btn19))
btn19.grid(row = 1, column = 19)

btn20 = tk.Button(frame1, text = "  20  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("20", btn20))
btn20.grid(row = 1, column = 20)

btn21 = tk.Button(frame1, text = "  21  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("21", btn21))
btn21.grid(row = 1, column = 21)

btn22 = tk.Button(frame1, text = "  22  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("22", btn22))
btn22.grid(row = 1, column = 22)

btn23 = tk.Button(frame1, text = "  23  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("23", btn23))
btn23.grid(row = 1, column = 23)

btn24 = tk.Button(frame1, text = "  24  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("24", btn24))
btn24.grid(row = 1, column = 24)

btn25 = tk.Button(frame1, text = "  25  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("25", btn25))
btn25.grid(row = 1, column = 25)

space1 = tk.Label(window)
space1.pack()

# Create a label. This will act as a placeholder for where we play the video.
placeholder = tk.Label(window)
placeholder.pack()

# Play the video (this is the path of the video from my laptop. If you want to test it on your laptop:
    # right-click "sampleVid.mov"
    # select "Copy Path"
    # replace the path I have with the one you just copied)
# For demonstration purposes, we can just use the path of whoever is presenting.
video = tkvideo("/Users/aditikisara/Documents/GitHub/OpenCV-Cow-Detection/feeds/feed - 2.mp4", placeholder, loop = 1, size = (889,500))
video.play()

space2 = tk.Label(window)
space2.pack()

# Bottom section for buttons
frame2 = tk.Frame(window)
frame2.pack()

# Prompt tells if nozzle is open or not
prompt2 = tk.Label(frame2, text = " ")
prompt2.grid(row = 0, column = 12, columnspan = 5)

# Displays BOTTOM ROW buttons
btn26 = tk.Button(frame2, text = "  26  ", fg = "black", highlightthickness = "1px", highlightbackground = "white" ,command = lambda: onclick("26", btn26))
btn26.grid(row = 1, column = 1)

btn27 = tk.Button(frame2, text = "  27  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("27", btn27))
btn27.grid(row = 1, column = 2)

btn28 = tk.Button(frame2, text = "  28  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("28", btn28))
btn28.grid(row = 1, column = 3)

btn29 = tk.Button(frame2, text = "  29  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("29", btn29))
btn29.grid(row = 1, column = 4)

btn30 = tk.Button(frame2, text = "  30  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("30", btn30))
btn30.grid(row = 1, column = 5)

btn31 = tk.Button(frame2, text = "  31  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("31", btn31))
btn31.grid(row = 1, column = 6)

btn32 = tk.Button(frame2, text = "  32  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("32", btn32))
btn32.grid(row = 1, column = 7)

btn33 = tk.Button(frame2, text = "  33  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("33", btn33))
btn33.grid(row = 1, column = 8)

btn34 = tk.Button(frame2, text = "  34  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("34", btn34))
btn34.grid(row = 1, column = 9)

btn35 = tk.Button(frame2, text = "  35  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("35", btn35))
btn35.grid(row = 1, column = 10)

btn36 = tk.Button(frame2, text = "  36  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("36", btn36))
btn36.grid(row = 1, column = 11)

btn37 = tk.Button(frame2, text = "  37  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("37", btn37))
btn37.grid(row = 1, column = 12)

btn38 = tk.Button(frame2, text = "  38  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("38", btn38))
btn38.grid(row = 1, column = 13)

btn39 = tk.Button(frame2, text = "  39  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("39", btn39))
btn39.grid(row = 1, column = 14)

btn40 = tk.Button(frame2, text = "  40  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("40", btn40))
btn40.grid(row = 1, column = 15)

btn41 = tk.Button(frame2, text = "  41  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("41", btn41))
btn41.grid(row = 1, column = 16)

btn42 = tk.Button(frame2, text = "  42  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("42", btn42))
btn42.grid(row = 1, column = 17)

btn43 = tk.Button(frame2, text = "  43  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("43", btn43))
btn43.grid(row = 1, column = 18)

btn44 = tk.Button(frame2, text = "  44  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("44", btn44))
btn44.grid(row = 1, column = 19)

btn45 = tk.Button(frame2, text = "  45  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("45", btn45))
btn45.grid(row = 1, column = 20)

btn46 = tk.Button(frame2, text = "  46  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("46", btn46))
btn46.grid(row = 1, column = 21)

btn47 = tk.Button(frame2, text = "  47  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("47", btn47))
btn47.grid(row = 1, column = 22)

btn48 = tk.Button(frame2, text = "  48  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("48", btn48))
btn48.grid(row = 1, column = 23)

btn49 = tk.Button(frame2, text = "  49  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("49", btn49))
btn49.grid(row = 1, column = 24)

btn50 = tk.Button(frame2, text = "  50  ", fg = "black", highlightthickness = "1px", highlightbackground = "white", command = lambda: onclick("50", btn50))
btn50.grid(row = 1, column = 25)


window.mainloop()