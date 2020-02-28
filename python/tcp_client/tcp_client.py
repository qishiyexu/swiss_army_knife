# coding: utf8
from socket import *

HOST = '127.0.0.1'
PORT = 2345

ADDR = (HOST, PORT)
BUFSIZE = 1024


class SyncTcpClient:
    
    def run(self, addr):
        client_sock = socket(AF_INET, SOCK_STREAM)
        client_sock.connect(ADDR)

        while True:
            data = input('>')
            if not data:
                break

            data_bytes = bytes(data, encoding = "utf8")
            client_sock.send(data_bytes)
            print ('send!')        

# class AsyncTcpClient:
    
#     def run(self, addr):
#         client_sock = socket(AF_INET, SOCK_STREAM)
#         client_sock.connect(ADDR)
#         client_sock.setblocking(0) 

#         while True:
#             data = input('>')
#             if not data:
#                 break

#             data_bytes = bytes(data, encoding = "utf8")
#             client_sock.send(data_bytes)
#             print ('send!')     

def main():
    client = SyncTcpClient()
    client.run(ADDR)


if __name__== "__main__":
    main()