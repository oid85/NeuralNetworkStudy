"""
Написать программу для перевода килобайт в байты, байты в килобайты
Ввод: Номер операции, а также число, которое вводит пользователь с клавиатуры
Вывод: текстовая строка с числом и указанием единиц измерения
"""

print('Конвертер единиц измерения объема информации')
print('\n')
print('1. килобайт => байт')
print('2. байт => килобайт')
print('Выберите операцию (1 или 2):')

inputData = input()

convertOperation = int(inputData)

if convertOperation == 1:
    print('Введите кол-во килобайт:')
    kbInputData = input()
    kb = float(kbInputData)
    b = kb * 1024
    print(f'{kb} килобайт = {b} байт')

elif convertOperation == 2:
    print('Введите кол-во байт:')
    bInputData = input()
    b = float(bInputData)
    kb = b / 1024
    print(f'{b} байт = {kb} килобайт')

else:
    print('Операция не выбрана')
