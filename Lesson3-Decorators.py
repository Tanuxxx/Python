#Decorator is the wrapper function
# @trace
# def foo(x):
#     return 42
#
# def foo(x):
#     return 42
# foo = trace(foo)

#sys.stdout
#sys.stderror

#functools module
#@functools.wraps()

#Декоратор может быть параметризированным. Если параметризированный декоратор вызывается со скобками, то он считается параметризированным,
# если декоратор вызывается без скобок, то он будет считаться не параметризированным. Пареметризированный декоратов требует еще одного уровня вложенности.
# Верхняя функция в качестве параметров принимает параметры декоратора, следующая - саму функция, слудеющая - реализует логику декоратора.

import functools

#Wrapper
def profiled(func):
    @functools.wraps(func) #все параметры декорируемой функции присваиваются ф-ции обертке, чтобы они не потерялись
    def inner(*args, **kwargs):
        inner.ncalls += 1 #Функция - объект. У объекта создается переменная
        #print(func.__name__)
        return func(*args, **kwargs)

    inner.ncalls = 0 #Значение переменной для каждой функции, переданной в декоратор будет свое
    inner.func_name = func.__name__
    return inner


@profiled
def dummy(x):
    return x

dummy(2)
dummy(3)

print(dummy.ncalls, dummy.func_name)


#Decorator is called only once during first fuction call
def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
    inner.called = False
    return inner

@once
def initialaze_settings():
    print("Settings initialazed!")

initialaze_settings()
initialaze_settings()


def sandwitch(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('bread')
        func(*args, **kwargs)
        print('bread')
    return inner

@sandwitch
def meat_function():
    print('meat')

meat_function()

#Кеширование
def memorized(func):
    cache = {}
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner

@memorized
def sum(a,b):
    return a+b

print(sum(3,2))

#Контрактное программирование
#Пре и пост условия с параметрами

#Встроенные декораторы - functools.lru_cache(maxsize=64)
#functools.singledispatch - сериализация объекта в компактное строковое представление


#bamchmark декотратор, который меряет сколько секунд проработала функция из предыдущего примера
#singledispatcher, функция для сортировки диктионари. Функция должна принимать на вход только диктионари, строки и что-то еще