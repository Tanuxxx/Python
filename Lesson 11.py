#@property - decorator that makes attribute read only?
# class Connection:
#     @property
#     def get_all_connections(self):
#         return 0
#
# #Descriptor - class that realises protocol and/or property that can be reused
# #Realises from 1 to 3 methods: get, set
# class Descr:
#     def __get__(self, instance, owner):
#         print(instance, owner)
#
#     def __set__(self, instance, value):
#         print(instance, value)
#
#     #for descriptor if del method is called first delete method from descriptor will be used, not build-in del method
#     def __delete__(self, instance):
#         print(instance)
#
#
# class A:
#     attr = Descr()
#
#
# class B(A):
#     pass
#
# print(A.attr)
# print(A().attr)
# print(B.attr)
# print(B().attr)
#
# instance = A()
# instance.attr = 42
# A.attr = 43# - attr will be set to 43 not Descr()any more

#Exists data descriptor that realises all 3 methods or at least get and set and non-data descriptor that realises not all methods

class DescrTest:
    def __init__(self):
        self.arr = []

    def __get__(self, instance, owner):
        self.arr.append(1)
        print(self.arr)


class A1:
    b=DescrTest()

a1=A1()
a1.b
a1.b


class DescrTest2:
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        instance.__dict__[self.label].append(1)
        print(instance.__dict__[self.label])

    def __set__(self, instance, value):
        instance.__dict__[self.label] = value


class A2:
    b=DescrTest2('plus_one')

a2=A2()
a2.b = []
a2.b
a2.b
a2.b

#data = ['a':1
#'a\b':2
#'a\b\c':3
#'d\f':4]

#{name:a, chield:[name:b, chield:[name c, value:6]]}

#T=Tree.collect(data)
#T.as_dict()