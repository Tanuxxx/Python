#list=[]
#tuple=() - not changing list
#set={}
#dictionary={a:b}

#functiona name contains from letters, numbers, '_'

#docstring function comments - """comment""" after function name
#get function docstring: func.__doc___

#unlimited number of parameters
#* - щператор упаковки
def summarize(*args): #type(args) == tuple - кортеж, неизменяемый список
    result = 0

    for element in args:
        result += element

    return result

print (summarize(1, 2, 3))
print (summarize(1, 2, 3, 144, 567, -678, 4000))

#2 argument are required in order not to allow call summarize from no arguments
def summarize2(first, second, *args):
    result = 0

    for element in (first, second) + args:
        result += element

    return result

#apply unction for collections
xs = {-5, -12, 3}
print (summarize(*xs))

print (summarize(*[-5, 12, 13]))


#key arguments
#get unique elements
#don't use changing types as key argument
def unique(iterable, seen=set()):
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

xs = [1, 1, 2, 3]
print(unique(xs))
#set is already full, its value is saved after previous function eecution
print(unique(xs))
#what this function already has as default values
print(unique.__defaults__)

def unique(iterable, seen=None):
    seen = set(seen or []) #if seen is not None (someting was transfered as parameter) use this value,
                            # if it is None make it []
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

xs = [1, 1, 2, 3]
print(unique(xs))
print(unique(xs))


#visible parameters transfer
#depth is predefined Python operator that says how deep we should watch
def flatten(xs, depth=None):
    pass

#both varients will work
flatten([1, [2], 3], depth =1)
flatten([1, [2], 3], 1)


#* means that there can be any number of parameters
#but actually we can't use this parameters as they will be wrapped up to empty variable without name
def flatten2(xs, *, depth=None):
    pass
#get error as depth wasn't transfered явно and it thinks it still * parameters
#flatten2([1, [2], 3], 2)
#with visible transfer it'll work
flatten2([1, [2], 3], depth=2)


#Use * to get tuple
#Use ** to get dictionary
def run_logger(cmd, **kwargs): #type(kwargs) = dictionary
    if kwargs.get('DEBUG', True): #get vaue by key
        print('Debug mode activated')

run_logger('mysql', limit=42)
run_logger('mysql', **{'verbose': False})
options = {'verbose': False}
run_logger('mysql', **options)

#Распаковка и присваивание
result = []
seen = set()
(result, seen) = [], set()


a, b, c = [1, 2, 3]
a, b, c = {1, 2, 3}
a, b, c = 'abc'

rectangle = (0, 0), (4, 4)
(x1, y1), (x2, y2) = rectangle


#Поменять 2 элемента местами
a = 1
b = 2

a, b = b, a


# first, *rest = range(1, 5) #first=1, rest=everything else
# print(first)
# print(rest)
#
# first, *rest, last = range(1, 5)
# print(first)
# print(rest)
# print(last)
#
# first, *rest, last = [42]
# print(first)
# print(rest)
# print(last)
#
# *_, (first, *rest) = [range(1, 5)] * 5
# print(first)
# print(rest)

print('---------------------')
for a, *b in [range(4), range(2)]:
#first element goes to a, all others go to b
#a,*b = [0, 1, 2, 3], a=1, b=[1,2,3]
#a,*b = [0, 1], a=0, b=1
    print(a)
    print(b)