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

with open('finalJeopardy.json') as fj_file:
    fj = json.load(fj_file)

fj_topics = fj['topics']
fj_questions = fj['questions']
fj_answers = fj['answers']
zip_fj = zip(fj_topics, fj_questions, fj_answers)
list_fj = list(zip_fj)
random.shuffle(list_fj)
fj_topics, fj_questions, fj_answers = zip(*list_fj)

class Jeopardy:
    def __init__(self):
        self.buttons()
        self.is_fullscreen = True
        self.questions = []
        self.answers = []
        self.question_buttons = [[] for i in range(5)]
        self.result_label = Label()
        self.scores = {}
        self.score_updater = 100
        self.names = []
        self.num_of_players = 0
        self.player_pointer = 1
        self.enter_name_label = Label(root, text="Enter name for Player " + str(self.player_pointer), width=60, bg="black", fg="white", font=("Helvetica", 32, "bold"))
        self.entry = Entry(root, width=40)
        self.player_labels = {}
        self.player_score_labels = {}
        self.question_frame = LabelFrame()
        self.question_label = Label()
        self.answer_label = Label()
        self.topic_labels = []
        self.submit_button = Button()
        self.return_button = Button() 
        self.qa_dict = {}
        self.addition_buttons = []
        self.subtraction_buttons = []
        #self.daily_doublex = random.randrange(0,5)
        #self.daily_doubley = random.randrange(0,5)
        self.daily_doublex = 0
        self.daily_doubley = 0
        self.question_being_asked = False
        self.daily_double_player = ""
        self.daily_double_frame = LabelFrame()
        self.played_daily_double = False
        self.picking_labels = {}
        self.daily_double_entry = Entry()
        self.verify_daily_double_button = Button()
        self.daily_double_label = Label()
        self.topic_label = Label()
        self.enter_bid_label = Label()
        self.questions_left = 1
        self.final_jeopardy_button = Button()
        self.final_bid_label = Label()
        self.final_bid_button = Button()
        self.final_bid_entry = Entry()
        self.final_jeopardy_bets = {}
        self.zero_or_negative_label = Label()
        #self.questions_left = 25


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
            self.picking_labels[name] = Label(root, text="", width=10, bg="black", fg="white", font=("Helvetica", 16, "bold"))
            self.player_labels[name] = Label(root, text=name + ":", width=20, height=5, bg="darkblue", borderwidth=4, relief="raised", fg="white", font=("Helvetica", 16, "bold"))    
            self.player_score_labels[name] = Label(root, text=0, width=16, bg="black", fg="white", font=("Helvetica", 16, "bold"))
            self.addition_buttons.append(Button(root, text="+", command=lambda name1=name:[self.add(name1)], width=1, borderwidth=2, bg="green", fg="black", font=("Helvetica", 12, "bold")))
            self.subtraction_buttons.append(Button(root, text="-", command=lambda name1=name:[self.subtract(name1)], width=1, borderwidth=2, bg="red", fg="black", font=("Helvetica", 12, "bold")))

        self.daily_double_player = random.choice(self.names)
        self.player_labels[self.daily_double_player].configure(bg="yellow", fg="black")

        diff = 0.05
        labelx = 0.5
        playery = 0.935
        scorey = 0.965

        if self.num_of_players == 1:
            self.picking_labels[self.names[0]].place(relx=labelx, rely=0.83, anchor="center")
            self.player_labels[self.names[0]].place(relx=labelx, rely=playery, anchor="center")
            self.player_score_labels[self.names[0]].place(relx=labelx, rely=scorey, anchor="center")
            self.addition_buttons[0].place(relx=labelx-diff, rely=scorey, anchor="center")
            self.subtraction_buttons[0].place(relx=labelx+diff, rely=scorey, anchor="center")
        elif self.num_of_players == 2:
            labelx = 0.3

            for i in range(2):
                self.picking_labels[self.names[i]].place(relx=labelx, rely=0.83, anchor="center")
                self.player_labels[self.names[i]].place(relx=labelx, rely=playery, anchor="center")
                self.player_score_labels[self.names[i]].place(relx=labelx, rely=scorey, anchor="center")
                self.addition_buttons[i].place(relx=labelx-diff, rely=scorey, anchor="center")
                self.subtraction_buttons[i].place(relx=labelx+diff, rely=scorey, anchor="center")
                labelx += 0.4
        elif self.num_of_players == 3:
            labelx = 0.3

            for i in range(3):
                self.picking_labels[self.names[i]].place(relx=labelx, rely=0.83, anchor="center")
                self.player_labels[self.names[i]].place(relx=labelx, rely=playery, anchor="center")
                self.player_score_labels[self.names[i]].place(relx=labelx, rely=scorey, anchor="center")
                self.addition_buttons[i].place(relx=labelx-diff, rely=scorey, anchor="center")
                self.subtraction_buttons[i].place(relx=labelx+diff, rely=scorey, anchor="center")
                labelx += 0.2
        else:
            labelx = 0.2

            for i in range(4):
                self.picking_labels[self.names[i]].place(relx=labelx, rely=0.83, anchor="center")
                self.player_labels[self.names[i]].place(relx=labelx, rely=playery, anchor="center")
                self.player_score_labels[self.names[i]].place(relx=labelx, rely=scorey, anchor="center")
                self.addition_buttons[i].place(relx=labelx-diff, rely=scorey, anchor="center")
                self.subtraction_buttons[i].place(relx=labelx+diff, rely=scorey, anchor="center")
                labelx += 0.2
        
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
                self.question_buttons[x].append(Button(root, text="", width=20, height=3, command=lambda x1=x, y1=y: [self.question_buttons[x1][y1].configure(text="", state = DISABLED), self.ask_question(x1, y1)], borderwidth=2, relief="groove", bg="darkblue", fg="white", font=("Helvetica", 16, "bold")))

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

        self.picking_labels[self.daily_double_player].configure(text="Picking")

    def add(self, name):
        if self.question_being_asked == True:
            if name != self.daily_double_player:
                self.player_labels[self.daily_double_player].configure(bg="darkblue", fg="white")
                self.daily_double_player = name
                self.player_labels[self.daily_double_player].configure(bg="yellow", fg="black")

        self.scores[name] += self.score_updater
        self.player_score_labels[name].configure(text=self.scores[name])

    def subtract(self, name):
        self.scores[name] -= self.score_updater
        self.player_score_labels[name].configure(text=self.scores[name])

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

    def verify_bet(self):
        bet = self.daily_double_entry.get()
        
        if bet.isdigit():
            bet = int(bet)
            if (self.scores[self.daily_double_player] > 0 and bet > 0 and bet <= self.scores[self.daily_double_player]) or (self.scores[self.daily_double_player] <= 0 and bet > 0 and bet <= self.score_updater):
                self.score_updater = bet
                self.verify_daily_double_button.destroy()
                self.daily_double_label.destroy()
                self.topic_label.destroy()
                self.enter_bid_label.destroy()
                self.daily_double_entry.destroy()
                self.question_frame.pack()
            else:
                self.enter_bid_label.configure(text="Enter a valid bet!")
        else:
            self.enter_bid_label.configure(text="Enter a positive number!")

    def daily_double(self, topic):
        self.daily_double_frame = LabelFrame(root, width=width, height=height, bg="black", fg="white")
        self.daily_double_frame.pack(padx=10, pady=10)
        self.question_frame = LabelFrame(self.daily_double_frame, width=width, height=height, bg="black", fg="white")
        self.daily_double_label = Label(self.daily_double_frame, text="Daily Double", width=70, wrap=1200, bg="black", fg="white", font=("Helvetica", 32, "bold"))
        self.daily_double_label.place(relx=0.5, rely=0.2, anchor="center")

        self.topic_label = Label(self.daily_double_frame, text="Topic: " + topic + " (" + str(self.score_updater) + ")", width=50, bg="black", fg="yellow", font=("Helvetica", 18, "bold"))
        self.topic_label.place(relx=0.5, rely=0.3, anchor="center")
        
        self.enter_bid_label = Label(self.daily_double_frame, text=self.daily_double_player + ", enter your bid!", width=50, bg="black", fg="red", font=("Helvetica", 18, "bold"))
        self.enter_bid_label.place(relx=0.5, rely=0.5, anchor="center")

        self.daily_double_entry = Entry(self.daily_double_frame, width=40)
        self.daily_double_entry.place(relx=0.5, rely=0.55, anchor="center")
        self.daily_double_entry.focus_set()

        self.verify_daily_double_button = Button(self.daily_double_frame, text="Verify Bet", command=lambda:[self.verify_bet()],  width=30, bg="darkblue", fg="white", font=("Helvetica", 16, "bold"))
        self.verify_daily_double_button.place(relx=0.5, rely=0.7, anchor="center")

    def ask_question(self, row, col):
        self.picking_labels[self.daily_double_player].configure(text="")
        self.question_being_asked = True
        self.questions_left -= 1

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

        choices = list(zip(questions[row][col], answers[row][col]))
        random.shuffle(choices)
        question, answer = zip(*choices)
        question = question[0]
        answer = "What is " + answer[0] + "?"
        topic = topics[row]

        if row == self.daily_doublex and col == self.daily_doubley:
            self.played_daily_double = True
            self.daily_double(topic)
        else:   
            self.question_frame = LabelFrame(root, width=width, height=height, bg="black", fg="white")
            self.question_frame.pack(padx=10, pady=10)

        submit_button = Button(self.question_frame, text="Reveal Answer", command=lambda:[self.reveal_answer(), submit_button.destroy()], width=20, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        topic_label = Label(self.question_frame, text="Topic: " + topic, width=100, bg="black", fg="red", font=("Helvetica", 16, "bold"))
        question_label = Label(self.question_frame, text=question, width=100, wrap=1200, bg="black", fg="white", font=("Helvetica", 24, "bold"))
        self.answer_label = Label(self.question_frame, text=answer, width=100, bg="black", fg="yellow", font=("Helvetica", 24, "bold"))

        topic_label.place(relx=0.5, rely=0.1, anchor="center")
        question_label.place(relx=0.5, rely=0.3, anchor="center")
        submit_button.place(relx=0.5, rely=0.5, anchor="center")


    def reveal_answer(self):
        return_button = Button(self.question_frame, text="Return to Board", command=lambda:[self.destroy_frame(), return_button.destroy()], width=20, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        return_button.place(relx=0.5, rely=0.95, anchor="center")
        self.answer_label.place(relx=0.5, rely=0.7, anchor="center")

    def destroy_frame(self):
        if self.questions_left == 0:
            self.destroy_board()

        self.question_being_asked = False
        self.question_frame.destroy()

        if self.played_daily_double == True:
            self.daily_double_frame.destroy()
        
        self.score_updater = 100

        if self.questions_left == 0:
            self.final_jeopardy_button = Button(root, text="Start Final Jeopardy", command=lambda:[self.final_jeopardy_button.destroy(), self.final_jeopardy()], width=30, bg="black", fg="white", font=("Helvetica", 32, "bold"))
            self.final_jeopardy_button.place(relx=0.5, rely=0.5, anchor="center")
            self.player_labels[self.daily_double_player].configure(bg="darkblue", fg="white")
        else:
            self.picking_labels[self.daily_double_player].configure(text="Picking")

    def destroy_board(self):
        for x in range(5):
            self.topic_labels[x].destroy()
            for y in range(5):
                self.question_buttons[x][y].destroy()

        for name in self.names:
            self.picking_labels[name].destroy()

    def final_jeopardy(self):
        self.score_updater = 0
        self.player_pointer = 1
        self.question_frame = LabelFrame(root, width=width, height=height, bg="black", fg="white")
        self.question_frame.pack(padx=10, pady=10)
    
        fj_topic = fj_topics[0]
        fj_question = fj_questions[0]
        fj_answer = fj_answers[0]
        fj_choices = list(zip(fj_question, fj_answer))
        random.shuffle(fj_choices)
        fj_question, fj_answer = zip(*fj_choices)
        fj_question = fj_question[0]
        fj_answer = fj_answer[0]

        fj_label = Label(self.question_frame, text="Final Jeopardy", width=50, bg="black", fg="white", font=("Helvetica", 32, "bold"))
        fj_topic_label = Label(self.question_frame, text="Topic: " + fj_topic, width=50, bg="black", fg="yellow", font=("Helvetica", 16, "bold"))

        fj_label.place(relx=0.5, rely=0.2, anchor="center")
        fj_topic_label.place(relx=0.5, rely=0.3, anchor="center")

        self.enter_final_bid()

    def enter_final_bid(self):
        player = self.names[self.player_pointer - 1]

        self.final_bid_label = Label(self.question_frame, text=player + ", enter your bid!", width=30, bg="black", fg="red", font=("Helvetica", 16, "bold")) 
        self.final_bid_entry = Entry(self.question_frame, width=50)
        self.final_bid_button = Button(self.question_frame, command=lambda:[self.verify_final_bid()], text="Submit Bid", width=30, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))

        self.final_bid_label.place(relx=0.5, rely=0.5, anchor="center")
        self.final_bid_entry.place(relx=0.5, rely=0.6, anchor="center")
        self.final_bid_button.place(relx=0.5, rely=0.8, anchor="center")
    
        self.final_bid_entry.focus_set()

    def verify_final_bid(self):
        bet = self.final_bid_entry.get()
        player = self.names[self.player_pointer - 1]
        score = self.scores[player]
        self.final_bid_entry.delete(0, END)

        if bet.isdigit():
            bet = int(bet)

            if score > 0 and bet >= 100 and bet <= score:
                self.final_jeopardy_bets[player] = bet
                self.end_verify()
            elif score <= 0:
                must_bet = int(abs(score)/2)
                if bet == must_bet:
                    self.final_jeopardy_bets[player] = bet
                    self.end_verify()
                else:
                    self.final_bid_label.configure(text=player + ", enter " + str(must_bet) + " to continue.")

    def end_verify(self):
        if self.player_pointer == self.num_of_players:
            self.final_bid_label.destroy()
            self.final_bid_entry.destroy()
            self.final_bid_button.destroy()
            print(self.final_jeopardy_bets)
        else:
            self.player_pointer += 1
            self.final_bid_label.configure(text=self.names[self.player_pointer - 1] + ", enter your bid!")


jeopardy = Jeopardy()
root.mainloop()
