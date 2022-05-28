import tkinter as tk
import socket
import pdb
import threading
from client import *

HEADER = 64
BODY = 4096
FORMAT = 'UTF-8'


class GUI(Client):
    def __init__(self, client_socket, username):
        super().__init__(client_socket, username)
        self.BG_GRAY = "#edf2f7"
        self.BG_COLOR = "#17202A"
        self.TEXT_COLOR = "#f7faf8"
        self.FONT = "Helvetica 14"
        self.FONT_BOLD = "Helvetica 13 bold"
        self.username = username
        self.own_msg = True

    def _layout(self):
        self.root.title("Discourse")
        #self.root.resizable(width=False, height=False)
        self.root.configure(width=650, height=800, bg=self.BG_COLOR)

        head = tk.Label(self.root, bg=self.BG_COLOR, fg=self.TEXT_COLOR, text="Chatroom Name Here", font=self.FONT, pady=10)
        head.place(relwidth=.85)

        nav_bar = tk.Label(self.root, bg=self.BG_COLOR)
        nav_bar.place(relwidth=.15, relheight=1)

        self.text = tk.Text(self.root, width=20, height=2, bg=self.BG_COLOR, fg=self.TEXT_COLOR, font=self.FONT, padx=5, pady=5)
        self.text.place(relheight=.75, relwidth=.85, rely=.075, relx=.15)
        self.text.configure(cursor="arrow", state=tk.DISABLED)

        scrollbar = tk.Scrollbar(self.text)
        scrollbar.place(relheight=1, relx=.975)
        scrollbar.configure(command=self.text.yview)

        input_widget = tk.Label(self.root, bg=self.BG_GRAY, height=80)
        input_widget.place(relwidth=.85, rely=.825, relx=.15)

        self.input_entry = tk.Entry(input_widget, bg="#2C3E50", fg=self.TEXT_COLOR, font=self.FONT)
        self.input_entry.place(relwidth=.74, relheight=.06, rely=.0075, relx=.01)
        self.input_entry.focus()
        self.input_entry.bind("<Return>", self._enter_msg)

        enter_button = tk.Button(input_widget, text="Enter", font=self.FONT_BOLD, width=20, bg=self.BG_GRAY, command=lambda: self._enter_msg(None, True))
        enter_button.place(relx=.77, rely=.008, relheight=.06, relwidth=.22)

    def _enter_msg(self, event, own_msg):
        if own_msg == True:
            msg = self.input_entry.get()
            self.session_PDU(self.client_socket, self.USERNAME, msg)
            PDU = self._decode_session_PDU()
            msg = PDU[1]
            self._insert_msg(self.username, msg)

    def _insert_msg(self, username, msg):
        if not msg:
            return

        else:

            #pdb.set_trace()
            self.input_entry.delete(0, tk.END)
            formated_msg = f"{self.username}: {msg}\n"
            self.text.configure(state=tk.NORMAL)
            self.text.insert(tk.END, formated_msg)
            self.text.configure(state=tk.DISABLED)

            self.text.see(tk.END)


    def _decode_session_PDU(self):
        try:
            head = self.client_socket.recv(HEADER).decode(FORMAT)
            print(self.client_socket)
            head_len = int(head)
            header = self.client_socket.recv(head_len).decode(FORMAT)
            msg = self.client_socket.recv(BODY).decode(FORMAT)
            msg_len = int(msg)
            message = self.client_socket.recv(BODY).decode(FORMAT)
            print(head, head_len)
            print(msg, msg_len)
            PDU = [header, message]
        except Exception:
            return None
        return PDU

    def _update(self):
        print("in update function")
        PDU = self._decode_session_PDU()
        print(PDU)
        if PDU != None:
            self._insert_msg(PDU[0], PDU[1])
        self._update()

    def run_GUI(self):
        self.root = tk.Tk()

        self._layout()
        check_msg_thread = threading.Thread(target=self._update)
        check_msg_thread.start()
        print("main thread")

        self.root.mainloop()
        check_msg_thread.join()
        #Put disconnect header code here

if __name__ == '__main__':
    gui = GUI("debugman")
    gui.run_GUI()