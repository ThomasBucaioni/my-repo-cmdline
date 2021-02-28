#!/usr/bin/env python3

import socket

hostname = '127.0.0.1'


def send_client_message(s, message):
    s.send(message.encode())
    msg = s.recv(1024)
    return msg.decode()


def get_client_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.getfqdn(hostname)
    port = 9999
    s.connect((host, port))
    return s


def run_client():
    s = get_client_socket()
    # Receive no more than 1024 bytes

    for i in range(5):
        print(send_client_message(s, f'say {i}'))

    print(send_client_message(s, 'say goodnight'))
    print(send_client_message(s, 'say goodnight, Gracie'))

    print(send_client_message(s, 'garbage'))

    print(send_client_message(s, 'increment 5'))
    print(send_client_message(s, 'increment 12345'))

    print(send_client_message(s, 'bye'))

    s.close()


if __name__ == '__main__':
    run_client()
