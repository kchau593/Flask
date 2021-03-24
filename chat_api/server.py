#chat application demo with a server and multiple clients 
import socket #how to connect to multiple clients
import select #this is how python talks to the I/O on different OS's (Mac, Linux, Windows)

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)