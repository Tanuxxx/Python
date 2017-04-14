def get_uniq(*args):
    uniq_elementes = set()
    for item in args:
        # if item not in uniq_elementes:
        #     uniq_elementes.add(item)
        uniq_elementes.add(item)
    return uniq_elementes


def get_uniq1(*args):
    return set(args)

print(get_uniq1(1,3,5,7,5,3,8,9,8,9,1))