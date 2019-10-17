#!/usr/bin/python
# -*- coding: UTF-8 -*-


import socket
import sys

RECV_CHUNK_SIZE = 1024

def start_echo(port):
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('0.0.0.0', port)
    sock.bind(address)
    sock.listen(1)
    
    while True:
        print ('waiting for a connection')
        connection, client_address = sock.accept()
        
        try:
            print ('connection from', client_address)

            while True:
                data = connection.recv(RECV_CHUNK_SIZE)
                print ('recv data size: %d' % len(data), data)
                if data:
                    connection.sendall(data)
                else:
                    break
        except Exception, e:
            print ('%s' % str(e)) 
            
        finally:
            print ('connection ', client_address, 'closed')
            connection.close()
        

if __name__ == "__main__":
    listen_port = 9876
    if len(sys.argv) > 1:
        listen_port = sys.argv[1]
    start_echo(listen_port)
    
    
    
    
    
    