"""
Detailed Explanation at : https://www.geeksforgeeks.org/jump-search/
"""

from math import floor, sqrt


def jump_search1(array, target):
    # Best step value = root(n)
    step = floor(sqrt(array_len := len(array)))

    step_start = 0
    step_end = 0

    while step_start < array_len:
        step_end = min(step_start + step, array_len) 

        if array[step_end-1] > target: 
            for index in range(step_start, step_end):
                if array[index] == target:
                    return index
        else:
            step_start = step_end

    return None

def verify(index, target):
    if index is not None:
        print("Target", target, "found at index:", index)
    else:
        print("Target", target, "not in list")


array = [x for x in range(1, 51)]
print("Input array:", array)

verify(jump_search(array, 30), 30)
verify(jump_search(array, 70), 70)
