# def greet_names():
#     # for name in names:
#     #     print("Hello", name.title())
#     while names:
#         name = names.pop()
#         print("Hello", name.title())
#
#
# names = ["sam", "nick", "john"]
# print("names:", names)
# # greet_names(names)
# print("names", names)
#
#
# def filter_names(names, max_len=3):
#     result = []
#     for name in names[:]:
#         if len(name) <= max_len:
#             names.append(name)
#     return result
#
#
# filter_names = filter_names(names, 1)

from time import time
from functools import wraps


def fib(pos):
    """
    1, 2, 3, 5, 8
    1 = 1 + 0
    2 = 1 + 1
    3 = 2 + 1
    5 = 3 + 2
    8 = 5 + 3 ||  8 = (3 + 2) + 3 || 8 = ((2 + 1) + 2) + (2 + 1)
    :param pos:
    :return:
    """
    if pos <= 1:
        return 1
    return fib(pos - 1) + fib(pos - 2)


fib_nums = []
for i in range(1, 5):
    fib_nums.append((fib(i)))

# print(fib_nums)
# print([fib(i) for i in range(30)])

fib_nums = []
for i in range(3):
    print("pos", 1)
    start = time()
    res = fib(i)
    end = time()
    fib_nums.append(res)
    print("res for", i, " = ", res)
    time_taken = end - start
    print(f"time taken: {time_taken: .13f}")


def time_call(func):
    # print("incoming func:", func)

    @wraps(func)
    def wrapper(p):
        start = time()
        res = func(p)
        end = time()
        print("res for", p, " = ", res)
        time_taken = end - start
        print(f"time taken: {time_taken: .13f}")
        return func(p)

    print(wrapper.__wrapped__)
    print(id(wrapper))
    print(id(func))
    print(id(wrapper.__wrapped__))
    return wrapper


t_call = time_call

timed_fib = t_call(fib)
print("create new func")
print(timed_fib(30))
