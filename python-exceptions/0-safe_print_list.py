#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end=' ')
            count += i
    except IndexError:
        pass
    print()
    return count 
safe_print_list([1, 2, 3, 4], 4)      
safe_print_list([1, 2, 3, 4], 2)      
safe_print_list([1, 2, 3, 4], 0)      
safe_print_list([], 0)               
safe_print_list([1, 2, 3, 4], 5)
safe_print_list([1, 2, 3, 4], 14)
