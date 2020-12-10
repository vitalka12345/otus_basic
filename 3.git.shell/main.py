# Degree function
random_list = [1, 2, 3, 4]
random_degree = 2


def degree_func(income_list, income_degree=4):
    new_list = []
    for i in income_list:
        new_list.append(pow(i, income_degree))
    print(new_list)


# degree_func(random_list, random_degree)

# Failed degree function
rand_list = [1, 2, 3, 4]
rand_degree = 2


def rand_degree_func(income_list, income_degree=4):
    print(list(map(lambda dgr1: pow(dgr1, income_degree), income_list)))


rand_degree_func(rand_list, rand_degree)

# TypeError: 'int' object is not callable
