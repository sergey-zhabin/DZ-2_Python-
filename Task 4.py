# 5 Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result = random.sample(list, len(list))
print ('\n', str(list), ' получаем случайный список ', str(result), '\n')