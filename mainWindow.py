import tkinter

from custom_classes import CustomWindow

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720


class MainWindow(CustomWindow.Window):
    def __init__(self):
        super().__init__()
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.center_on_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

    def add_widgets(self):
        # temp_frame = tkinter.Frame(self, width=180, height=720, background="#7a7a7a")
        # temp_frame.place(x=1080, y=0)
        #
        # def slide_in(event):
        #     x = temp_frame.winfo_x()
        #     final_x = (1080 - 150)
        #     if x > final_x:
        #         temp_frame.place(x=x - 80)
        #         self.after(50, lambda: slide_in(event))
        #         self.bind('<space>', slide_out)
        #
        # def slide_out(event):
        #     x = temp_frame.winfo_x()
        #     final_x = 1080
        #     if x < final_x:
        #         temp_frame.place(x=x + 50)
        #         self.after(50, lambda: slide_out(event))
        #         self.bind('<space>', slide_in)
        #
        # self.bind('<space>', slide_in)
        pass
