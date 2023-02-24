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

with open('jeopardyQA.json') as qa_file:
    qa = json.load(qa_file)

topics = qa['topics']
questions = qa['questions']
answers = qa['answers']
zip_qa = zip(topics, questions, answers)
list_qa = list(zip_qa)
random.shuffle(list_qa)
topics, questions, answers = zip(*list_qa)

class Jeopardy:
    def __init__(self):
        self.buttons()
        self.is_fullscreen = True
        self.questions = []
        self.answers = []
        self.question_buttons = [[]*5 for i in range(5)]
        self.result_label = Label()
        self.scores = {}
        self.score_updater = 100
        self.names = []
        self.num_of_players = 0
        self.player_pointer = 1
        self.enter_name_label = Label(root, text="Enter name for Player " + str(self.player_pointer), width=60, bg="black", fg="white", font=("Helvetica", 32, "bold"))
        self.entry = Entry(root, width=40)
        self.player1 = Label(root, text="", width=20, height=5, bg="yellow", fg="black", font=("Helvetica", 16, "bold"))
        self.player1_score = Label(root, text=0, width=20, bg="darkgray", fg="white", font=("Helvetica", 16, "bold"))
        self.player2 = Label(root, text="", width=20, height=5, bg="yellow", fg="black", font=("Helvetica", 16, "bold"))
        self.player2_score = Label(root, text=0, width=20, bg="darkgray", fg="white", font=("Helvetica", 16, "bold"))
        self.player3 = Label(root, text="", width=20, height=5, bg="yellow", fg="black", font=("Helvetica", 16, "bold"))
        self.player3_score = Label(root, text=0, width=20, bg="darkgray", fg="white", font=("Helvetica", 16, "bold"))
        self.player4 = Label(root, text="", width=20, height=5, bg="yellow", fg="black", font=("Helvetica", 16, "bold"))
        self.player4_score = Label(root, text=0, width=20, bg="darkgray", fg="white", font=("Helvetica", 16, "bold"))
        self.question_frame = LabelFrame()
        self.topic_labels = []


    def buttons(self):
        quit_button = Button(root, text="Quit", command=root.destroy, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        quit_button.pack(side="bottom", anchor="se")
        toggle_window_button = Button(root, text="Toggle Window", command=self.is_fullscreen_command, width=12, bg="darkgreen", fg="white", font=("Helvetica", 16, "bold"))
        toggle_window_button.pack(side="bottom", anchor="se")
        stop_music_button = Button(root, text="Stop Music", command=lambda:[self.destroy_frame()], width=12, bg="purple", fg="white", font=("Helvetica", 16, "bold"))
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
        self.one_player_button = Button(root, text="One", command=lambda:[self.destroy_player_select(), self.one_player()], width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        self.two_player_button = Button(root, text="Two", command=lambda:[self.destroy_player_select(), self.two_player()], width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        self.three_player_button = Button(root, text="Three", command=lambda:[self.destroy_player_select(), self.three_player()], width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        self.four_player_button = Button(root, text="Four", command=lambda:[self.destroy_player_select(), self.four_player()], width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))

        self.player_amount_label.place(relx=0.5, rely=0.2, anchor="center")
        self.one_player_button.place(relx=0.2, rely=0.5, anchor="center")
        self.two_player_button.place(relx=0.4, rely=0.5, anchor="center")
        self.three_player_button.place(relx=0.6, rely=0.5, anchor="center")
        self.four_player_button.place(relx=0.8, rely=0.5, anchor="center")

    def destroy_player_select(self):
        self.player_amount_label.destroy()
        self.one_player_button.destroy()
        self.two_player_button.destroy()
        self.three_player_button.destroy()
        self.four_player_button.destroy()

    def one_player(self):
        self.num_of_players = 1
        self.enter_name()
        self.get_name_button()
        
    def last(self):
        self.enter_name_label.destroy()
        self.entry.destroy()
        self.get_name_button.destroy()

        for name in self.names:
            self.scores[name] = 0

        if self.num_of_players == 1:
            self.player1.configure(text=self.names[0] + ":")
            self.player1.place(relx=0.51, rely=0.935, anchor="center")
            self.player1_score.place(relx=0.51, rely=0.960, anchor="center")
        elif self.num_of_players == 2:
            self.player1.configure(text=self.names[0] + ":")
            self.player1.place(relx=0.3, rely=0.935, anchor="center")
            self.player1_score.place(relx=0.3, rely=0.960, anchor="center")

            self.player2.configure(text=self.names[1] + ":")
            self.player2.place(relx=0.7, rely=0.935, anchor="center")
            self.player2_score.place(relx=0.7, rely=0.960, anchor="center")
        elif self.num_of_players == 3:
            self.player1.configure(text=self.names[0] + ":")
            self.player1.place(relx=0.3, rely=0.935, anchor="center")
            self.player1_score.place(relx=0.3, rely=0.960, anchor="center")

            self.player2.configure(text=self.names[1] + ":")
            self.player2.place(relx=0.5, rely=0.935, anchor="center")
            self.player2_score.place(relx=0.5, rely=0.960, anchor="center")

            self.player3.configure(text=self.names[2] + ":")
            self.player3.place(relx=0.7, rely=0.935, anchor="center")
            self.player3_score.place(relx=0.7, rely=0.960, anchor="center")
        else:
            self.player1.configure(text=self.names[0] + ":")
            self.player1.place(relx=0.2, rely=0.935, anchor="center")
            self.player1_score.place(relx=0.2, rely=0.960, anchor="center")

            self.player2.configure(text=self.names[1] + ":")
            self.player2.place(relx=0.4, rely=0.935, anchor="center")
            self.player2_score.place(relx=0.4, rely=0.960, anchor="center")

            self.player3.configure(text=self.names[2] + ":")
            self.player3.place(relx=0.6, rely=0.935, anchor="center")
            self.player3_score.place(relx=0.6, rely=0.960, anchor="center")

            self.player4.configure(text=self.names[3] + ":")
            self.player4.place(relx=0.8, rely=0.935, anchor="center")
            self.player4_score.place(relx=0.8, rely=0.960, anchor="center")
        
        for x in range(5):
            this_x = 0.20

            if x == 1:
                this_x = 0.35
            elif x == 2:
                this_x = 0.50
            elif x == 3:
                this_x = 0.65
            elif x == 4:
                this_x = 0.80

            self.topic_labels.append(Label(root, text=topics[x], width=20, height=3, bg="black", fg="yellow", font=("Helvetica", 20, "bold")))
            self.topic_labels[x].place(relx=this_x, rely=0.2, anchor="center")
            
            for y in range(5):
                self.question_buttons[x].append(Button(root, text="", width=20, height=3, command=lambda x1=x, y1=y: [self.question_buttons[x1][y1].configure(text="", state = DISABLED), self.ask_question(y1)], borderwidth=2, relief="groove", bg="darkblue", fg="white", font=("Helvetica", 16, "bold")))

                if y == 0:
                    self.question_buttons[x][y].configure(text="100")
                    self.question_buttons[x][y].place(relx=this_x, rely=0.3, anchor="center")
                elif y == 1:
                    self.question_buttons[x][y].configure(text="200")
                    self.question_buttons[x][y].place(relx=this_x, rely=0.4, anchor="center")
                elif y == 2:
                    self.question_buttons[x][y].configure(text="300")
                    self.question_buttons[x][y].place(relx=this_x, rely=0.5, anchor="center")
                elif y == 3:
                    self.question_buttons[x][y].configure(text="400")
                    self.question_buttons[x][y].place(relx=this_x, rely=0.6, anchor="center")
                elif y == 4:
                    self.question_buttons[x][y].configure(text="500")
                    self.question_buttons[x][y].place(relx=this_x, rely=0.7, anchor="center")



    def get_names(self):
        string = self.entry.get()
        self.names.append(string)
        self.entry.delete(0, END)

        if self.player_pointer != self.num_of_players:
            self.player_pointer += 1
            self.enter_name()
        else:
            self.last()

    def two_player(self):
        self.num_of_players = 2
        self.enter_name()
        self.get_name_button()

    def three_player(self):
        self.num_of_players = 3
        self.enter_name()
        self.get_name_button()

    def four_player(self):
        self.num_of_players = 4
        self.enter_name()
        self.get_name_button()

    def get_name_button(self):
        self.get_name_button = Button(root, text="Confirm", command=self.get_names, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        self.get_name_button.place(relx=0.5, rely=0.8, anchor="center")

    def enter_name(self):
        self.enter_name_label.configure(text="Enter name for Player " + str(self.player_pointer))
        self.enter_name_label.place(relx=0.5, rely=0.2, anchor="center")
        self.entry.focus_set()
        self.entry.place(relx=0.5, rely=0.5, anchor="center")

    def ask_question(self, col):
        if col == 0:
            self.score_updater = 100
        elif col == 1:
            self.score_updater = 200
        elif col == 2:
            self.score_updater = 300
        elif col == 3:
            self.score_updater = 400
        else:
            self.score_updater = 500

        print(self.score_updater)

        self.question_frame = LabelFrame(root, width=width, height=height, bg="black", fg="white")
        self.question_frame.pack(padx=10, pady=10)




        
        #self.score_updater = 100

    def destroy_frame(self):
        self.question_frame.destroy()
    


jeopardy = Jeopardy()
root.mainloop()
