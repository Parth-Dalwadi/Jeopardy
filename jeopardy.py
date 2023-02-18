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
root.title("Pokemon Jeopardy")
root.configure(background="black")
title = Label(root, text="Pokemon Jeopardy", width=width, foreground="white", background="#e4000f", font=("Helvetica", 24, "bold"))
title.pack(side="top")

class Jeopardy:
    def __init__(self):
        self.buttons()
        self.is_fullscreen = True
        self.questions = []
        self.answers = []
        self.choices = []
        self.result_label = Label()
        self.scores = []

    def buttons(self):
        quit_button = Button(root, text="Quit", command=root.destroy, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        quit_button.pack(side="bottom", anchor="se")
        toggle_window_button = Button(root, text="Toggle Window", command=self.is_fullscreen_command, width=12, bg="darkgreen", fg="white", font=("Helvetica", 16, "bold"))
        toggle_window_button.pack(side="bottom", anchor="se")
        stop_music_button = Button(root, text="Stop Music", command=self.is_fullscreen_command, width=12, bg="purple", fg="white", font=("Helvetica", 16, "bold"))
        stop_music_button.pack(side="bottom", anchor="se")
        play_music_button = Button(root, text="Play Music", command=self.is_fullscreen_command, width=12, bg="gray", fg="white", font=("Helvetica", 16, "bold"))
        play_music_button.pack(side="bottom", anchor="se")

        start_button = Button(root, text="Start", command=lambda:[self.amount_of_players(), start_button.destroy()], width=12, bg="#e4000f", fg="white", font=("Helvetica", 16, "bold"))
        start_button.place(relx=0.5, rely=0.5, anchor="center")

    def is_fullscreen_command(self):
        self.is_fullscreen = not self.is_fullscreen
        root.attributes('-fullscreen', self.is_fullscreen)

    def amount_of_players(self):
        self.player_amount_label = Label(root, text="How many players?", width=60, bg="black", fg="white", font=("Helvetica", 32, "bold"))
        self.one_player_button = Button(root, text="One", command=self.destroy_player_select, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        self.two_player_button = Button(root, text="Two", command=self.destroy_player_select, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        self.three_player_button = Button(root, text="Three", command=self.destroy_player_select, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        self.four_player_button = Button(root, text="Four", command=self.destroy_player_select, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))

        self.player_amount_label.place(relx=0.5, rely=0.2, anchor="center")
        self.one_player_button.place(relx=0.2, rely=0.5, anchor="center")
        self.two_player_button.place(relx=0.4, rely=0.5, anchor="center")
        self.three_player_button.place(relx=0.6, rely=0.5, anchor="center")
        self.four_player_button.place(relx=0.8, rely=0.5, anchor="center")
        
        def destroy_player_select(self):
           self.player_amount_label.destroy()
           self.one_player_button.destroy()
           self.two_player_button.destroy()
           selfthree_player_button.destroy()
           self.four_player_button.destroy()

    def destroy_player_select(self):
        self.player_amount_label.destroy()
        self.one_player_button.destroy()
        self.two_player_button.destroy()
        self.three_player_button.destroy()
        self.four_player_button.destroy()

#    def one_player(self):
        

  #  def two_player(self):

 #   def three_player(self):

#    def four_player(self):





jeopardy = Jeopardy()
root.mainloop()
