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
        self.chatroom_name_frame = tk.Frame(self.root, bd=2, width=645, height=100, relief="groove")
        self.chatroom_name_label = tk.Label(self.chatroom_name_frame, text="It's working")
        
        self.chatlog_frame = tk.Frame(self.root, bd=2, width=645, height=550, relief="groove", bg="white")
        self.chatlog_label = tk.Label(self.chatlog_frame, text="It's working")

        self.input_frame = tk.Frame(self.root, bd=2, width=645, height=150, relief="groove")
        #self.input_label = tk.Label(self.input_frame)
        self.input_field = tk.Entry(self.input_frame)
        self.enter_button = tk.Button(self.input_frame, text="Enter", command=self._enter_msg, bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        

    def _grid(self):
        self.chatroom_name_label.place(relx=.5, rely=.5, anchor="c")
        self.chatroom_name_frame.pack()

        self.chatlog_label.place(relx=.01, anchor="nw")
        self.chatlog_frame.pack()

        #self.input_label.place(anchor="c")
        self.input_frame.pack()
        self.input_field.place(width=620, height=145, anchor="w")
        self.enter_button.place(anchor="e")

        
        

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