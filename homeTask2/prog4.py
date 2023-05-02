"""
Даны списки: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]; b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
Нужно вернуть все элементы, которые хотя бы раз встречаются в обоих списках.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Сложим списки в один
ab = [*a, *b]

print(ab)

# Если элемент встречается в первом и втором списке хотябы один раз,
# то в общем списке он должен встретиться минимум 2 раза

result = set() # Будем складывать во множество, чтобы убрать дубликаты

for item in ab:
    if ab.count(item) >= 2:
        result.add(item)

print(list(result))