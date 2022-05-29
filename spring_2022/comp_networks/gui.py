import tkinter as tk
from client import *


class GUI(Client):
    def __init__(self):
        self.BG_GRAY = "#ABB2B9"
        self.BG_COLOR = "#17202A"
        self.TEXT_COLOR = "#EAECEE"
        self.FONT = "helvetica 14"

    def _layout(self):
        self.root.title("Discourse")
        #self.root.resizable(width=False, height=False)
        self.root.geometry('650x800')

    def _elements(self):
        self.chatroom_name = tk.Label(self.root, text="Current Chatroom name here", bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.chatlog = tk.Label(self.root, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.input_field = tk.Entry(self.root)
        self.enter_button = tk.Button(self.input_field, text="Enter", command=self._enter_msg, bg=self.BG_COLOR, fg=self.TEXT_COLOR)

    def _grid(self):
        self.left_col.grid(row=0, column = 0)
        self.chatroom.grid(row=0, column = 1)
        self.user.grid(row=1, column = 1)
        self.enter_button.grid(row=1, column=2)

    def _enter_msg(self):
        self.chatlog.configure(text=self.user.get())

    def run_GUI(self):
        self.root = tk.Tk()

        self._layout()
        self._elements()
        self._grid()

        self.root.mainloop()

if __name__ == '__main__':
    gui = GUI()
    gui.run_GUI()