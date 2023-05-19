import tkinter as tk
import threading
import socket
from queue import Queue

# Global variables
peer1_queue = Queue()
peer2_queue = Queue()
text_peer1 = None
text_peer2 = None


def start_peer1():
    import peer1


def start_peer2():
    import peer2


def send_message(peer_queue, message):
    peer_queue.put(message)


def update_message_display(text_widget, message):
    text_widget.configure(state='normal')
    text_widget.insert(tk.END, message + '\n')
    text_widget.configure(state='disabled')


def start_peer1_interface():
    global text_peer1

    root = tk.Tk()
    root.title("User 1")

    # Message display area for Peer 1
    text_peer1 = tk.Text(root, state='disabled', height=14, width=50)
    text_peer1.pack()

    # Text input area for Peer 1
    entry_peer1 = tk.Entry(root)
    entry_peer1.pack()

    # Button to send message from Peer 1
    btn_send_peer1 = tk.Button(root, text="Send", command=lambda: send_message(peer1_queue, entry_peer1.get()))
    btn_send_peer1.pack()

    root.mainloop()


def start_peer2_interface():
    global text_peer2

    root = tk.Tk()
    root.title("User 2")

    # Message display area for Peer 2
    text_peer2 = tk.Text(root, state='disabled', height=14, width=50)
    text_peer2.pack()

    # Text input area for Peer 2
    entry_peer2 = tk.Entry(root)
    entry_peer2.pack()

    # Button to send message from Peer 2
    btn_send_peer2 = tk.Button(root, text="Send", command=lambda: send_message(peer2_queue, entry_peer2.get()))
    btn_send_peer2.pack()

    root.mainloop()


def main():
    t1 = threading.Thread(target=start_peer1_interface)
    t1.daemon = True

    t2 = threading.Thread(target=start_peer2_interface)
    t2.daemon = True

    t1.start()
    t2.start()

    while True:
        if not peer1_queue.empty():
            message = peer1_queue.get()
            update_message_display(text_peer2, "Peer 1: " + message)

        if not peer2_queue.empty():
            message = peer2_queue.get()
            update_message_display(text_peer1, "Peer 2: " + message)


if __name__ == "__main__":
    t_main = threading.Thread(target=main)
    t_main.daemon = True
    t_main.start()

    start_peer1()
    start_peer2()
