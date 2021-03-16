#!/usr/bin/env python3

import socket
import pickle

hostname = '127.0.0.1'


def get_client_connection():
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    host = socket.getfqdn(hostname)
    port = 9999
    serversocket.bind((host, port))

    serversocket.listen()
    print("Ready to accept connection")

    clientsocket, addr = serversocket.accept()
    return clientsocket


def run_server():
    clientsocket = get_client_connection()

    actions = {
        'numbers': lambda: list(range(10)),
        'reverse_word': lambda word: word[::-1],
        'unicode_map': lambda word: {letter: ord(letter) for letter in word}
    }

    while True:
        client_message = clientsocket.recv(1024).decode()

        if not client_message:
            break

        print(f"Received: '{client_message}'")

        command, *args = client_message.split()

        if command == 'bye':
            break
        elif command not in actions:
            clientsocket.send(pickle.dumps(
                f"Unknown command '{client_message}'"))
        else:
            clientsocket.send(pickle.dumps(actions[command](*args)))

    clientsocket.close()


if __name__ == '__main__':
    run_server()
    
