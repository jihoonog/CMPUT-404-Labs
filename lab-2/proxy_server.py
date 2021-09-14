#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process

#define address & buffer size
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 4096

# get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

# Handle the client's request
def handle_request(conn, remote_conn):
    from_client_data = conn.recv(BUFFER_SIZE)
    remote_conn.sendall(from_client_data)
    from_remote_full_data = b""
    while True:
        data = remote_conn.recv(BUFFER_SIZE)
        if not data:
            break
        from_remote_full_data += data
    conn.sendall(from_remote_full_data)
    remote_conn.close()

def main():
    extern_host = "www.google.com"
    extern_port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(2)

        while True:
            conn, addr = proxy_start.accept()
            print("Connected by", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                remote_ip = get_remote_ip(extern_host)

                proxy_end.connect((remote_ip, extern_port))

                p = Process(target=handle_request, args=(conn, proxy_end))
                p.daemon = True
                p.start()
                print("started process ", p)

            conn.close()
if __name__ == "__main__":
    main()
