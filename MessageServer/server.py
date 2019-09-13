#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from chat import Chat
import pickle

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print('%s:%s has connected.' % client_address)
        chat = Chat('Greetings from the cave! Now type your name and press enter!', 'server')
        client.send(pickle.dumps(chat))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = pickle.loads(client.recv(BUFSIZ)).sender
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    chat = Chat(welcome, 'server')
    client.send(pickle.dumps(chat))
    msg = "%s has joined the chat!" % name
    broadcast(msg)
    clients[client] = name

    while True:
        msg = pickle.loads(client.recv(BUFSIZ)).message
        if msg != '{quit}':
            broadcast(msg, name+': ')
        else:
            #client.send(bytes('{quit}', 'utf8'))
            client.close()
            del clients[client]
            broadcast('%s has left the chat.' % name)
            break

def broadcast(msg, prefix=''):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    print(msg)
    p_chat = pickle.dumps(Chat(msg, 'who knows'))
    for sock in clients:
        #message = prefix + msg
        sock.send(p_chat)

clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == '__main__':
    SERVER.listen(5)
    print('Waiting for connection...')
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()