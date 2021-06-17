from tkinter import *
from functools import partial
import random
import csv



class Start:
    def __init__(self):
        self.rounds = 0

        #set toplevel (GUI)
        self.start_box = Toplevel()
        self.start_frame = Frame(self.start_box,padx=10, pady=10)
        self.start_frame.grid()

        # deity header text

        self.setup_text = Label(self.start_frame, text="Legendary Figures Quiz", font=("Arial", "16", "bold"))
        self.setup_text.grid(row=0, pady=5)

        # instruction text

        self.instructions_text = Label(self.start_frame, text="Please select the culture you wanna play \n",
                                       font=("Arial", "9"))
        self.instructions_text.grid(row=1, pady=5)

        # Round warning text row 2

        self.round_warning = Label(self.start_frame, text="If left blank there will be infinity rounds",
                                   font="Helvetica 9 italic", fg="red")
        self.round_warning.grid(row=2, column=0)

        # Frame for rounds row 3
        self.round_frame = Frame(self.start_frame)
        self.round_frame.grid(row=3)

        # Round Label row 0.0
        self.round_label = Label(self.round_frame, text="Rounds:", font="helvetica 15")
        self.round_label.grid(row=0, column=0)

        # Round Entry row 0.1
        self.round_entry = Entry(self.round_frame, font="Helvetica 20", bg="#FFFFFF"
                                 , width=5)
        self.round_entry.grid(row=0, column=1, padx=5, pady=5)

        # to_game button frame row 4
        self.to_game_frame = Frame(self.start_frame)
        self.to_game_frame.grid(row=4)

        # Button Font
        button_font = "Arial 15 bold"

        # to_egyptian buttons row 4.0
        self.egyptian_button = Button(self.to_game_frame, text="Egyptian", font=button_font,
                                  command=self.to_egyptian, height=2, width=13, borderwidth=2,relief="raised")
        self.egyptian_button.grid(row=0, column=0, padx=10, pady=5)

        # to_greek buttons row 4.1
        self.greek_button = Button(self.to_game_frame, text="Greek", font=button_font,
                                  command=self.to_greek, height=2, width=13, borderwidth=2,relief="raised")
        self.greek_button.grid(row=0, column=1, padx=10, pady=5)

        # to_norse buttons row 4.1
        self.norse_button = Button(self.to_game_frame, text="Norse", font=button_font,
                                  command=self.to_norse, height=2, width=13, borderwidth=2, relief="raised")
        self.norse_button.grid(row=0, column=2, padx=10, pady=5)



    def to_greek (self):
        self.rounds=self.round_entry.get()
        if self.rounds == "":
            self.rounds = int(999999999)
            self.infinity = 1
            Greek(self)
            self.start_box.destroy()
        else:
            try:
                self.rounds = int(self.rounds)
                self.infinity = 0
                if self.rounds >= 1:
                        Greek(self)
                        self.start_box.destroy()
                else:
                    self.round_warning.config(bg="red", text="Please enter a number or remain blank", fg="#FFFFFF")
                    self.round_entry.delete(0, "end")
            except ValueError:
                self.round_warning.config(bg="red",text="Please enter a number or remain blank",fg="#FFFFFF")
                self.round_entry.delete(0,"end")

    def to_norse (self):
        self.rounds=self.round_entry.get()
        if self.rounds == "":
            self.rounds = int(999999999)
            self.infinity = 1
            Norse(self)
            self.start_box.destroy()
        else:
            try:
                self.rounds = int(self.rounds)
                self.infinity = 0
                if self.rounds >= 1:
                        Norse(self)
                        self.start_box.destroy()
                else:
                    self.round_warning.config(bg="red", text="Please enter a number or remain blank", fg="#FFFFFF")
                    self.round_entry.delete(0, "end")
            except ValueError:
                self.round_warning.config(bg="red",text="Please enter a number or remain blank",fg="#FFFFFF")
                self.round_entry.delete(0,"end")

    def to_egyptian (self):
        self.rounds=self.round_entry.get()
        if self.rounds == "":
            self.rounds = int(999999999)
            self.infinity = 1
            Egypt(self)
            self.start_box.destroy()
        else:
            try:
                self.rounds = int(self.rounds)
                self.infinity = 0
                if self.rounds >= 1:
                        Egypt(self)
                        self.start_box.destroy()
                else:
                    self.round_warning.config(bg="red", text="Please enter a number or remain blank", fg="#FFFFFF")
                    self.round_entry.delete(0, "end")
            except ValueError:
                self.round_warning.config(bg="red",text="Please enter a number or remain blank",fg="#FFFFFF")
                self.round_entry.delete(0,"end")

        # frame for answer options

        self.answer_frame = Frame(self.start_frame)
        self.answer_frame.grid(row=2, pady=5)

        # Answer buttons

        # row 1

        self.norse_button = Button(self.answer_frame, text="Norse", width=10, height=2,
                                          command=lambda: self.update_numbers(self.norse_button, "top"))
        self.norse_button.grid(row=0, column=0, padx=5, pady=5)

        self.greek_button = Button(self.answer_frame, text="Greek", width=10, height=2,
                                          command=lambda: self.update_numbers(self.greek_button, "top"))
        self.greek_button.grid(row=0, column=1, padx=5, pady=5)

        self.egyptian_button = Button(self.answer_frame, text="Egyptian", width=10, height=2,
                                          command=lambda: self.update_numbers(self.egyptian_button, "top"))
        self.egyptian_button.grid(row=0, column=2, padx=5, pady=5)


        #bottom buttons

        # frame for given options

        self.given_frame = Frame(self.start_frame)
        self.given_frame.grid(row=4, pady=5)

        # Given buttons


        # frame for buttons

        self.play_quit_button_frame = Frame(self.start_frame)
        self.play_quit_button_frame.grid(row=6, pady=5)


        # quit button

        self.quit_button = Button(self.play_quit_button_frame, text="Quit",
                                  command=partial(root.destroy))
        self.quit_button.grid(row=0, column=1, padx=5)

    def open_play(self):
        Play(self)
        self.start_box.withdraw()

    # update_numbers enables all buttons in category and then disables selected button,
    # updates selected option variables

    def update_numbers(self, option, category):
        if category == "top":
            self.norse_button.configure(state=NORMAL)
            self.greek_button.configure(state=NORMAL)
            self.egyptian_button.configure(state=NORMAL)
            self.answer_option = option.cget('text').replace("\n", " ")
        else:
            self.norse_button.configure(state=NORMAL)
            self.greek_button.configure(state=NORMAL)
            self.egyptian_button.configure(state=NORMAL)
            self.given_option = option.cget('text').replace("\n", " ")

        option.config(state=DISABLED)


class Play:
    def __init__(self, partner):

        # set Toplevel

        self.play_box = Toplevel()

        # set up closing behaviour

        self.play_box.protocol('WM_DELETE_WINDOW', partial(root.destroy))

        # set up frame

        self.play_frame = Frame(self.play_box, padx=50, pady=5)
        self.play_frame.grid()

        # header text

        self.play_text = Label(self.play_frame, text="Play")
        self.play_text.grid(row=0)

        # body text

        self.play_text = Label(self.play_frame, text="{},{}".format(partner.answer_option, partner.given_option))
        self.play_text.grid(row=1)

        # frame for buttons

        self.help_stats_button_frame = Frame(self.play_frame)
        self.help_stats_button_frame.grid(row=2, pady=5)

        # help button

        self.help_button = Button(self.help_stats_button_frame, text="Help")
        self.help_button.grid(row=0, column=0, padx=5)

        # stats button

        self.stats_button = Button(self.help_stats_button_frame, text="Stats")
        self.stats_button.grid(row=0, column=1, padx=5)

        # quit button

        self.quit_button = Button(self.play_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=3)
def to_quit():
    root.destroy()

class Greek:
    def __init__(self, partner):
        background = "#FFF4C3"
        # Import the csv file, name of csv file goes here...
        with open('Greek_gods_list.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # List to store the answers
        self.game_history = []

        # Initial Score
        self.score = 0

        # Amount of total rounds
        self.total_rounds = partner.rounds

        self.infinity = partner.infinity

        # Amounts of games played
        self.played = 0

        # chooses four different cultures from the list
        question_ans = random.choice(my_list)
        yes = random.choice(my_list)
        no = random.choice(my_list)
        ok = random.choice(my_list)

        # incorrect[1,2,3] are the incorrect gods
        self.question = question_ans[1]
        self.answer = question_ans[0]
        wrong_1 = yes[0]
        wrong_2 = no[0]
        wrong_3 = ok[0]
        print(question_ans)

        # I made the button_list a list so the list can be mixed so that the answer button positions are not always in the same place is always different
        buttons_list = [self.answer, wrong_1, wrong_2, wrong_3]
        random.shuffle(buttons_list)
        self.top_left = buttons_list[0]
        self.top_right = buttons_list[1]
        self.bottom_left = buttons_list[2]
        self.bottom_right = buttons_list[3]

        # GUI Setup
        self.game_box = Toplevel(bg=background)
        self.game_frame = Frame(self.game_box, bg=background)
        self.game_frame.grid()
        self.game_box.protocol('WM_DELETE_WINDOW', to_quit)

        # Gods Label row 0
        self.deity_label = Label(self.game_frame, text=self.question,
                                   font="Helvetica 15 bold", bg=background)
        self.deity_label.grid(row=0)

        # Label showing correct or incorrect row 1
        self.answer_box = Label(self.game_frame, text="", font="Helvetica 12 italic", width=35, wrap=300)
        self.answer_box.grid(row=1)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box, width=50, height=50, bg=background)
        self.top_answers_frame.grid(row=2, padx=5)

        # design and style of the buttons
        wt = 20
        ht = 2
        wr = 160
        ft = "Helvetica 15"

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text=self.top_left,
                                             font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                             command=lambda: self.show_answer(self.top_left))
        self.top_left_answer_button.grid(column=0, row=0, padx=5, pady=5)

        self.top_right_answer_button = Button(self.top_answers_frame, text=self.top_right,
                                              font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                              command=lambda: self.show_answer(self.top_right))
        self.top_right_answer_button.grid(column=1, row=0, padx=5, pady=5)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text=self.bottom_left,
                                                font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                                command=lambda: self.show_answer(self.bottom_left))
        self.bottom_left_answer_button.grid(column=0, row=1, padx=5, pady=5)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text=self.bottom_right,
                                                 font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                                 command=lambda: self.show_answer(self.bottom_right))
        self.bottom_right_answer_button.grid(column=1, row=1, padx=5, pady=5)

        # Label for the score and games played row 3
        self.score_label = Label(self.game_box, text="{} correct, {} rounds played".format(self.score, self.played),
                                 bg=background)
        self.score_label.grid(row=3)

        # Button frames for next, quit and hint button row 4
        self.button_frame = Frame(self.game_box, bg=background)
        self.button_frame.grid(row=4)

        # The quit button so users can quit the game early row 0 column 1
        self.quit_button = Button(self.button_frame, text="End Game", command=lambda: self.to_end(self.game_history)
                                  , width=10,
                                  font="Helvetica 10 bold")
        self.quit_button.grid(row=0, column=0, padx=5, pady=8)

        # The hint button to get the hint for this country row 0 column 1
        self.hint_button = Button(self.button_frame, text="Hint", command=self.to_hint, width=10,
                                  font="Helvetica 10 bold")
        self.hint_button.grid(row=0, column=1, padx=5, pady=8)

        # The Next button to proceed to the next round row 0 column 2
        self.next_button = Button(self.button_frame, text="Next",
                                  command=lambda: self.to_next(my_list, self.game_history, self.infinity), width=10,
                                  font="Helvetica 10 bold")
        self.next_button.grid(row=0, column=2, padx=5, pady=8)
        # Disable the next button initially,
        self.next_button.config(state=DISABLED)

    def show_answer(self, location):

        # Disable all the buttons
        self.top_left_answer_button.config(state=DISABLED)
        self.top_right_answer_button.config(state=DISABLED)
        self.bottom_left_answer_button.config(state=DISABLED)
        self.bottom_right_answer_button.config(state=DISABLED)
        self.hint_button.config(state=DISABLED)

        # Enable the next_button
        self.next_button.config(state=NORMAL)

        # Increase total rounds played by 1
        self.played += 1

        # Check if button is correct.
        if location == self.answer:
            self.answer_box.config(text="Correct!", fg="green")
            self.score += 1
            correct_answer = "{}, the answer was {} \u2713".format(self.question,self.answer)
            self.game_history.append(correct_answer)
        else:
            self.answer_box.config(text="Incorrect, correct deity is {}".format(self.answer), fg="red")
            incorrect_answer = "{}, the answer was {} \u274c, you answered {}".format(self.question,self.answer,location)
            self.game_history.append(incorrect_answer)

        # Update the score that the user has
        self.score_label.config(text="{} correct / {} rounds played".format(self.score, self.played))

    def to_next(self, greek_list, history,infinity):
        # if the amount of rounds played is 15 the player is taken to the end screen
        if self.played == self.total_rounds:
            easy=1
            played=self.total_rounds
            End(self.score, history,easy,played)
            self.game_box.destroy()

        # Else the quiz repeats and new questions are asked.
        else:
            self.top_left_answer_button.config(state=NORMAL)
            self.top_right_answer_button.config(state=NORMAL)
            self.bottom_left_answer_button.config(state=NORMAL)
            self.bottom_right_answer_button.config(state=NORMAL)
            self.next_button.config(state=DISABLED)
            self.answer_box.config(text="")
            self.hint_button.config(state=NORMAL)

            # chooses four different countries / capitals from the list
            question_ans = random.choice(greek_list)
            if infinity == 0:
                greek_list.remove(question_ans)
            else:
                pass
            yes = random.choice(greek_list)
            no = random.choice(greek_list)
            ok = random.choice(greek_list)

            # Defining variables for the capitals and countries,
            # question is the capital in question
            # self.answer is the correct answer
            # incorrect[1,2,3] are the incorrect countries.
            self.question = question_ans[1]
            self.answer = question_ans[0]
            self.hint = question_ans[2]
            incorrect1 = yes[0]
            incorrect2 = no[0]
            incorrect3 = ok[0]
            print(question_ans)

            # I made the button_list a list so the list can be randomized so that the answer button locations is always
            # different.
            button_list = [self.answer, incorrect1, incorrect2, incorrect3]
            random.shuffle(button_list)
            self.top_left = button_list[0]
            self.top_right = button_list[1]
            self.bottom_left = button_list[2]
            self.bottom_right = button_list[3]

            # Defining the randomized list to their corresponding buttons
            self.top_left_answer_button.config(text=self.top_left, command=lambda: self.reveal_answer(self.top_left))
            self.top_right_answer_button.config(text=self.top_right, command=lambda: self.reveal_answer(self.top_right))
            self.bottom_left_answer_button.config(text=self.bottom_left,
                                                  command=lambda: self.reveal_answer(self.bottom_left))
            self.bottom_right_answer_button.config(text=self.bottom_right,
                                                   command=lambda: self.reveal_answer(self.bottom_right))

    def to_hint(self):
        get_hint = Hint(self)
        get_hint.help_text.configure(text="this country is located in: {}".format(self.hint))

    def to_end(self,history):
        easy=1
        End(self.score,history,easy,self.played)
        self.game_box.destroy()

class Norse:
    def __init__(self, partner):
        background = "#FFF4C3"
        # Import the csv file, name of csv file goes here...
        with open('Norse_gods.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # List to store the answers
        self.game_history = []

        # Initial Score
        self.score = 0

        # Amount of total rounds
        self.total_rounds = partner.rounds

        self.infinity = partner.infinity

        # Amounts of games played
        self.played = 0

        # chooses four different cultures from the list
        question_ans = random.choice(my_list)
        yes = random.choice(my_list)
        no = random.choice(my_list)
        ok = random.choice(my_list)

        # incorrect[1,2,3] are the incorrect gods
        self.question = question_ans[1]
        self.answer = question_ans[0]
        wrong_1 = yes[0]
        wrong_2 = no[0]
        wrong_3 = ok[0]
        print(question_ans)

        # I made the button_list a list so the list can be mixed so that the answer button positions are not always in the same place is always different
        buttons_list = [self.answer, wrong_1, wrong_2, wrong_3]
        random.shuffle(buttons_list)
        self.top_left = buttons_list[0]
        self.top_right = buttons_list[1]
        self.bottom_left = buttons_list[2]
        self.bottom_right = buttons_list[3]

        # GUI Setup
        self.game_box = Toplevel(bg=background)
        self.game_frame = Frame(self.game_box, bg=background)
        self.game_frame.grid()
        self.game_box.protocol('WM_DELETE_WINDOW', to_quit)

        # Gods Label row 0
        self.deity_label = Label(self.game_frame, text=self.question,
                                 font="Helvetica 15 bold", bg=background)
        self.deity_label.grid(row=0)

        # Label showing correct or incorrect row 1
        self.answer_box = Label(self.game_frame, text="", font="Helvetica 12 italic", width=35, wrap=300)
        self.answer_box.grid(row=1)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box, width=50, height=50, bg=background)
        self.top_answers_frame.grid(row=2, padx=5)

        # design and style of the buttons
        wt = 20
        ht = 2
        wr = 160
        ft = "Helvetica 15"

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text=self.top_left,
                                             font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                             command=lambda: self.show_answer(self.top_left))
        self.top_left_answer_button.grid(column=0, row=0, padx=5, pady=5)

        self.top_right_answer_button = Button(self.top_answers_frame, text=self.top_right,
                                              font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                              command=lambda: self.show_answer(self.top_right))
        self.top_right_answer_button.grid(column=1, row=0, padx=5, pady=5)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text=self.bottom_left,
                                                font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                                command=lambda: self.show_answer(self.bottom_left))
        self.bottom_left_answer_button.grid(column=0, row=1, padx=5, pady=5)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text=self.bottom_right,
                                                 font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr,
                                                 bg="#EEE6D2",
                                                 command=lambda: self.show_answer(self.bottom_right))
        self.bottom_right_answer_button.grid(column=1, row=1, padx=5, pady=5)

        # Label for the score and games played row 3
        self.score_label = Label(self.game_box, text="{} correct, {} rounds played".format(self.score, self.played),
                                 bg=background)
        self.score_label.grid(row=3)

        # Button frames for next, quit and hint button row 4
        self.button_frame = Frame(self.game_box, bg=background)
        self.button_frame.grid(row=4)

        # The quit button so users can quit the game early row 0 column 1
        self.quit_button = Button(self.button_frame, text="End Game", command=lambda: self.to_end(self.game_history)
                                  , width=10,
                                  font="Helvetica 10 bold")
        self.quit_button.grid(row=0, column=0, padx=5, pady=8)

        # The hint button to get the hint for this country row 0 column 1
        self.hint_button = Button(self.button_frame, text="Hint", command=self.to_hint, width=10,
                                  font="Helvetica 10 bold")
        self.hint_button.grid(row=0, column=1, padx=5, pady=8)

        # The Next button to proceed to the next round row 0 column 2
        self.next_button = Button(self.button_frame, text="Next",
                                  command=lambda: self.to_next(my_list, self.game_history, self.infinity), width=10,
                                  font="Helvetica 10 bold")
        self.next_button.grid(row=0, column=2, padx=5, pady=8)
        # Disable the next button initially,
        self.next_button.config(state=DISABLED)

    def show_answer(self, location):

        # Disable all the buttons
        self.top_left_answer_button.config(state=DISABLED)
        self.top_right_answer_button.config(state=DISABLED)
        self.bottom_left_answer_button.config(state=DISABLED)
        self.bottom_right_answer_button.config(state=DISABLED)
        self.hint_button.config(state=DISABLED)

        # Enable the next_button
        self.next_button.config(state=NORMAL)

        # Increase total rounds played by 1
        self.played += 1

        # Check if button is correct.
        if location == self.answer:
            self.answer_box.config(text="Correct!", fg="green")
            self.score += 1
            correct_answer = "{}, the answer was {} \u2713".format(self.question, self.answer)
            self.game_history.append(correct_answer)
        else:
            self.answer_box.config(text="Incorrect, correct deity is {}".format(self.answer), fg="red")
            incorrect_answer = "{}, the answer was {} \u274c, you answered {}".format(self.question, self.answer,
                                                                                      location)
            self.game_history.append(incorrect_answer)

        # Update the score that the user has
        self.score_label.config(text="{} correct / {} rounds played".format(self.score, self.played))

    def to_next(self, norse_list, history, infinity):
        # if the amount of rounds played is 15 the player is taken to the end screen
        if self.played == self.total_rounds:
            easy = 1
            played = self.total_rounds
            End(self.score, history, easy, played)
            self.game_box.destroy()

        # Else the quiz repeats and new questions are asked.
        else:
            self.top_left_answer_button.config(state=NORMAL)
            self.top_right_answer_button.config(state=NORMAL)
            self.bottom_left_answer_button.config(state=NORMAL)
            self.bottom_right_answer_button.config(state=NORMAL)
            self.next_button.config(state=DISABLED)
            self.answer_box.config(text="")
            self.hint_button.config(state=NORMAL)

            # chooses four different countries / capitals from the list
            question_ans = random.choice(norse_list)
            if infinity == 0:
                norse_list.remove(question_ans)
            else:
                pass
            yes = random.choice(norse_list)
            no = random.choice(norse_list)
            ok = random.choice(norse_list)

            # Defining variables for the capitals and countries,
            # question is the capital in question
            # self.answer is the correct answer
            # incorrect[1,2,3] are the incorrect countries.
            self.question = question_ans[1]
            self.answer = question_ans[0]
            self.hint = question_ans[2]
            incorrect1 = yes[0]
            incorrect2 = no[0]
            incorrect3 = ok[0]
            print(question_ans)

            # I made the button_list a list so the list can be randomized so that the answer button locations is always
            # different.
            button_list = [self.answer, incorrect1, incorrect2, incorrect3]
            random.shuffle(button_list)
            self.top_left = button_list[0]
            self.top_right = button_list[1]
            self.bottom_left = button_list[2]
            self.bottom_right = button_list[3]

            # Defining the randomized list to their corresponding buttons
            self.top_left_answer_button.config(text=self.top_left,
                                               command=lambda: self.show_answer(self.top_left))
            self.top_right_answer_button.config(text=self.top_right,
                                                command=lambda: self.show_answer(self.top_right))
            self.bottom_left_answer_button.config(text=self.bottom_left,
                                                  command=lambda: self.show_answer(self.bottom_left))
            self.bottom_right_answer_button.config(text=self.bottom_right,
                                                   command=lambda: self.show_answer(self.bottom_right))

    def to_hint(self):
        get_hint = Hint(self)
        get_hint.help_text.configure(text="this country is located in: {}".format(self.hint))

    def to_end(self, history):
        easy = 1
        End(self.score, history, easy, self.played)
        self.game_box.destroy()

class Egypt:
    def __init__(self, partner):
        background = "#FFF4C3"
        # Import the csv file, name of csv file goes here...
        with open('Egyptian_gods.csv', 'r') as f:
            # make csv file into list
            file = csv.reader(f)
            next(f)
            my_list = list(file)

        # List to store the answers
        self.game_history = []

        # Initial Score
        self.score = 0

        # Amount of total rounds
        self.total_rounds = partner.rounds

        self.infinity = partner.infinity

        # Amounts of games played
        self.played = 0

        # chooses four different cultures from the list
        question_ans = random.choice(my_list)
        yes = random.choice(my_list)
        no = random.choice(my_list)
        ok = random.choice(my_list)

        # incorrect[1,2,3] are the incorrect gods
        self.question = question_ans[1]
        self.answer = question_ans[0]
        wrong_1 = yes[0]
        wrong_2 = no[0]
        wrong_3 = ok[0]
        print(question_ans)

        # I made the button_list a list so the list can be mixed so that the answer button positions are not always in the same place is always different
        buttons_list = [self.answer, wrong_1, wrong_2, wrong_3]
        random.shuffle(buttons_list)
        self.top_left = buttons_list[0]
        self.top_right = buttons_list[1]
        self.bottom_left = buttons_list[2]
        self.bottom_right = buttons_list[3]

        # GUI Setup
        self.game_box = Toplevel(bg=background)
        self.game_frame = Frame(self.game_box, bg=background)
        self.game_frame.grid()
        self.game_box.protocol('WM_DELETE_WINDOW', to_quit)

        # Gods Label row 0
        self.deity_label = Label(self.game_frame, text=self.question,
                                   font="Helvetica 15 bold", bg=background)
        self.deity_label.grid(row=0)

        # Label showing correct or incorrect row 1
        self.answer_box = Label(self.game_frame, text="", font="Helvetica 12 italic", width=35, wrap=300)
        self.answer_box.grid(row=1)

        # Setup grid for answer buttons row 2
        self.top_answers_frame = Frame(self.game_box, width=50, height=50, bg=background)
        self.top_answers_frame.grid(row=2, padx=5)

        # design and style of the buttons
        wt = 20
        ht = 2
        wr = 160
        ft = "Helvetica 15"

        # Top level answers buttons row 2.0
        self.top_left_answer_button = Button(self.top_answers_frame, text=self.top_left,
                                             font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                             command=lambda: self.show_answer(self.top_left))
        self.top_left_answer_button.grid(column=0, row=0, padx=5, pady=5)

        self.top_right_answer_button = Button(self.top_answers_frame, text=self.top_right,
                                              font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                              command=lambda: self.show_answer(self.top_right))
        self.top_right_answer_button.grid(column=1, row=0, padx=5, pady=5)

        # Bottom level answers buttons row 2.1
        self.bottom_left_answer_button = Button(self.top_answers_frame, text=self.bottom_left,
                                                font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                                command=lambda: self.show_answer(self.bottom_left))
        self.bottom_left_answer_button.grid(column=0, row=1, padx=5, pady=5)

        self.bottom_right_answer_button = Button(self.top_answers_frame, text=self.bottom_right,
                                                 font=ft, padx=5, pady=5, width=wt, height=ht, wrap=wr, bg="#EEE6D2",
                                                 command=lambda: self.show_answer(self.bottom_right))
        self.bottom_right_answer_button.grid(column=1, row=1, padx=5, pady=5)

        # Label for the score and games played row 3
        self.score_label = Label(self.game_box, text="{} correct, {} rounds played".format(self.score, self.played),
                                 bg=background)
        self.score_label.grid(row=3)

        # Button frames for next, quit and hint button row 4
        self.button_frame = Frame(self.game_box, bg=background)
        self.button_frame.grid(row=4)

        # The quit button so users can quit the game early row 0 column 1
        self.quit_button = Button(self.button_frame, text="End Game", command=lambda: self.to_end(self.game_history)
                                  , width=10,
                                  font="Helvetica 10 bold")
        self.quit_button.grid(row=0, column=0, padx=5, pady=8)


        # The Next button to proceed to the next round row 0 column 2
        self.next_button = Button(self.button_frame, text="Next",
                                  command=lambda: self.to_next(my_list, self.game_history, self.infinity), width=10,
                                  font="Helvetica 10 bold")
        self.next_button.grid(row=0, column=2, padx=5, pady=8)
        # Disable the next button initially,
        self.next_button.config(state=DISABLED)
    def show_answer(self, location):

        # Disable all the buttons
        self.top_left_answer_button.config(state=DISABLED)
        self.top_right_answer_button.config(state=DISABLED)
        self.bottom_left_answer_button.config(state=DISABLED)
        self.bottom_right_answer_button.config(state=DISABLED)

        # Enable the next_button
        self.next_button.config(state=NORMAL)

        # Increase total rounds played by 1
        self.played += 1

        # Check if button is correct.
        if location == self.answer:
            self.answer_box.config(text="Correct!", fg="green")
            self.score += 1
            correct_answer = "{}, the answer was {} \u2713".format(self.question,self.answer)
            self.game_history.append(correct_answer)
        else:
            self.answer_box.config(text="Incorrect, correct deity is {}".format(self.answer), fg="red")
            incorrect_answer = "{}, the answer was {} \u274c, you answered {}".format(self.question,self.answer,location)
            self.game_history.append(incorrect_answer)

        # Update the score that the user has
        self.score_label.config(text="{} correct / {} rounds played".format(self.score, self.played))

    def to_next(self, greek_list, history,infinity):
        # if the amount of rounds played is 15 the player is taken to the end screen
        if self.played == self.total_rounds:
            easy=1
            played=self.total_rounds
            End(self.score, history,easy,played)
            self.game_box.destroy()

        # Else the quiz repeats and new questions are asked.
        else:
            self.top_left_answer_button.config(state=NORMAL)
            self.top_right_answer_button.config(state=NORMAL)
            self.bottom_left_answer_button.config(state=NORMAL)
            self.bottom_right_answer_button.config(state=NORMAL)
            self.next_button.config(state=DISABLED)
            self.answer_box.config(text="")
            self.hint_button.config(state=NORMAL)

            # chooses four different countries / capitals from the list
            question_ans = random.choice(greek_list)
            if infinity == 0:
                greek_list.remove(question_ans)
            else:
                pass
            yes = random.choice(greek_list)
            no = random.choice(greek_list)
            ok = random.choice(greek_list)

            # Defining variables for the capitals and countries,
            # question is the capital in question
            # self.answer is the correct answer
            # incorrect[1,2,3] are the incorrect countries.
            self.question = question_ans[1]
            self.answer = question_ans[0]
            self.hint = question_ans[2]
            incorrect1 = yes[0]
            incorrect2 = no[0]
            incorrect3 = ok[0]
            print(question_ans)

            # I made the button_list a list so the list can be randomized so that the answer button locations is always
            # different.
            button_list = [self.answer, incorrect1, incorrect2, incorrect3]
            random.shuffle(button_list)
            self.top_left = button_list[0]
            self.top_right = button_list[1]
            self.bottom_left = button_list[2]
            self.bottom_right = button_list[3]

            # Defining the randomized list to their corresponding buttons
            self.top_left_answer_button.config(text=self.top_left, command=lambda: self.show_answer(self.top_left))
            self.top_right_answer_button.config(text=self.top_right, command=lambda: self.show_answer(self.top_right))
            self.bottom_left_answer_button.config(text=self.bottom_left,
                                                  command=lambda: self.show_answer(self.bottom_left))
            self.bottom_right_answer_button.config(text=self.bottom_right,
                                                   command=lambda: self.show_answer(self.bottom_right))


    def to_end(self,history):
        easy=1
        End(self.score,history,easy,self.played)
        self.game_box.destroy()


class End:
    def __init__(self, score, history, difficulty, played):
        # Background color is light yellow
        background = "#FFF4C3"

        # Accuracy percentage
        if played == 0:
            percentage = 0
        else:
            percentage = (score / played) * 100

        # End Frame
        self.end_box = Toplevel()
        self.end_frame = Frame(self.end_box, bg=background)
        self.end_frame.grid(row=0)
        self.end_box.protocol('WM_DELETE_WINDOW', to_quit)

        # Heading row 0
        self.end_heading = Label(self.end_frame, text="Thanks for playing!", font="Helvetica 25 bold",
                                 bg=background)
        self.end_heading.grid(row=0, padx=10)

        # Game statistics row 1
        self.end_stats = Label(self.end_frame, text="You managed to get \n {} \n right out of \n {} \n\n"
                                                    "Accuracy percentage : {:.2f}%".format(score, played,
                                                                                           percentage),
                               bg=background, font="Helvetica 10")
        self.end_stats.grid(row=1)

        # Button grid row 2
        # Three Different buttons.
        # Export, Retry, Quit
        self.end_buttons = Frame(self.end_frame, bg=background)
        self.end_buttons.grid(row=2)

        # Export button row 0 column 0
        self.end_export_button = Button(self.end_buttons, text="Export", font="Helvetica 10 bold",
                                        command=lambda: self.to_export(history, difficulty, score, percentage,
                                                                       played), width=10
                                        , bg="#99CCFF", height=2)
        self.end_export_button.grid(row=0, column=0, padx=6, pady=5)

        # Retry Button row 0 column 1
        self.end_retry_button = Button(self.end_buttons, text="Play Again!", font="Helvetica 10 bold",
                                       command=self.to_start, width=10, bg="#FFFF99", height=2)
        self.end_retry_button.grid(row=0, column=1, padx=6, pady=5)

        # Quit button row 0 column 2
        self.end_quit_button = Button(self.end_buttons, text="Quit", font="Helvetica 10 bold",
                                      command=root.quit, width=10, bg="#FFBAB8", height=2)
        self.end_quit_button.grid(row=0, column=2, padx=6, pady=5)

    def to_start(self):
        Start()
        self.end_box.destroy()

    def to_export(self, history, difficulty, score, percentage, played):
        Export(self, history, difficulty, score, percentage, played)

class Export:
    def __init__(self, partner, history, difficulty, score, percentage, played):

        # Background Color is light yellow
        background = "#FFF4C3"

        # disable export button
        partner.end_export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press 'x' cross at the top, closes export and 'releases' export button.
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="Arial 15 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below",
                                 justify=LEFT, width=40, wrap=250, bg=background)
        self.export_text.grid(row=1)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename you entered already exists,"
                                                         "it will be overwritten.", justify=LEFT,
                                 fg='red', font="Arial 10 italic", bg=background,
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon", bg=background
                                      )
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame, bg=background)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", width=5,
                                  command=partial(
                                      lambda: self.save_history(partner, history, difficulty, score, percentage,
                                                                played)))
        self.save_button.grid(row=0, column=0, padx=5, pady=5)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", width=5,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1, padx=5, pady=5)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.end_export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_history(self, partner, history, difficulty, score, percentage, played):
        global problem

        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = " (no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text="Invalid filename - {}".format(problem))

            self.filename_entry.config(bg="#ffafaf")

        else:
            filename = filename + ".txt"

            f = open(filename, "w+", encoding="utf-8")

            if difficulty == 1:
                f.write("You've played the Greek culture!\n\n")
            else:
                f.write("You've played the  \n\n")

            for item in history:
                f.write(item + "\n")

            f.write("\n\nGame Details\n\n"
                    "You got {} out of {} correct\n\n"
                    "Percentage Correct = {:.2f}% \n\n".format(score, played, percentage))
            if percentage >= 90:
                f.write("Wonderful Job!!")
            elif percentage >= 80:
                f.write("Exellent Effort")
            elif percentage >= 60:
                f.write("Nice try")
            elif percentage >= 40:
                f.write("Better luck next round")
            elif percentage >= 20:
                f.write("Could've been better")
            else:
                f.write("What happened?")

            f.close()

            self.close_export(partner)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Legendary Figures Quiz")
    something = Start()
    root.mainloop()



# This is Amos's code