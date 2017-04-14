import collections
import functools
import time


def work_time(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time-start_time)
        return func(*args, **kwargs)
    return inner


@work_time
def most_common_words(limit):
    """
    Get the list of most common errors

    :limit: number of errors to get
    """
    with open('C:/Users/Tanuxxx/PycharmProjects/pythonCourses/temp/python_home_work.txt') as f:
        error_list = f.read().split()

    errors_counter = collections.Counter(error_list).most_common(limit)

    return list(map(lambda value: value[0], errors_counter))


@work_time
def most_common_words2(limit):
    """
    Get the list of most common errors

    :limit: number of errors to get
    """
    with open('C:/Users/Tanuxxx/PycharmProjects/pythonCourses/temp/python_home_work.txt') as f:
        error_list = f.read().split()

    error_list_counted = set()
    for error in error_list:
        counter = 0
        for counted_error in error_list:
            if error.__eq__(counted_error):
                counter += 1
        error_list_counted.add((counter, error))

    error_list_counted_sorted = sorted(error_list_counted, key=lambda tup: tup[0], reverse=True)

    return list(map(lambda value: value[1], error_list_counted_sorted))[:limit]


@work_time
def most_common_words3(limit):
    """
    Get the list of most common errors

    :limit: number of errors to get
    """
    with open('C:/Users/Tanuxxx/PycharmProjects/pythonCourses/temp/python_home_work.txt') as f:
        error_list = f.read().split()

    error_list_counted = {}
    for error in error_list:
        if error not in error_list_counted:
            error_list_counted[error] = 1
        else:
            error_list_counted[error] += 1

    error_list_counted_sorted = sorted(error_list_counted, key=error_list_counted.get, reverse=True)
    return error_list_counted_sorted[:limit]


common_words = most_common_words(10)
for word in common_words:
    print(word)


common_words2 = most_common_words2(10)
for word in common_words2:
    print(word)


common_words3 = most_common_words3(10)
for word in common_words3:
    print(word)

