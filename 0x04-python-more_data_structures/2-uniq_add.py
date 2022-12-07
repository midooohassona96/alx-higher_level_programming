utable File  7 lines (7 sloc)  149 Bytes



#!/usr/bin/python3

def uniq_add(my_list=[]):

    new_list = set(my_list)

    result = 0

    for i in new_list:

        result += i

    return result
