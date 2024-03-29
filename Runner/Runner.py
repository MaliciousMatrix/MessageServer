from relay_virtual import RelayVirtual
from relay import RelayState
import uuid
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from chat import Chat
import pickle
def print_something(value):
    print("Value changed to " + str(value))

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            chat = pickle.loads(client_socket.recv(BUFSIZ))
            msg_list.insert(tkinter.END, chat.message)
        except OSError:  # Possibly client has left the chat.
            break

def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    chat = Chat(msg, 'my name')
    my_msg.set("")  # Clears input field.
    client_socket.send(pickle.dumps(chat))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
#my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = 'localhost'
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
input('waiting for input')
print('Creating client...')
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.




if __name__ == '__main__':
    relay = RelayVirtual(uuid.uuid4(), 'Dis Relay') 
    relay.state_changed += print_something
    relay.state = RelayState.CLOSED
    relay.state = RelayState.OPEN
    relay.state = RelayState.CLOSED
    relay.state = RelayState.CLOSED
    relay.toggle()




    


