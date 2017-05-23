import socket

sock = socket.socket()
sock.connect(('localhost', 8888))
sock.send(b'5')

data = sock.recv(1024)
sock.close()

print(data)