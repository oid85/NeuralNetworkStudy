"""
Создайте свой пакет под названием CalcLib, реализуйте в нем функцию расчета n-го числа последовательности Фибоначчи.
Создайте вложенный подпакет CalcLib.call в котором реализуйте вызов функции из основного пакета.
Подключите данный пакет в основной файл и вызовите функцию call
"""

from matplotlib import pyplot as plt

from CalcLib.call.call_fibonacci import call

# Выведем первые N элементов последовательности Фибоначчи
N = 25
indexes = range(1, N)
fibonacci_elements = []

for i in indexes:
    fibonacci_elements.append(call(i))

print(f'Первые {N} элементов последовательности Фибоначчи:')
print(*fibonacci_elements)

# Чтобы было красиво, попробуем посмотреть визуально, как выглядит последовательность Фибоначчи
plt.plot(indexes, fibonacci_elements)
plt.show()
