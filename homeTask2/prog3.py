"""
Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]. Выведите все элементы, которые меньше 5.
"""

# Способ 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for item in a:
    if item < 5:
        print(item)

# Способ 2
print('\n')
filtered = filter(lambda item: item < 5, a)
print(list(filtered))
