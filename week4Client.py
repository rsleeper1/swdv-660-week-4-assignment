import socket

host = '127.0.0.1'
port = 9500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b"Hello")
    s.sendall(b"Test")
    data = s.recv(1024)

print('Received', repr(data))
