# Произвольное количество позиционных аргументов
def hi_all(*names):
    for name in names:
        print(f'Hi, {name}!!!')

print('Произвольное количество позиционных аргументов')
hi_all('Alex', 'John', 'Tim')


# Произвольное количество именованных аргументов
def get_weather(**params):
    for param in params:
        print(param, ":", params[param])


print('\n')
print('Произвольное количество именованных аргументов')
get_weather(**{'Температура': '25 град.', 'Давление': '760 мм. рт. ст', 'Ветер': '1-2 м/с'})

# Упаковка и распаковка коллекций
print('\n')
print('Упаковка и распаковка коллекций')

*a, b = 1, 2, 3
print(a, b)

a = 1, 5
print(list(range(*a)))
print([*range(*a)])
print([*range(*a), *['asd', True, 456]])

a, b = (1, 2)
print(a, b)

a, *b = (1, 2, 3, 4, 5)
print(a, b)

a, *b = [1, 2, 3, 4, 5]
print(a, b)

*a, b, c = {1, 2, 3, 4, 5}
print(a, b, c)

dict1 = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров'}
print(*dict1)
print({*dict1})

dict2 = {4: 'Смирнов', 5: 'Сергеев', 6: 'Дмитриев'}
print({**dict1, **dict2})
