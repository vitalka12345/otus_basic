def dgr_func(degree=2):
    my_list = []
    if degree is None:
        degree = int(input("Enter wanted degree:"))
    else:
        pass
    number = int(input("Enter numbers type(int), which you want added to dgr_list.\nEnter 0 to complete entering:\n"))
    while number != 0:
        my_list.append(number)
        number = int(input("Enter numbers type(int), which you want added to dgr_list.\nEnter 0 to complete entering:\n"))
    count_elem = len(my_list)
    print("len of entered_list:", count_elem)
    print("list", my_list)
    dgr_list = []
    for n in range(count_elem):
        dgr_list.append(my_list[n] ** degree)
    print("degree list:", dgr_list)


dgr_func(None)
