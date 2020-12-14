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
