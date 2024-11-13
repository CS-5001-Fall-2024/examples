def func(item, list=[], name='bob'):
    list.append(item)
    return list

print(func('apple'))

print(func('banana', ['orange']))
