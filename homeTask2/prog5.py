"""
Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
(отвечающий за добавку к выбираемому лимонаду)
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
а иначе отобразится следующая фраза: «Обычная газировка»
"""


class Soda:
    def __init__(self, drink_additive=None):
        self.drink_additive = drink_additive

    def show_my_drink(self):
        if self.drink_additive:
            return f'Газировка и {self.drink_additive}'
        else:
            return 'Обычная газировка'


drink = Soda()
drinkName = drink.show_my_drink()
print(drinkName)

drink = Soda('клубничный сироп')
drinkName = drink.show_my_drink()
print(drinkName)

drink = Soda('ром')
drinkName = drink.show_my_drink()
print(drinkName)
