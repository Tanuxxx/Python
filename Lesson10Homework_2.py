import socket

def get_fibonachy(number):
    a = 0
    b = 1
    for __ in range(number):
        a, b = b, a + b
    return a
sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    r = get_fibonachy(int(data))
    conn.send(str.encode(str(r)))

conn.close()