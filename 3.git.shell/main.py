from time import time
from functools import wraps
import decimal
from enum import Enum


def increase_degree(income_list, income_degree=2):
    new_list = []
    for i in income_list:
        new_list.append(pow(i, income_degree))
    return new_list


class OperationType(Enum):
    EVEN = 1
    ODD = 2
    PRIME = 3


def filter_by_operation(input_list, operation):
    output_list = []

    for _ in input_list:
        if operation == OperationType.EVEN:
            even_odd_prime_list = filter(lambda x: x % 2 == 0, input_list)
            output_list = list(set(even_odd_prime_list))
        elif operation == OperationType.ODD:
            even_odd_prime_list = filter(lambda x: x % 2 == 1, input_list)
            output_list = list(set(even_odd_prime_list))
        elif operation == OperationType.PRIME:
            even_odd_prime_list = filter(is_prime, input_list)
            output_list = list(set(even_odd_prime_list))
        else:
            print(f"Unknown type operation: {operation}")
    return output_list


def is_prime(num):
    i = 2
    while num % i != 0 and num > i:
        i += 1
    return i == num


# Time call deco
def time_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        time_taken = end - start
        print(f"Time on func \"{func.__name__}\" spent: {time_taken:.20f}")
        return res

    return wrapper


# Trace deco
def trace(func):
    func.level = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(map(lambda k, v: f"{k}={v!r}", kwargs.items()))
        func_args = list(filter(bool, (args_str, kwargs_str)))
        print("___" * func.level + f"-> {func.__name__}({', '.join(func_args)})")
        func.level += 1
        res = func(*args, **kwargs)
        func.level -= 1
        print("___" * func.level + f"<- {func.__name__}({', '.join(func_args)}) == {res}")
        return res

    return wrapper


# Fibonacci function
@trace
def fib(pos):
    if pos < 0:
        return 0
    if pos < 2:
        return 1
    return fib(pos - 1) + fib(pos - 2)


# Pow function
@time_call
def pow_funk(a, b):
    return decimal.Decimal(pow(a, b))


if __name__ == "__main__":
    random_list = range(0, 20)
    random_degree = 2
    increase_degree_result = increase_degree(random_list, random_degree)
    print(f"Degree {random_degree} list:", increase_degree_result)

    operation_list = range(-5, 20)
    odd_result = filter_by_operation(operation_list, OperationType.ODD)
    print(f"ODD {operation_list.__repr__()} list:", odd_result)

    even_result = filter_by_operation(operation_list, OperationType.EVEN)
    print(f"EVEN {operation_list.__repr__()} list:", even_result)

    prime_result = filter_by_operation(operation_list, OperationType.PRIME)
    print(f"PRIME {operation_list.__repr__()} list:", prime_result)

    print("Demonstrate trace deco:")
    fib(4)

    print("Demonstrate time call deco, result pow function = ", format(pow_funk(123456789, 12345), ".1E"))
