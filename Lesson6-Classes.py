class Counter:
    """I count. That is all"""
    # all classes inherited from class Object
    all_counters = [] #атрибут класса
    _private_attribute = [] #интерпретатор ничего с этим не сделает, это для разработчиков
    __very_private_attribute = [] #интерпретатор Python сделает атрибуты, начинающиеся с двух подчеркиваний условно невидимым

    def __init__(self, initial=0):
        self.value = initial # аттрибут экземпляра
        Counter.all_counters.append(self)

    def increment(self):
        """I increase value"""
        self.value += 1

    def decrement(self):
        """I decrease value"""
        self.value -= 1

    def get(self):
        return self.value

c = Counter(42)
c.increment()
print(c.get())
c.decrement()
print(c.get())
print(Counter.all_counters)
#__dict__ dictionary with all class arguments
print(Counter.__dict__)
print(c.__class__)
print(Counter.__class__)


#Наследование
class Counter1:
    def __init__(self, initial=0):
        self.value = initial


class OtherCounter(Counter1):
    def __init__(self, initial = 0):
        self.initial = initial
        super().__init__(initial) #вызов метода родительского класса

    def get(self):
        return self.value

oc = OtherCounter()
print(vars(oc))

#---------------------------

class User:
    def save(self):
        pass


class UserA(User):
    def save(self):
        #do some changes
        super().save()

#---------------------------

class Animal:
    def voice(self):
        return "voice"


class Cat(Animal):
    def voice(self):
        return "{0} {1}".format("myau", super().voice())

cat_barsik = Cat()
print(cat_barsik.voice())


#-----------Множественное наследование--------------
class A:
    def f(self):
        print("A.f")

class B:
    def f(self):
        print("B.f")

class C(A, B):
    pass

#Алгоритм MRO (method resolution order)- линиализация дерева наследования

print(C.mro())
C().f()

#__getattr__ вызывается при попытке прочитать значение несуществующего атрибута


#__call__ позволяет "вызывать" экземпляры классов, имитируя интерфейс функций
class Cat:
    def __call__(self):
        print("Myau")

Cat()()

#__repr__ and __str__
class Counter2:
    def __init__(self, initial=0):
        self.value = initial

    def __repr__(self):
        return "Counter({})".format(self.value)

    def __str__(self):
        return "Counted to {}".format(self.value)

c=Counter2(42)
print(c)


#-----------------------

class Test:
    @classmethod #чаще всего используется как расширение фабрики
    def a(cls):
        print("A")

    @staticmethod
    def b():
        print("B")

Test.b()
Test.a()
Test().a()
Test().b()


#------------------------
class Calc:
    def __init__(self):
        self.results = []

    def sum(self, numb1, numb2):
        sum = numb1 + numb2
        self.results.append(sum)
        return sum

    def diff(self, numb1, numb2):
        diff = numb1 - numb2
        self.results.append(diff)
        return diff

    def get_results(self):
        return self.results[-5:] #det 5 last elements from the list


class mCalc(Calc):
    def sum(self, numb1, numb2):
        if (numb1 > numb2):
            return super().sum(numb1, numb2)
        else:
            return "Sorry, can't perform. First number should be greater then second"

c1 = Calc()
print(c1.sum(3, 2))
print(c1.sum(4, 5))
print(c1.sum(4, 5))
print(c1.diff(4, 5))
print(c1.diff(4, 5))
print(c1.diff(4, 5))
print(c1.get_results())

mc=mCalc()
print(mc.sum(4,3))
print(mc.sum(1,3))

