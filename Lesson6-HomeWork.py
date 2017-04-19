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
# import functools


class CacheCalc:
    # work_time = 0.0

    def __init__(self, cache_limit=50):
        self.cache_dict = {}
        self.sorting_dict = {}
        self.cache_limit = cache_limit
        self.counted = 0
        self.from_cache = 0
        self.work_time = 0

    # def time_of_work(func):
    #     @functools.wraps(func)
    #     def inner(*args, **kwargs):
    #         start_time = time.time()
    #         func(*args, **kwargs)
    #         end_time = time.time()
    #         current_work_time = end_time - start_time
    #         if current_work_time > CacheCalc.work_time:
    #             CacheCalc.work_time = current_work_time
    #         return func
    #     return inner

    # @time_of_work
    def sum(self, *args):
        start_time = time.time()
        sum = 0
        for key in self.cache_dict:
            if args.__eq__(key):
                self.from_cache += 1
                self.sorting_dict[key] += 1
                return self.cache_dict.get(key)
        for numb in args:
            sum += numb
        self.cache(*args, sum=sum)
        self.counted += 1
        self.work_time = time.time() - start_time
        return sum

    def cache(self, *args, sum):
        if len(self.cache_dict) >= self.cache_limit:
            sorted_sorting_dict = sorted(self.sorting_dict, key=self.sorting_dict.get)
            self.cache_dict.pop(sorted_sorting_dict[0])
            self.sorting_dict.pop(sorted_sorting_dict[0])

        self.cache_dict[args] = sum
        self.sorting_dict[args] = 0

    def save_results(self):
        sorted_sorting_dict = sorted(self.sorting_dict, key=self.sorting_dict.get, reverse=True)
        with open('C:/Users/Tanuxxx/PycharmProjects/pythonCourses/temp/lesson6_home_work.txt', 'w') as f:
            f.write(str(sorted_sorting_dict))

    def show_results(self):
        print('Counted: {0}'.format(self.counted))
        print('From cache: {0}'.format(self.from_cache))
        print('Longest time of work: {0}'.format(self.work_time))


calc = CacheCalc(10)
calc.sum(1,2)
calc.sum(*range(1, 1000))
calc.sum(1,2)
calc.sum(2,1)
calc.sum(6,1)
calc.sum(3,5)
calc.sum(2,1)

calc.save_results()
calc.show_results()
