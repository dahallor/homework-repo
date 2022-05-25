import tkinter as tk

def _enter_msg(chatroom, user):
    #TODO: create stuff here
    chatroom.configure(text=user.get())

root = tk.Tk()


left_col = tk.Label(root, text="Chatroom icons here")
chatroom = tk.Label(root, text="Current Chatroom name here")
user = tk.Entry(root)
enter_button = tk.Button(root, text="Enter", command=lambda: _enter_msg(chatroom, user))

left_col.grid(row=0, column = 0)
chatroom.grid(row=0, column = 1)
user.grid(row=1, column = 1)
enter_button.grid(row=1, column=2)


root.mainloop()