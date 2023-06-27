# coding: utf8
from socket import *
import time, datetime

HOST = '127.0.0.1'
PORT = 7890

ADDR = (HOST, PORT)
BUFSIZE = 1024000
SENDSIZE = 10240


class SyncTcpClient:
    
    def run(self, addr):
        client_sock = socket(AF_INET, SOCK_STREAM)
        client_sock.connect(ADDR)

        while True:
            time_start = datetime.datetime.now()
           # data = 'aaaaa'
           # data_bytes = bytearray(data, encoding = "utf8")
            data_bytes = bytearray(SENDSIZE)
            client_sock.send(data_bytes)
            recv_data = client_sock.recv(BUFSIZE)
            time_end = datetime.datetime.now()
            diff = (time_end - time_start).microseconds
            diff_millisec = diff / 1000
            print ("microseconds: %d, milliseconds: %d" % (diff, diff_millisec))        
            time.sleep(1)
   

def main():
    client = SyncTcpClient()
    client.run(ADDR)


if __name__== "__main__":
    main()