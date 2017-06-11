#Создать веб сервер на сокетах (встроенная библиотека socket)
#Состоит из одной функции, которая считает ряд чисел Фибоначчи
#Функция будет работать в этом сервере. Подключаемся к серверу, пишем там число, он ситает значение

#Протестировать сервис на производительность. Закидать его реквестами и посмотреть, сколько реквестов он выдержит в секунду

#После этого переделать метод на генераторы, и посмотреть как изменится производительность

#2 000 реквестов в секунду с двух подключений

#Дэвид Бизли - соотв. лекция

#https://www.youtube.com/watch?v=ys8lW8eQaJQ

import socket

HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

def get_fibonachy(number):
    a = 0
    b = 1
    for __ in range(number):
        a, b = b, a + b
    return a

#Create socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print ('Failed to create socket')

print ('Socket Created')

#Bind socket
try:
    s.bind((socket.gethostname(), PORT))
except socket.error:
    print ('Bind failed')

print ('Socket bind complete')

#Start listening on socket
s.listen(1)
print('Socket now listening')

# now keep talking with the client
# wait to accept a connection - blocking call
conn, addr = s.accept()

# display client information
print('Connected with ' + addr[0] + ':' + str(addr[1]))

# now keep talking with the client
number = conn.recv(1024)
conn.send(get_fibonachy(number))

conn.close()
s.close()
