# 1 Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы

import timeit
code_to_test = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
factorial(5)                
"""

elapsed_time =  timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)




code_to_test = """
def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n
fac(5)    
"""

elapsed_time =  timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)



code_to_test = """
def factorial_gen(n):
    if n == 0:
        yield 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
            yield result
result = list(factorial_gen(5))
"""

elapsed_time =  timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)

# 2 Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:


def typed(type):
    def decorator(func):
        def wrapper(*args):
            converted_args = []
            for i in args:
                if isinstance(i, type):
                    converted_args.append(i)
                else:
                    converted_args.append(type(i))
            return func(*converted_args)
        return wrapper
    return decorator

@typed(str)
def add_two_symbols(a, b):
    return a + b

print(add_two_symbols(3, "5"))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))

@typed(int)
def add_three_symbols(a, b, c):
    return a + b + c

@typed(float)
def add_three_float(a, b, c):
    return a + b + c

print(add_three_symbols(5, 6, 7))
print(add_three_symbols('3', 5, 0))
print(add_three_float(0.1, 0.2, 0.4))


