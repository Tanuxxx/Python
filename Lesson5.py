import functools


x=[1, -2, 3, -50, 40, -90]
result = filter(lambda x: x>0, x)


# возвести все положительные элементы последовательности в квадрат
def positive_in_square(el):
    if el>0:
        return el**2
    else:
        return el


print(list(map(positive_in_square, x)))
# map принимает 2 параметра: func и *iterables.
# map makes an iterator that computes the function using arguments from each of the iterables.


def make_p(func):
    functools.wraps(func)

    def wrapper(*args):
        result = '{0} {1} {2}'.format('<p>', func(*args), '</p>')
        return result
    return wrapper


def make_strong(func):
    functools.wraps(func)

    def wrapper(*args):
        result = '{0} {1} {2}'.format('<strong>', func(*args), '</strong>')
        return result
    return wrapper


#декоратор инициалиируется один раз для каждой новой переданой ему функции. После того как он инициализирован вызывается только wrapper
def check_count(func):
    functools.wraps(func)

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(wrapper.calls)
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@check_count
@make_strong
@make_p
def create_text(text):
    return text


# print(create_text('Hello world!'))
# print(create_text('Hello world!'))
# print(create_text('Hello world!'))


# Генераторы
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in numbers:
#     print(num)

[num for num in numbers]
[num for num in numbers if num>0]

divide_by_two = [str(num) for num in numbers if num%2==0]
for num in divide_by_two:
    print(num)

#Генератор инициализирует по одному элементу, а не все элементы списка сразу
#Генератор может быть и dictionary {}