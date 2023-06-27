import socket


MESSAGE = b'123123'
ADDR = '172.23.119.14'
PORT = 9006


    

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.settimeout(5)
sock.connect((ADDR, PORT))

sock.send(MESSAGE)
recv_data = sock.recv(1024)
print(recv_data)
