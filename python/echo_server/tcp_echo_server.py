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
        except:
            print ('except')
            
        finally:
            print ('connection ', client_address, 'closed')
            connection.close()

def start_just_listen(port):
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('0.0.0.0', port)
    sock.bind(address)
    sock.listen(1)
    
    while True:
        print ('waiting for a connection')
        connection, client_address = sock.accept()
        
        try:
            print ('connection from', client_address)

        except:
            print ('except')
            
        finally:
            print ('connection ', client_address, 'closed')
            connection.close()

def start_write_file(port):
        
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
                    with open('tcp.data', 'a+') as f:
                        f.write(data)
                # else:
                #     break
        except e:
            print ('%s' % str(e)) 
            
        finally:
            print ('connection ', client_address, 'closed')
            connection.close()        


if __name__ == "__main__":
    listen_port = 9100
    if len(sys.argv) > 1:
        listen_port = sys.argv[1]
   # start_echo(listen_port)
    start_write_file(listen_port)
    #start_just_listen(listen_port)
    
    
    
    
    
    