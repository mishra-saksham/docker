import pickle
import os 
import sys 
import time 
import socket
import auth 
import socket

HOST = 'localhost'  # The host name or IP address to bind the socket to
PORT = 6000         # The port number to listen on

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
sock.bind((HOST, PORT))

# Listen for incoming connections
sock.listen()

# Accept incoming connections and handle them in a loop
while True:
    # Wait for a client connection
    conn, addr = sock.accept()

    # Handle the connection
    print('Connected by', addr)
    data = conn.recv(1024)  # Receive up to 1024 bytes of data from the client
    # Process the received data here
    conn.sendall(b'Hello, world!')  # Send a response back to the client

    # Close the connection
    conn.close()
    sock.close()
