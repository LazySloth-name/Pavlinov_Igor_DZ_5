# Домашнее задание номер 5 из урока 5 "Основы языка Python"
# Текст задания: 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка
# их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()  #перебор уникальных значений
result = [el for el in set(src) if src.count(el) == 1]
print(result)
print('время выполнения 1: ', perf_counter() - start)