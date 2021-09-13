#!/usr/bin/env python3
import socket, sys
from multiprocessing import Pool

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHOST: www.google.com\r\n\r\n"

def connect(addr):
    try:
        # Create socket, connect, send and recieve, the shutdown
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_RDWR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    
    except Exception as e:
        print(e)
    finally:
        # Close the socket
        s.close()
def main():
    address = [(HOST, PORT)]
    with Pool() as p:
        p.map(connect, address * 2)

if __name__ == "__main__":
    main()

