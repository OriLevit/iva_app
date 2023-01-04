import tkinter
from tkinter import Button


class Btn(Button):
    def __init__(self, root, img1, img2, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.img = tkinter.PhotoImage(file=img1)
        self.img2 = tkinter.PhotoImage(file=img2)

        self['image'] = self.img

        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

    def enter(self, event):
        self.config(image=self.img2)

    def leave(self, event):
        self.config(image=self.img)