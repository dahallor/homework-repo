import tkinter as tk


class GUI:
    def __init__(self):
        self.BG_GRAY = "#ABB2B9"
        self.BG_COLOR = "#17202A"
        self.TEXT_COLOR = "#EAECEE"
        self.FONT = "helvetica 14"

    def _layout(self):
        self.root.title("Chatroom Name Here")
        #self.root.resizable(width=False, height=False)
        self.root.configure(width=400, height=500, bg=self.BG_COLOR)

    def _elements(self):
        self.left_col = tk.LabelFrame(self.root, text="Chatroom icons here", bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.chatroom = tk.LabelFrame(self.root, text="Current Chatroom name here", bg=self.BG_COLOR, fg=self.TEXT_COLOR, padx=400, pady=550)
        self.user = tk.Entry(self.root)
        self.enter_button = tk.Button(self.root, text="Enter", command=self._enter_msg, bg=self.BG_COLOR, fg=self.TEXT_COLOR)

    def _grid(self):
        self.left_col.grid(row=0, column = 0)
        self.chatroom.grid(row=0, column = 1)
        self.user.grid(row=1, column = 1)
        self.enter_button.grid(row=1, column=2)

    def _enter_msg(self):
        self.chatroom.configure(text=self.user.get())

    def run_GUI(self):
        self.root = tk.Tk()

        self._layout()
        self._elements()
        self._grid()

        self.root.mainloop()

if __name__ == '__main__':
    gui = GUI()
    gui.run_GUI()