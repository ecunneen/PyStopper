import random
import time
from tkinter import *


# Starts the tkinter loop thingy and gives it a window to do stuff in.
class TopWindow:

    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack()

        # Creates canvas on which red/green will be drawn
        self.lightarea = Canvas(self.root, width=600, height=400)
        self.lightarea.pack()

        self.isGreen = True

    # Draws green square. Draws red square.
    def light_green(self):
        self.lightarea.create_rectangle(20, 20, 581, 381, fill="green", tags="greenlight")
        print("Green square drawn.")

    def light_red(self):
        self.lightarea.create_rectangle(20, 20, 581, 381, fill="red", tags="redlight")
        print("Red square drawn.")

    # # Draws the green square, waits for timegreen milliseconds.
    # def startPlaying():
    #     print("Begin Playing")
    #     lightGreen()
    #     root.after(random.randint(1000, 5000), lightRed)
    #
    # # Same as above, just with the red square
    # def stopPlaying():
    #     lightRed()
    #     root.after(random.randint(1000, 5000), lightGreen)

    def toggle_playing(self):
        self.lightarea.delete("all")
        if self.isGreen:
            self.isGreen = False
            self.light_red()
        else:
            self.isGreen = True
            self.light_green()

    # Generates one "cycle" of green and red lights
    def play_cycle(self):
        self.toggle_playing()
        self.root.after(random.randint(1000, 5000), self.play_cycle)

    # Code for the exit button.
    def close_program(self):
        self.root.destroy()

    def run(self):
        stopb = Button(self.root, text="Close program", command=self.close_program)
        stopb.pack(padx=20, pady=20)

        start_button = Button(self.root, text="Start", command=self.play_cycle)
        start_button.pack(padx=20, pady=20)

        self.light_green()
        self.root.mainloop()

our_window = TopWindow()
our_window.run()