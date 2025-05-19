#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# prototype.py ************************
#
#
# ferris’s_rafflematic
#     slider for # of attendees
#     checkbox for ferris
#     button for new number
#
#
# *************************************

import tkinter
import random


class App(object):
    def __init__(self, root):
        self.root = root

        self.root.title("Ferris' Rafflematic")
        self.root.geometry("500x120")

        self.attendees = tkinter.IntVar()
        self.include_ferris = tkinter.IntVar()
        self.include_ferris.set(0)

        self.scale = tkinter.Scale(root, orient=tkinter.HORIZONTAL, from_=1, to_=50, length=300, variable=self.attendees)
        self.scale.pack(anchor=tkinter.CENTER)

        self.check = tkinter.Checkbutton(self.root, text="Include Ferris", variable=self.include_ferris)
        self.check.pack(anchor=tkinter.CENTER)

        self.generate_button = tkinter.Button(self.root, text="Go", command=self.generate_winner)
        self.generate_button.pack(anchor=tkinter.CENTER)

        self.label = tkinter.Label(self.root, text="Good luck!")
        self.label.pack()

    def generate_winner(self):
        upper_bound = self.attendees.get()

        if self.include_ferris.get():
            lower_bound = 0
        else:
            lower_bound = 1

        winner = random.randint(lower_bound, int(upper_bound))
        self.label.config(text=str(winner))


def main():
    root = tkinter.Tk()
    _ = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
