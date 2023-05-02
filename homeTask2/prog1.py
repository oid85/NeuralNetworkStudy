"""
Задание 1.
Дано натуральное число. Определить:
1) количество цифр 4 в нём;
2) сколько раз в нём встречается последняя цифра;
3) количество чётных цифр в нём;
4) сумму его цифр больше 5;
5) сколько раз в нём встречаются цифра 0 и 5 (всего);
6) Произведение его цифр, больших 7;
"""

number = int(input("Введите натуральное число:"))

countOfDigit4 = 0
countOfLastDigit = 0
countOfEvenDigit = 0
sumOfDigitMore5 = 0
countOfDigit0and5 = 0
multOfDigitMore7 = 1

lastDigit = number % 10

while number > 0:
    digit = number % 10

    # Количество цифр 4
    if digit == 4:
        countOfDigit4 = countOfDigit4 + 1

    # Cколько раз встречается последняя цифра
    if digit == lastDigit:
        countOfLastDigit = countOfLastDigit + 1

    # Количество чётных цифр
    if digit % 2 == 0:
        countOfEvenDigit = countOfEvenDigit + 1

    # Сумма цифр больше 5
    if digit > 5:
        sumOfDigitMore5 = sumOfDigitMore5 + digit

    # Количество цифр 0 и 5
    if digit == 0 or digit == 5:
        countOfDigit0and5 = countOfDigit0and5 + 1

    # Произведение цифр больше 7
    if digit > 7:
        multOfDigitMore7 = multOfDigitMore7 * digit

    number = number // 10

print(f'Количество цифр 4 - {countOfDigit4}')
print(f'Последняя цифра {(lastDigit)} встречается {countOfLastDigit} раз')
print(f'Количество чётных цифр - {countOfEvenDigit}')
print(f'Сумма цифр больше 5 - {sumOfDigitMore5}')
print(f'Цифры 0 и 5 встречаются {countOfDigit0and5} раз')

if multOfDigitMore7 == 1:
    print(f'Цифры 7 в числе нет')
else:
    print(f'Произведение цифр больше 7 - {multOfDigitMore7}')
