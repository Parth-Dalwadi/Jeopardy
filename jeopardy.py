import json
from tkinter import *
import random
from decimal import *
from PIL import Image

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.attributes('-fullscreen', True)
root.title("Jeopardy")
root.configure(background="black")
title = Label(root, text="Jeopardy", width=width, foreground="white", background="#e4000f", font=("Helvetica", 24, "bold"))
title.pack(side="top")

class Jeopardy:
    def __init__(self):
        self.buttons()
        self.is_fullscreen = True

    def buttons(self):
        quit_button = Button(root, text="Quit", command=root.destroy, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        quit_button.pack(side="bottom", anchor="se")
        toggle_window_button = Button(root, text="Toggle Window", command=self.is_fullscreen_command, width=12, bg="darkgreen", fg="white", font=("Helvetica", 16, "bold"))
        toggle_window_button.pack(side="bottom", anchor="se")
        stop_music_button = Button(root, text="Stop Music", command=self.is_fullscreen_command, width=12, bg="purple", fg="white", font=("Helvetica", 16, "bold"))
        stop_music_button.pack(side="bottom", anchor="se")
        play_music_button = Button(root, text="Play Music", command=self.is_fullscreen_command, width=12, bg="gray", fg="white", font=("Helvetica", 16, "bold"))
        play_music_button.pack(side="bottom", anchor="se")


    def is_fullscreen_command(self):
        self.is_fullscreen = not self.is_fullscreen
        root.attributes(-fullscreen, self.is_fullscreen)




jeopardy = Jeopardy()
root.mainloop()
