"""
В этой задаче, Вам нужно создать функцию проверки пароля
Условия проверки:
длина пароля должна быть больше 6
Входные данные: Строка
Выходные данные: Логический тип
"""


def checkPassword(password):
    # Проверка длины
    if len(password) <= 6:
        return False
    return True


def checkPasswordSuper(password):
    if not checkPassword(password):
        return False

    # Проверка наличия цифр
    if not any(map(str.isdigit, password)):
        return False

    return True


def checkPasswordUltra(password):
    if not checkPasswordSuper(password):
        return False

    # Проверка наличия символов в верхнем регистре
    if not any(map(str.isupper, password)):
        return False

    # Проверка наличия символов в нижнем регистре
    if not any(map(str.islower, password)):
        return False

    # Проверка наличия спецсимволов
    if password.find('!') != 1 or \
            password.find('@') != 1 or \
            password.find('$') != 1 or \
            password.find('%') != 1 or \
            password.find('^') != 1 or \
            password.find('&') != 1 or \
            password.find('*') != 1 or \
            password.find('(') != 1 or \
            password.find(')') != 1:
        return False

    return True


passwordForCheck = "QwesdfQWs"
print(f'Simple check: {checkPassword(passwordForCheck)}')
print(f'Super check: {checkPasswordSuper(passwordForCheck)}')
print(f'Ultra check: {checkPasswordUltra(passwordForCheck)}')
