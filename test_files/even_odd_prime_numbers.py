def even_odd_prime_numbers_func(op_type):
    my_list = range(-4, 20)
    if op_type is None:
        op_type = str(input("You can choose one of 3 types (even, odd, prime):"))
    else:
        pass
    # number = int(input("Enter numbers type(int), which you want added to even_odd_prime_list.\nEnter 0 to complete "
    #                    "entering:\n"))
    # while number != 0:
    #     my_list.append(number)
    #     number = int(input("Enter numbers type(int), which you want added to even_odd_prime_list.\nEnter 0 to "
    #                        "complete entering:\n"))
    count_elem = len(my_list)
    print("len of entered_list:", count_elem)
    print("entered_list", my_list)
    even_odd_prime_list = []
    for n in range(count_elem):
        if op_type == 'even':
            even_odd_prime_list = filter(lambda x: x % 2 == 0, my_list)
            # if my_list[n] % 2 == 0:
            #     even_odd_prime_list.append(my_list[n])
            # else:
            #     pass
        elif op_type == 'odd':
            if my_list[n] % 2 == 1:
                even_odd_prime_list.append(my_list[n])
            else:
                pass
        elif op_type == 'prime':
            if my_list[n] == 2:
                even_odd_prime_list.append(my_list[n])
            elif my_list[n] > 1:
                for i in range(2, my_list[n]):
                    if my_list[n] % i == 0:
                        break
                    else:
                        even_odd_prime_list.append(my_list[n])
            else:
                pass
    my_distinct_list = list(set(even_odd_prime_list))
    print(f"{op_type} list:", my_distinct_list)


even_odd_prime_numbers_func('even')

# my_list = [1, 2, 3, 4, 5]
# filter(my_list, )

# if my_list[n] > 1:
#     for i in range(2, my_list[n]):
#         if (my_list[n] % i) == 0:
#             pass
#         else:
#             even_odd_prime_list.append(my_list[n])


# if my_list[n] > 1:
#     for i in range(2, my_list[n]):
#         if my_list[n] % i == 0:
#             break
#         else:
#             even_odd_prime_list.append(my_list[n])
