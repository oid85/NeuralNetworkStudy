"""
Найти:
а) сумму кубов всех целых чисел от 20 до 40;
б) сумму квадратов всех целых чисел от а до 50 (значение а вводится с клавиатуры: 0 ≤ а≤ 50);
в) сумму квадратов всех целых чисел от 1 до n (значение и вводится с клавиатуры; 1 ≤ n ≤ 100);
г) сумму квадратов всех целых чисел от а до b (значения а и b вводятся с клавиатуры; b ≥ а).
"""


def sumNumbersInPow(begin, end, p):
    sum = 0
    indexes = range(begin, end)
    for i in indexes:
        sum = sum + (i ** p)

    return sum


print('\n а). Cумма кубов всех целых чисел от 20 до 40')
result = sumNumbersInPow(20, 40, 3)
print(result)

print('\n б). Cумма квадратов всех целых чисел от а до 50')
print('Введите число a (0 ≤ а≤ 50):')
a = int(input())

if 0 <= a <= 50:
    result = sumNumbersInPow(a, 50, 2)
    print(result)
else:
    print('Данные введены неверно')

print('\n в). Cумма квадратов всех целых чисел от 1 до n')
print('Введите число n (1 ≤ n ≤ 100):')
n = int(input())
if 1 <= n <= 100:
    result = sumNumbersInPow(1, n, 2)
    print(result)
else:
    print('Данные введены неверно')

print('\n г). Cумма квадратов всех целых чисел от а до b')
print('Введите число a:')
a = int(input())
print('Введите число b (b ≥ а):')
b = int(input())

if b >= a:
    result = sumNumbersInPow(a, b, 2)
    print(result)
else:
    print('Данные введены неверно')



