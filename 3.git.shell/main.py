from time import time
from functools import wraps
import decimal

# Degree function
random_list = range(0, 20)
random_degree = 2


def degree_func(income_list, income_degree=2):
    new_list = []
    for i in income_list:
        new_list.append(pow(i, income_degree))
    print(f"Degree {income_degree} list:", new_list)


# Even, Odd function
operation_list = range(-5, 20)


def even_odd_prime_numbers_function(list1, op_type=None):
    if op_type is None:
        op_type = str(input("You can choose one of 3 types (even, odd, prime):"))
    else:
        pass
    count_elem = len(operation_list)
    even_odd_prime_list = []
    for n in range(count_elem):
        if op_type == "EVEN":
            even_odd_prime_list = filter(lambda x: x % 2 == 0, operation_list)
            returned_list = list(set(even_odd_prime_list))
        elif op_type == "ODD":
            even_odd_prime_list = filter(lambda x: x % 2 == 1, operation_list)
            returned_list = list(set(even_odd_prime_list))
        elif op_type == "PRIME":
            even_odd_prime_list = filter(is_prime, operation_list)
            returned_list = list(set(even_odd_prime_list))
    print(f"{op_type} {operation_list.__repr__()} list:", returned_list)


# Prime function
def is_prime(n):
    d = 2
    while n % d != 0 and n > d:
        d += 1
    return d == n


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
def trace(func1):
    func1.level = 0

    @wraps(func1)
    def wrapper1(*args, **kwargs):
        args_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(map(lambda k, v: f"{k}={v!r}", kwargs.items()))
        func_args = list(filter(bool, (args_str, kwargs_str)))
        print("___" * func1.level + f"-> {func1.__name__}({', '.join(func_args)})")
        func1.level += 1
        res = func1(*args, **kwargs)
        func1.level -= 1
        print("___" * func1.level + f"<- {func1.__name__}({', '.join(func_args)}) == {res}")
        return res

    return wrapper1


@trace
def fib(pos):
    if pos < 0:
        return None
    if pos < 2:
        return 1
    return fib(pos - 1) + fib(pos - 2)


# Pow function
@time_call
def pow_funk(a, b):
    return decimal.Decimal(pow(a, b))


if __name__ == "__main__":
    degree_func(random_list, random_degree)
    even_odd_prime_numbers_function(operation_list, "ODD")
    even_odd_prime_numbers_function(operation_list, "EVEN")
    even_odd_prime_numbers_function(operation_list, "PRIME")
    print("Demonstrate trace deco:")
    fib(4)
    # print("Demonstrate time call deco pow func = ", pow_funk(123456789, 12345))
    print("Demonstrate time call deco, result pow function = ", format(pow_funk(123456789, 12345), ".1E"))
