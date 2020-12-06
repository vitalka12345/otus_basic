my_list = [1, "spam", True, ["lox", "pidor", "net_druzey"]]
for i in my_list:
    print(i, "\n", end=" ",)


for index, elem in enumerate(my_list):
    print(index, elem)
    print("in")
print("out")
