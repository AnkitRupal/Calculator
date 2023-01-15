from tkinter import *
from window import window
from capture import capture

Capture = capture()
mainFrame = window(Capture)
mainFrame.root.mainloop()