from time import time
from functools import wraps
# import trace

# Degree function
random_list = range(0, 20)
random_degree = 2


def degree_func(income_list, income_degree=2):
    new_list = []
    for i in income_list:
        new_list.append(pow(i, income_degree))
    print('Degree list:', new_list)


degree_func(random_list, random_degree)

# Even, Odd, Prime function.
operation_list = range(-5, 20)


def even_odd_prime_numbers_function(list1, op_type=None):
    if op_type is None:
        op_type = str(input("You can choose one of 3 types (even, odd, prime):"))
    else:
        pass
    count_elem = len(operation_list)
    even_odd_prime_list = []
    for n in range(count_elem):
        if op_type == 'EVEN':
            even_odd_prime_list = filter(lambda x: x % 2 == 0, operation_list)
            returned_list = list(set(even_odd_prime_list))
        elif op_type == 'ODD':
            even_odd_prime_list = filter(lambda x: x % 2 == 1, operation_list)
            returned_list = list(set(even_odd_prime_list))
        elif op_type == 'PRIME':
            even_odd_prime_list = filter(is_prime, operation_list)
            returned_list = list(set(even_odd_prime_list))
    print(f"{op_type} list:", returned_list)


def is_prime(n):
    d = 2
    while n % d != 0 and n > d:
        d += 1
    return d == n


even_odd_prime_numbers_function(operation_list, 'PRIME')


# - создать декоратор для замера времени выполнения функции
# 2.
# БОНУСНОЕ ЗАДАНИЕ: создать декоратор, который показывает вложенные входы в функцию.
# Применить на примере вычисления чисел Фибоначчи
# https://gist.github.com/mahenzon/d77361a1bd44f138e706ae4734007ee6
# сложить это всё в один файл. В файле написать код, который продемонстрирует работу всех функций выше.
# Красивые принты приветствуются. Подсказка: можно воспользоваться модулем pprint
# - создание декоратора для замера времени выполнения функции - 1 балл
# внутри обёртки используется wraps из functools
# декоратор trace - 1 балл
# написана функция для вычисления чисел Фибоначчи
# функция для вычисления чисел Фибоначчи использует рекурсию
# обёртка работает и показывает погружения
# для всех написанных функций есть пример их работы - 1 балл
# данные выводятся красиво и понятно - 1 балл


def time_call(func):
    print("incoming func:", func.__name__)

    @wraps(func)
    def wrapper(p):
        start = time()
        res = func(p)
        end = time()
        print("res for", p, " = ", res)
        time_taken = end - start
        print(f"time taken: {time_taken:.13f}")
        return res

    # print("id   wrapper", id(wrapper))
    # print(wrapper.__wrapped__)
    # print(id(wrapper))
    # print(id(func))
    # print(id(wrapper.__wrapped__))
    return wrapper


def trace(func):
    count = 1

    @wraps(func)
    def wrapper1(d):
        count += 1
        res = func(d)
        print(f"when {type(res)} returned, count = " + str(count))
        return wrapper1


# @trace
@time_call
def fib(pos):
    """
    1, 1, 2, 3, 5, 8
    1 = 1
    2 =  1
    3 =  1
    5 =  2  || (2 + 1) + 2
    8 =  3  || 8 = (3 + 2) + 3 || 8 = ((2 + 1) + 2) + (2 + 1)
    :param pos:
    :return:
    """
    if pos <= 1:
        return 1
    return fib(pos - 1) + fib(pos - 2)


fib(5)
