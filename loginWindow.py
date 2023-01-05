import tkinter
from custom_classes import CustomWindow, button, CustomEntry
import mainWindow
import registerWindow
import database_interaction
import hashlib

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


class LoginWindow(CustomWindow.Window):
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
        title_label = tkinter.Label(master=main_frame, text="Login", font=("Ariel", 18, "bold"))
        title_label.grid(column=1, row=0, pady=15)
        title_label.config(bg="#2b2b2b", fg="white")

        wrong_credentials_label = tkinter.Label(master=main_frame, text="Username/Password incorrect!",
                                                font=("Ariel", 10, "bold"))
        wrong_credentials_label.grid(column=1, row=3, pady=10)
        wrong_credentials_label.config(bg="#2b2b2b", fg="red")
        wrong_credentials_label.grid_remove()
        # endregion

        # region entries
        username_entry = CustomEntry.CustomEntry(main_frame, "Username", font=("Verdana", 12))
        username_entry.grid(column=1, row=1, pady=10)

        password_entry = CustomEntry.CustomEntry(main_frame, "Password", show="*", font=("Verdana", 12))
        password_entry.grid(column=1, row=2, pady=5)

        # endregion

        # endregion

        def submit_login(event=None):
            usr = username_entry.get()
            hash_object = hashlib.sha256(password_entry.get().encode())
            hashed_password = hash_object.hexdigest()

            if database_interaction.check_login(usr, hashed_password):
                print("Logging in...")
                self.destroy()
                mainWindow.MainWindow(usr)
            else:
                # TODO make a difference between wrong credentials and non existent user
                wrong_credentials_label.grid()

        def register():
            self.destroy()
            registerWindow.RegisterWindow()

        # region buttons
        login_button = button.Btn(root=main_frame,
                                  img1="images/login_button.png",
                                  img2="images/login_button_pressed.png")
        login_button.configure(bg="#2b2b2b", activebackground="#2b2b2b", borderwidth=0, command=submit_login)
        login_button.grid(column=1, row=5)

        register_button = button.Btn(root=main_frame,
                                     img1="images/register_button.png",
                                     img2="images/register_button_pressed.png",
                                     command=register)

        register_button.configure(bg="#2b2b2b", activebackground="#2b2b2b", borderwidth=0)
        register_button.grid(column=1, row=6, pady=15)
        # endregion

        self.bind('<Return>', submit_login)
