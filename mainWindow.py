import tkinter

from custom_classes import CustomWindow

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720


class MainWindow(CustomWindow.Window):
    def __init__(self, username):
        super().__init__()
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.center_on_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.configure(background="#525050")
        self.add_widgets(username)
        self.resizable(False,False)

    def add_widgets(self, username):
        menu_frame = tkinter.Frame(self, width=200, height=720, background="#c2a199")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        menu_frame.grid(column=4, row=0)

        main_frame = tkinter.Frame(self, width=(1080 - 200), height=720, background="#525050")
        main_frame.grid(column=0, row=0, columnspan=4, rowspan=4)
        main_frame.grid_propagate(False)
        # for i in range(3):
        #     main_frame.columnconfigure(i, weight=1)

        main_frame.rowconfigure(1, weight=1)

        title_label = tkinter.Label(master=main_frame, text=f"Welcome {username}!")
        title_label.grid(column=2, row=1, pady=40)
        title_label.config(bg="#525050", fg="white", font=("Ariel", 18, "bold"))

        disclaimer_label = tkinter.Label(master=main_frame, text="הנתונים מעודכנים לפי אתר איגוד הכדורעף* ")
        disclaimer_label.grid(column=0, row=0)
        disclaimer_label.config(bg="#525050", fg="white", font=("Ariel", 8, "bold"))

        leaderboard_frame = tkinter.Frame(main_frame, width=250, height=450, background="#c4d171")
        leaderboard_frame.grid(column=2, row=2, padx=20)
        leaderboard_frame.grid_propagate(False)
        leaderboard_frame.rowconfigure(1, weight=1)
        leaderboard_frame.columnconfigure(1, weight=1)

        leaderboard_title = tkinter.Label(master=leaderboard_frame, text="טבלת ליגה")
        leaderboard_title.config(bg="#c4d171", fg="white", font=("Ariel", 14, "bold"))
        leaderboard_title.grid(row=0, column=1, pady=10)

        upcoming_frame = tkinter.Frame(main_frame, width=250, height=450, background="#a638b5")
        upcoming_frame.grid(column=1, row=2, padx=20)
        upcoming_frame.grid_propagate(False)
        upcoming_frame.rowconfigure(1, weight=1)
        upcoming_frame.columnconfigure(1, weight=1)

        upcoming_title = tkinter.Label(master=upcoming_frame, text="משחקים קרובים")
        upcoming_title.config(bg="#a638b5", fg="white", font=("Ariel", 14, "bold"))
        upcoming_title.grid(row=0, column=1, pady=10)

        previous_frame = tkinter.Frame(main_frame, width=250, height=450, background="#911f2e")
        previous_frame.grid(column=0, row=2, padx=20)
        previous_frame.grid_propagate(False)
        previous_frame.rowconfigure(1, weight=1)
        previous_frame.columnconfigure(1, weight=1)

        previous_title = tkinter.Label(master=previous_frame, text="משחקים אחרונים")
        previous_title.config(bg="#911f2e", fg="white", font=("Ariel", 14, "bold"))
        previous_title.grid(row=0, column=1, pady=10)
