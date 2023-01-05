import tkinter


class Window(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.center_on_screen()
        self.add_basics()

    def center_on_screen(self, SCREEN_WIDTH=300, SCREEN_HEIGHT=300):
        # get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (SCREEN_WIDTH / 2)
        y = (screen_height / 2) - (SCREEN_HEIGHT / 2)
        self.geometry('%dx%d+%d+%d' % (SCREEN_WIDTH, SCREEN_HEIGHT, x, y))

    def add_widgets(self,**kwargs):
        pass

    def add_basics(self):
        self.title("IVA - APP")
        self.configure(background="#242424")
        self.iconbitmap("images/volleyball.ico")