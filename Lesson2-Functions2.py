import dis
print(dis.dis("first, *rest, last = ('a', 'b', 'c')"))
print('-----')
print(dis.dis("first, *rest, last = ['a', 'b', 'c']"))


def wrapper():
    def local_function(value):
        return value
    return local_function

f = wrapper()
print(f(42))


def function():
    print(value)
for value in range(4):
    function()

value = 42
def function1():
    value += 1
    return value
function()


def modify_data(file_obj=None):

    def get_obj():
        return file_obj

    def set_obj(update):
        nonlocal file_obj #get it higher and change it, not take it in its function visible area
        file_obj = update

    return get_obj, set_obj

get_obj, set_obj = modify_data()
set_obj(42)
print(get_obj)


#Anonymous functions
#map
print(set(map(lambda x: x%7, [1, 9, 16, -1, 2, 5])))
#В map можно переавать любое количество последовательностей, но длина результата будет равна длине минимальной последовательности
#х из массива первого, n берется из range. т.к. х только 2, то длина будет равна двум
print(list(map(lambda x, n: x**n, [2,3], range(1,8))))

#filter
print(filter(lambda x: x%2!=0, range(10)))

print(list(filter(lambda x:x%2!=0, range(10))))

# xs = [0, None, [], {}, set(), "", 42]
# list(filter(xs))

#zip
print(list(zip("abc", range(3), [42j, 42j, 42j])))
#Длина результата будет равна длине минимальной последовательности
print(list(zip("abc", range(10))))

#Генераторы списков множеств и словарей
print([x ** 2 for x in range(10) if x % 2 == 1])
#анонимные функции работают быстрее в данном случае, чем for

