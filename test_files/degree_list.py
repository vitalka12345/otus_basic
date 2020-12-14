# def dgr_func(degree=2):
#     my_list = []
#     if degree is None:
#         degree = int(input("Enter wanted degree:"))
#     else:
#         pass
#     number = int(input("Enter numbers type(int), which you want added to dgr_list.\nEnter 0 to complete entering:\n"))
#     while number != 0:
#         my_list.append(number)
#         number = int(
#             input("Enter numbers type(int), which you want added to dgr_list.\nEnter 0 to complete entering:\n"))
#     count_elem = len(my_list)
#     print("len of entered_list:", count_elem)
#     print("list", my_list)
#     dgr_list = []
#     for n in range(count_elem):
#         dgr_list.append(my_list[n] ** degree)
#     print("degree list:", dgr_list)
#
#
# dgr_func(None)


def degree_func(degree=2):
    my_list = [1, 2, 3, 4]
    degree_list = []
    for i in my_list:
        degree_list.append(i ** degree)
    print(degree_list)


degree_func(int(input("Enter wanted degree:")))

# Failed degree function
rand_list = [1, 2, 3, 4]
rand_degree = 2


def rand_degree_func(income_list, income_degree=4):
    print(list(map(lambda dgr1: pow(dgr1, income_degree), income_list)))


# rand_degree_func(rand_list, rand_degree)

# TypeError: 'int' object is not callable
