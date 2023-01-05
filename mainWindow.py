import tkinter

from custom_classes import CustomWindow

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720


class MainWindow(CustomWindow.Window):
    def __init__(self,username):
        super().__init__()
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.center_on_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.user = username

    def add_widgets(self):
        temp_frame = tkinter.Frame(self, width=180, height=720, background="#d1abc1")
        temp_frame.place(x=1080, y=0)
