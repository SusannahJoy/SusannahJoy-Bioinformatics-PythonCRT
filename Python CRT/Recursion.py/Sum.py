'''
Write a python program to print the summation of list elements using recursion

Syntax for recursion-
def function_name(parameters):
        if base_condition:
            return result
        return function_name(modified_parameters)
'''

def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])