#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += i
    except IndexError:
        pass
    print()
    return count
safe_print_list([1, 2, 3], 5)
