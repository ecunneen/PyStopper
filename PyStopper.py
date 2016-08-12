import random
from tkinter import Tk, Frame, Canvas, Button, Scale, Label, HORIZONTAL


# Starts the tkinter loop thingy and gives it a window to do stuff in.
class TopWindow:

    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack()

        # Creates canvas on which red/green will be drawn
        self.lightarea = Canvas(self.root, width=600, height=400)
        self.lightarea.pack()

        self.is_green = True
        self.is_playing = False

        pad_kwargs = {"padx": 10, "pady": 10}

        self.start_button = Button(self.root, text="Start", command=self.start_playing)
        self.start_button.pack(**pad_kwargs)

        self.stop_button = Button(self.root, text="Stop", command=self.stop_playing)
        self.stop_button.pack(**pad_kwargs)

        self.light_green()

        self.green_time_scale_lable = Label(text="Time Performing (sec)")
        self.green_time_scale_lable.pack()
        self.green_time_scale = Scale(self.root, from_=1, to=30, orient=HORIZONTAL)
        self.green_time_scale.set(15)
        self.green_time_scale.pack()

        self.red_time_scale_lable = Label(text="Time Frozen (sec)")
        self.red_time_scale_lable.pack()
        self.red_time_scale = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.red_time_scale.set(2)
        self.red_time_scale.pack()

    # Draws green square. Draws red square.
    def light_green(self):
        self.lightarea.create_rectangle(20, 20, 581, 381, fill="green", tags="greenlight")
        print("Green square drawn.")

    def light_red(self):
        self.lightarea.create_rectangle(20, 20, 581, 381, fill="red", tags="redlight")
        print("Red square drawn.")

    def toggle_playing(self):
        self.lightarea.delete("all")
        if self.is_green:
            self.is_green = False
            self.light_red()
        else:
            self.is_green = True
            self.light_green()

    # Generates one "cycle" of green and red lights
    def play_single_cycle(self):
        if self.is_playing:
            self.toggle_playing()
            rand_max = (self.green_time_scale.get() if self.is_green else self.red_time_scale.get()) * 1000  # convert to ms
            self.root.after(random.randint(1000, rand_max), self.play_single_cycle)

    def start_playing(self):
        self.is_playing = True
        self.play_single_cycle()

    def stop_playing(self):
        self.is_playing = False

    def run(self):
        self.root.mainloop()

our_window = TopWindow()
our_window.run()
