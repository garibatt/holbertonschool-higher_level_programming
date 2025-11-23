#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            if my_list[i] == int(my_list[i]):
                print("{:d}".format(my_list[i]), end="")
                counter += 1
        except (ValueError, TypeError):
            pass
    print()
    return counter
