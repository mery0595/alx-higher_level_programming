#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    result = set_1 ^ set_2
    return result

set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}

result = only_diff_elements(set_1, set_2)
print(result)
