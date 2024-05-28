# 1 Напишите функцию is_year_leap, которая принимает число (год) и возвращает true, если год високосный false если нет.

from core.is_year import is_year_leap


print(is_year_leap(1200))

# 2 Напишите функцию generate_natural_cubes(n), которая принимает число n и возвращает список, состоящий из кубов первых
# n натуральных чисел. То есть [1**3, 2**3, 3**3, ..., n**3]. Обязательно использование генераторов списков.



def generate_natural_cubes(n):
    return [i**3 for i in range(1, n+1)]


n = 5
print(generate_natural_cubes(n))



# 3 Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список,
# состоящий из их квадратов.Тоесть generate_squares(1, 2, 3) -> [1, 4, 9]


def generate_squares(*args):
    for i in args:
        i**2


print(generate_squares(1, 2, 3))

# 4 Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы), и возвращает
# самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.



def get_longest_word(text):
     word = text.split()
     get_longest_word = max(word,key = len)
     return get_longest_word


text = 'Hello my name is Vseslav , I am from Belarus'
print(get_longest_word(text))