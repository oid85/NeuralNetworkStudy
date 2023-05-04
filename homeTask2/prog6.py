"""
Дана строка и нужно найти ее первое слово
Строка состоит только из английских символов и пробелов
В начале и в конце строки пробелов нет
Входные данные: строка
Выходные данные: строка
"""

import random

# Задаем словарь из возможных слов
words = ["dog", "cat", "car", "house", "book", "comp", "pen"]

# Случайное предложение
inputString = f'{random.choice(words)} {random.choice(words)} {random.choice(words)} {random.choice(words)} {random.choice(words)}'

print(f'Сгенерированное предложение:')
print(inputString)

firstWord = inputString.split()[0]

print(f'Первое слово в предложении: {firstWord}')
