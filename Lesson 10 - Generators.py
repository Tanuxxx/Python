def g():
    try:
        yield 42
    except Exception as e:
        yield e

gen = g()
next(gen)
gen.throw(ValueError, "something is wrong")#raises error in the place where generator stopped execution and returns next generator value

#Method close raises special exception - GeneratorExit

#Сопрограмма - програма, кот. может иметь больше одной точки входа

#yield from - allows to delegate execution to another generator = await
def chain(*iterables):
    for iterable in iterables:
        yield from iterable


def f():
    yield 42
    return []

def g1():
    res = yield from f()
    print("Got {!r}".format(res))

gen = g()
print(next(gen))
print(next(gen, None))


#Context manager
from contextlib import contextmanager
import os

@contextmanager
def cd(path):
    old_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_path)

#Itertools module
#islice

from itertools import islice

def drop(array, n):
    return list(islice(array, n, None))

print(drop([6,8,9,0,6,5,4], 5))