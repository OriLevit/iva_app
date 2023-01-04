from tkinter import Entry


class CustomEntry(Entry):
    def __init__(self, root, text, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.bind('<Button-1>', self.click)
        self.configure(justify="center")
        self.insert(0, text)

    # Define a function to clear the content of the text widget
    def click(self, event):
        self.delete(0, len(self.get()))
        self.unbind('<Button-1>')
