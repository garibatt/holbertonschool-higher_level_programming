#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_add = []
    for i in my_list:
        if i not in unique_add:
            unique_add.append(i)
    return sum(unique_add)
