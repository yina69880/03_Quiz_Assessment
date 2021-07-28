from tkinter import *
from functools import partial
import random
import csv
import re


class Start:
    def __init__(self):
        self.rounds = 0

        #set toplevel (GUI)
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
        self.round_warning = Label(self.start_frame, text="There will be endless rounds until you press 'End Game'",
                                   font="Arial 9 italic", fg="red")
        self.round_warning.grid(row=2, column=0)

        # Frame for rounds row 3
        self.round_frame = Frame(self.start_frame)
        self.round_frame.grid(row=3)

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
            print("you chose greek")

    def to_norse (self):
            print("you chose norse")

    def to_egyptian (self):
            print("you chose egyptian")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Legendary Figures Quiz")
    something = Start()
    root.mainloop()
































































































# This is Amos's code