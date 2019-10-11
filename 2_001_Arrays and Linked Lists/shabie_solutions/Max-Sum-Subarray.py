def find_largest_sub(arr):
    so_far_largest = 0
    largest_to_this_element = 0

    for i in arr:
        largest_to_this_element += i
        if largest_to_this_element < 0:
            largest_to_this_element = 0
        elif so_far_largest < largest_to_this_element:
            so_far_largest = largest_to_this_element

    return so_far_largest


print(find_largest_sub([-2, -3, 4, -1, -2, -1, -5, -3]))
