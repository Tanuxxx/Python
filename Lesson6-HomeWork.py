#Он умеет суммировать значения, но он должен запоминать, что уже суммировал. Он умеет сохранять результаты и показывать
#Запоминает 100 результатов. SaveResults записывает результаты в файл. Во время создания задавать количество элементов, которые могут храниться в кэше
#Новые записи удаляют старые
# class CacheCalc:
#     pass
#
# L=CacheCalc(cache_limit)
# L.sum() #sum может принимат. Суммирует неограниченное количество элементов
# L.save_results() #cохранять результаты кэша в файл. Сохранит dictionary, отсортированные по частоте использования кэша
# L.show_resuls() #показать сколько раз он реально считал, а сколько забирал результаты из кэша, и самое длинное выполнение функции sum
# L.longest_run()#самое долгое выполнение функции

import time
import functools

class CacheCalc:
    def __init__(self, cache_limit):
        self.cache_dict = {}
        self.cache_limit = cache_limit
        self.work_time = 0

    def time_of_work(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()

            time_of_work = end_time - start_time
            if time_of_work > self.work_time:
                self.work_time = time_of_work
            return func
        return inner


    @time_of_work
    def sum(self, *args):
        sum = 0
        for key in self.cache_dict:
            if args.__eq__(key):
                print('Found in cache')
                return self.cache_dict.get(key)

        for numb in args:
            sum += numb
        self.cache(*args, sum = sum)
        print(self.cache_dict)
        return sum

    def cache(self, *args, sum):
        if len(self.cache_dict) < self.cache_limit:
            self.cache_dict[args] = sum
        else:
            pass

    def save_results(self):
        print(self.work_time)

    def show_results(self):
        pass

    def longest_run(self):
        pass

#help(dict)
# help(dict)

calc = CacheCalc(100)
calc.sum(1,2)
calc.sum(1,9)
calc.sum(1,2)
calc.sum(2,1)

calc.work_time()