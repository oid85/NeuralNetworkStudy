"""
Создайте и наполните значениями список целых чисел, кортеж строк,
множество чисел с плавающей точкой, и словарь, ключами которого служат числа, а значениями – строки
Выведите все эти объекты на экран
Выполните слияние списка и множества, выведите результат на экран
Выполните преобразование списка во множество, выведите результаты на экран
"""

import random
import uuid

from random import randint

# Создать, наполнить и вывести на экран список целых чисел
print('\n Подзадача 1')
count = 10  # Размер списка
indexes = range(count)
intNumberList = []

for i in indexes:
    randomIntNumber = randint(0, count * 10)
    intNumberList.append(randomIntNumber)

print(f'Cписок целых чисел ({len(intNumberList)} элементов):')
print(intNumberList)

# Создать, наполнить и вывести на экран кортеж строк
print('\n Подзадача 2')
count = 3  # Размер кортежа
indexes = range(count)
stringList = []

for i in indexes:
    randomString = str(uuid.uuid4())
    stringList.append(randomString)

# Создаем кортеж из списка
stringTuple = tuple(stringList)

print(f'Кортеж строк (размер кортежа - {len(stringTuple)}):')
print(stringTuple)

# Создать, наполнить и вывести на экран множество чисел с плавающей точкой
print('\n Подзадача 3')
count = 10  # Размер множества
indexes = range(count)
floatNumberSet = set()

for i in indexes:
    randomFloatNumber = randint(0, count * 10) / 10.0
    floatNumberSet.add(randomFloatNumber)

print(f'Множество чисел с плавающей точкой ({len(floatNumberSet)} элементов):')
print(floatNumberSet)

# Создать, наполнить и вывести на экран словарь, ключами которого служат числа, а значениями – строки
print('\n Подзадача 4')
count = 5  # Размер словаря
indexes = range(count)

intStringDictionary = dict()

for i in indexes:
    randomIntKey = randint(0, count * 10)
    randomStringValue = str(uuid.uuid4())
    intStringDictionary[randomIntKey] = randomStringValue

print(f'Cловарь, ключами которого служат числа, а значениями – строки ({len(intStringDictionary)} элементов):')
print(intStringDictionary)

# Выполните слияние списка и множества, выведите результат на экран
print('\n Подзадача 5')

newList = intNumberList + list(floatNumberSet)

print(f'Результат слияния ранее созданных списка и множества ({len(newList)} элементов):')
print(intNumberList)
print('+')
print(floatNumberSet)
print('=>')
print(newList)


# Выполните преобразование списка во множество, выведите результаты на экран
print('\n Подзадача 6')

newSet = set(intNumberList)

print(f'Результат преобразование ранее созданного списка во множество ({len(newSet)} элементов):')
print(intNumberList)
print('=>')
print(newSet)
