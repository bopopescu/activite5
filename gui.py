import tkinter as tk


class GuiApi (object):
    def __init__(self):
        windows = Tk()
        value = StringVar()
        tick1 = Radiobutton(windows. text="Quel aliment souhaitez-vous remplacer ? ", variable=value, value=1)
        self.tick2 = Radiobutton(self.windows. text="Retrouver mes aliments substitués.", variable=value, value=2)
        self.tick1.pack()
        self.tick2.pack()
