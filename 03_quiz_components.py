from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self):

        # set up frame

        self.start_frame = Frame(padx=80, pady=5)
        self.start_frame.grid()

        # header text

        self.start_text = Label(self.start_frame, text="Setup")
        self.start_text.grid(row=0)

        # frame for buttons

        self.setup_quit_button_frame = Frame(self.start_frame)
        self.setup_quit_button_frame.grid(row=1)

        # setup button

        self.setup_button = Button(self.setup_quit_button_frame, text="Play", command=lambda: self.open_setup())
        self.setup_button.grid(row=1, column=0, padx=5)

        # quit button

        self.quit_button = Button(self.setup_quit_button_frame, text="Quit", command=partial(root.destroy))
        self.quit_button.grid(row=1, column=1, padx=5)

    def open_setup(self):
        Setup(self)
        root.withdraw()


class Setup:
    def __init__(self, partner):

        #set toplevel

        self.setup_box = Toplevel()

        # set up closing behaviour

        self.setup_box.protocol('WM_DELETE_WINDOW', partial(root.destroy))

        # set up frame

        self.setup_frame = Frame(self.setup_box, padx=50, pady=5)
        self.setup_frame.grid()

        # Stored variables

        self.answer_option = ""
        self.given_option = ""

        # header text

        self.setup_text = Label(self.setup_frame, text="Legendary Figures Quiz", font=("Arial", "16", "bold"))
        self.setup_text.grid(row=0, pady=5)

        # instruction text

        self.instructions_text = Label(self.setup_frame, text="Please select the culture you wanna play \n",
                                       font=("Arial", "9"))
        self.instructions_text.grid(row=1, pady=5)

        # frame for answer options

        self.answer_frame = Frame(self.setup_frame)
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

        self.given_frame = Frame(self.setup_frame)
        self.given_frame.grid(row=4, pady=5)

        # Given buttons


        # frame for buttons

        self.play_quit_button_frame = Frame(self.setup_frame)
        self.play_quit_button_frame.grid(row=6, pady=5)


        # quit button

        self.quit_button = Button(self.play_quit_button_frame, text="Quit",
                                  command=partial(root.destroy))
        self.quit_button.grid(row=0, column=1, padx=5)

    def open_play(self):
        Play(self)
        self.setup_box.withdraw()

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

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Legendary Figures Quiz")
    something = Start()
    root.mainloop()