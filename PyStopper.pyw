import random
try:
    # for Python2
    from Tkinter import Tk, Frame, Canvas, Button, Scale, Label, HORIZONTAL, E, S
except ImportError:
    # for Python3
    from tkinter import Tk, Frame, Canvas, Button, Scale, Label, HORIZONTAL, E, S

# Starts the tkinter loop thingy and gives it a window to do stuff in.
class TopWindow:

    def __init__(self):

        pad_kwargs = {"padx": 0,
                      "pady": 0,
                      "ipadx": 0,
                      "ipady": 0}

        self.root = Tk()
        self.frame = Frame(self.root)

        # Creates canvas on which red/green will be drawn
        self.lightarea = Canvas(self.root, width=600, height=400)

        self.is_green = True
        self.is_playing = False

        self.start_button = Button(self.root, text="Start", command=self.start_playing)

        self.stop_button = Button(self.root, text="Stop", command=self.stop_playing)

        self.light_green()

        self.green_time_scale_lable = Label(text="Time Performing (sec)")
        self.green_time_scale = Scale(self.root, from_=1, to=30, orient=HORIZONTAL)
        self.green_time_scale.set(15)

        self.red_time_scale_lable = Label(text="Time Frozen (sec)")
        self.red_time_scale = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.red_time_scale.set(2)

        self.frame.grid()
        self.lightarea.grid(row=0, column=0, columnspan=4, **pad_kwargs)
        self.start_button.grid(row=1, column=0, **pad_kwargs)
        self.stop_button.grid(row=2, column=0, **pad_kwargs)
        self.green_time_scale_lable.grid(row=1, column=2, sticky= E + S, **pad_kwargs)
        self.green_time_scale.grid(row=1, column=3, **pad_kwargs)
        self.red_time_scale_lable.grid(row=2, column=2, sticky= E + S, **pad_kwargs)
        self.red_time_scale.grid(row=2, column=3, **pad_kwargs)

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
