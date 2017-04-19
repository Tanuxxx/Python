#Исключения и менеджеры контекста
# try:
# except (ValueError, ArithmeticError):
# except TypeError as e:
#
# except get 2 srguments: expression, возвраающее тип или кортеж типов и опциональное имя

#isinstance(e, expt) - вызывается внутри еxcept для выяснения какая ошибка возникла
#In except instead of expression anything can be - function call or бращение к переменной
# try:
# except type(e):
BaseException #только системные ошибки
Exception #наследоваться лучше от него!!!
AssertionError #лучше не использовать

print(BaseException.__subclasses__())

try:
    1+'42'
except Exception as e:
    caught = e
print(caught.args) #хранит кортеж аргументов, переденных конструктору исключения
print(caught.__traceback__) #содержит информацию о стеке вызовов в момент возникновения исключения

import traceback
traceback.print_tb(caught.__traceback__)

#raise TypeError("type mismatch") #raise exception, его аргументы должны быть наследниками базового класса BaseException
#raise #без аргументов он выкинет последнюю ошибку, а если ее не было, то RuntimeError


try:
    {}
    ["foobar"]
except KeyError as e:
    raise RuntimeError("Ooops!") from e
#Возникло 2 ошибки. Вначале KeyError, а затем уже вторая


import sys
try:
    handle = open("example.txt", "wt")
    try:
        pass
    finally: #will be executed in any case, was except or try
        handle.close()
except IOError as e:
    print(e, file=sys.stderr)


#else will work if no exceptions were cought in try branch
# try:
#     handle = open("example.txt", "wt")
# else:
#     # report.success(handle)
# except IOError as e:
#     print(e, file=sys.stderr)

#Минимизировать размер ветски try
#Стараться указывать наоболее специфичный тип исключения в ветке except

