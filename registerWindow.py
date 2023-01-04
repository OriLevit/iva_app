import hashlib
import tkinter
from custom_classes import CustomWindow, button, CustomEntry
import database_interaction
import mainWindow

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


class RegisterWindow(CustomWindow.Window):
    def __init__(self):
        super().__init__()

    def add_widgets(self):
        # region main frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        main_frame = tkinter.Frame(master=self)
        main_frame.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
        main_frame.config(bg="#2b2b2b")
        main_frame.grid_rowconfigure(4, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        # endregion

        # region labels
        title_label = tkinter.Label(master=main_frame, text="Register", font=("Ariel", 18, "bold"))
        title_label.grid(column=1, row=0, pady=15)
        title_label.config(bg="#2b2b2b", fg="white")

        already_exists_label = tkinter.Label(master=main_frame, text="Username taken!", font=("Ariel", 10, "bold"))
        already_exists_label.grid(column=1, row=3, pady=0)
        already_exists_label.config(bg="#2b2b2b", fg="red")
        already_exists_label.grid_remove()
        # endregion

        # region entries
        username_entry = CustomEntry.CustomEntry(main_frame, "Username", font=("Verdana", 12))
        username_entry.grid(column=1, row=1, pady=10)

        password_entry = CustomEntry.CustomEntry(main_frame, "Password", show="*", font=("Verdana", 12))
        password_entry.grid(column=1, row=2, pady=5)

        # endregion

        def submit_register(event=None):
            usr = username_entry.get()
            if database_interaction.does_username_exist(usr):
                already_exists_label.grid()
            else:
                hash_object = hashlib.sha256(password_entry.get().encode())
                hashed_password = hash_object.hexdigest()
                database_interaction.add_user(usr, hashed_password)
                already_exists_label.grid_remove()
                self.destroy()
                mainWindow.MainWindow()

        # region buttons
        register_button = button.Btn(root=main_frame,
                                     img1="images/register_button.png",
                                     img2="images/register_button_pressed.png",
                                     command=submit_register)

        register_button.configure(bg="#2b2b2b", activebackground="#2b2b2b", borderwidth=0)
        register_button.grid(column=1, row=4, pady=10)
        # endregion

        self.bind('<Return>', submit_register)
