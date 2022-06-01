import tkinter as tk
import threading
from client import *


class GUI:
    def __init__(self, client):
        self.BG_GRAY = "#ABB2B9"
        self.BG_COLOR = "#17202A"
        self.TEXT_COLOR = "#EAECEE"
        self.FONT = "helvetica 14"
        self.client = client
        self.current_chatroom = "&general"
        self.queue = []

    def _layout(self):
        self.root.title("Discourse")
        self.root.resizable(width=False, height=False)
        self.root.geometry('650x800')

    def _elements(self, v, code, client_socket, PDU):
        self.chatroom_name_frame = tk.Frame(self.root, bd=2, width=645, height=100, relief="groove", bg=self.BG_COLOR)
        self.chatroom_name_label = tk.Label(self.chatroom_name_frame, text="&general", bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        
        self.chatlog_frame = tk.Frame(self.root, bd=2, width=645, height=650, relief="groove", bg=self.BG_COLOR)
        self.chatlog_label = tk.Text(self.chatlog_frame)

        self.input_frame = tk.Frame(self.root, bd=2, width=645, height=150, relief="groove")
        #self.input_label = tk.Label(self.input_frame)
        self.input_field = tk.Entry(self.input_frame, bg=self.BG_GRAY, fg=self.TEXT_COLOR)
        self.enter_button = tk.Button(self.input_frame, text="Enter", command=lambda: self._enter_own_msg(v, code, client_socket, PDU), bg=self.BG_COLOR, fg=self.TEXT_COLOR, pady=10)
        

    def _grid(self):
        self.chatroom_name_label.place(relx=.5, rely=.5, anchor="c")
        self.chatroom_name_frame.pack()

        self.chatlog_label.place(relx=.01, anchor="nw")
        self.chatlog_frame.pack()

        #self.input_label.place(anchor="c")
        self.input_frame.pack()
        self.input_field.place(width=600, rely=.5, anchor="w")
        self.input_field.focus()
        #self.input_field.bind("<Return>", self._enter_own_msg)
        self.enter_button.place(relx=1, rely=.5, width=45, anchor="e")

    def _insert_into_chatlog(self, formated_msg):
        self.chatlog_label.configure(state=tk.NORMAL)
        self.chatlog_label.insert(tk.END, formated_msg)
        self.chatlog_label.configure(state=tk.DISABLED)
        self.chatlog_label.see(tk.END)
        
    def _enter_own_msg(self, v, code, client_socket, PDU):
        #self.chatlog_label.configure(text=self.input_field.get())
        msg = self.input_field.get()
        self.input_field.delete(0, tk.END)
        formated_msg = f"{self.client.user}: {msg}\n"
        self._insert_into_chatlog(formated_msg)
        PDU[1] = self.current_chatroom
        self.client._encode_session_PDU(v, code, client_socket, PDU, msg)
        if int(PDU[0]) == code.actions["Exit"]:
            self.root.destroy()


    def _enter_others_msg(self, PDU, msg):
        user = PDU[2]
        chat = PDU[1]
        if chat == self.current_chatroom:
            formated_msg = f"{user}: {msg}\n"
            self._insert_into_chatlog(formated_msg)

    def _load_chatlog(self, head, msgs):
        self.current_chatroom=head[1]
        self.chatroom_name_label.configure(text=head[1])
        self.chatlog_label.configure(state=tk.NORMAL)
        self.chatlog_label.delete('1.0', tk.END)
        self._insert_into_chatlog(msgs)

    def rec_loop(self, client_socket, PDU):
        while True:
            PDU = self.client._decode_session_PDU(client_socket)
            PDU_head = PDU[0].split(";")
            PDU_body = PDU[1]
            if PDU_head[2] != self.client.user:
                if int(PDU_head[0]) != 34:
                    self._enter_others_msg(PDU_head, PDU_body)
            if PDU_head[2] == self.client.user:
                if int(PDU_head[0]) == 50:
                    self.root.destroy()
                if int(PDU_head[0]) == 34:
                    self._load_chatlog(PDU_head, PDU_body)
            PDU = PDU_head
            print(f"rec loop: {PDU} {PDU_body}")


    def run_GUI(self, v, code, PDU, client_socket):
        self.root = tk.Tk()

        self._layout()
        self._elements(v, code, client_socket, PDU)
        self._grid()
        rec_thread = threading.Thread(target=self.rec_loop, args = (client_socket, PDU))
        rec_thread.start()

        self.root.mainloop()
        pdb.set_trace()
        rec_thread.join()

if __name__ == '__main__':
    c = Client()
    gui = GUI(c)
    gui.run_GUI()