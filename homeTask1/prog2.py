"""
Написать программу для сравнения трёх чисел
Ввод: числа вводит пользователь с клавиатуры
Вывод: число, которое больше одного, но меньше второго (т.е. вводится среднее число из трёх)
"""

print('Введите, пожалуйста, 1-е число:')
inputData1 = input()

print('Введите, пожалуйста, 2-е число:')
inputData2 = input()

print('Введите, пожалуйста, 3-е число:')
inputData3 = input()

number1 = float(inputData1)
number2 = float(inputData2)
number3 = float(inputData3)

numberList = [number1, number2, number3]

numberList.sort()

middleNumber = numberList[1]

print('Среднее число из трех:')
print(middleNumber)
