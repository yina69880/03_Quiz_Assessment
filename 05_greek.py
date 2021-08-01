from tkinter import *
from functools import partial
import random
import csv


class Start:
    def __init__(self):
        self.rounds = 0

        #set toplevel (GUI)
        # self./// = Toplevel()
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # deity header text

        self.setup_text = Label(self.start_frame, text="Legendary Figures Quiz", font=("Arial", "16", "bold"))
        self.setup_text.grid(row=0, pady=5)

        # instruction text

        self.instructions_text = Label(self.start_frame, text="Please select the culture you wanna play \n",
                                       font=("Arial", "9"))
        self.instructions_text.grid(row=1, pady=5)

        # Round warning text row 2

        self.round_warning = Label(self.start_frame, text=" If left blank, There will be endless rounds",
                                   font="Helvetica 9 italic", fg="red")
        self.round_warning.grid(row=2, column=0)

        # to_game button frame row 4
        self.to_game_frame = Frame(self.start_frame)
        self.to_game_frame.grid(row=4)

        # Button Font
        button_font = "Arial 15 bold"

        # to_greek buttons row 4.1
        self.greek_button = Button(self.to_game_frame, text="Greek", font=button_font,
                                  command=self.to_greek, height=2, width=13, borderwidth=2,relief="raised")
        self.greek_button.grid(row=0, column=1, padx=10, pady=5)


    def to_greek (self):
            self.rounds = int(999999999)
            self.infinity = 1
            Greek(self)

    def open_play(self):
        Play(self)

    def update_numbers(self, option, category):
        if category == "top":
            self.egyptian_button.configure(state=NORMAL)
            self.answer_option = option.cget('text').replace("\n", " ")
        else:
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
        self.answer_box = Label(self.game_frame, text="", font="Helvetica 12 italic", width=35, wrap=300, bg=background)
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

        # Button frames for next, quit row 4
        self.button_frame = Frame(self.game_box, bg=background)
        self.button_frame.grid(row=4)


        # The Next button to proceed to the next round row 0 column 2
        self.next_button = Button(self.button_frame, text="Next",
                                  command=lambda: self.to_next(my_list), width=10,
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

    def to_next(self, greek_list):
            self.top_left_answer_button.config(state=NORMAL)
            self.top_right_answer_button.config(state=NORMAL)
            self.bottom_left_answer_button.config(state=NORMAL)
            self.bottom_right_answer_button.config(state=NORMAL)
            self.next_button.config(state=DISABLED)
            self.answer_box.config(text="")
            # chooses four different deities from the list
            question_ans = random.choice(greek_list)
            yes = random.choice(greek_list)
            no = random.choice(greek_list)
            ok = random.choice(greek_list)

            # incorrect[1,2,3] are the incorrect deities.
            self.question = question_ans[1]
            self.answer = question_ans[0]
            # self.hint = question_ans[2]
            incorrect1 = yes[0]
            incorrect2 = no[0]
            incorrect3 = ok[0]
            print(question_ans)

            self.deity_label.config(text=self.question)

            # I made the button_list a list so the list can be randomized so that the answer button locations is always different.
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



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Legendary Figures Quiz")
    something = Start()
    root.mainloop()