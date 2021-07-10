# Домашнее задание номер 4 из урока 5 "Основы языка Python"
# Текст задания: 4. Представлен список чисел.
# Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
#
# Подсказка: использовать возможности python, изученные на уроке.

from time import perf_counter
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

start = perf_counter()  # вариант со списком
ex = src[0]
result = []
for el in src:
    if el > ex:
        result.append(el)
    ex = el
print(result)
print('время выполнения 2: ', perf_counter() - start, sys.getsizeof(result))