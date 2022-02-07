
def binary_search(my_list, element, low, high):
    if low <= high:
        mid = (low + high) // 2
        if my_list[mid] == element:
            return mid
        elif my_list[mid] > element:
            return binary_search(my_list, element, low, mid-1)
        else:
            return binary_search(my_list, element, mid+1, high)

    else:
        return -1


my_list = [1, 4, 6, 8, 11, 17, 20, 26, 30, 31, 39, 40, 42, 50]
print(binary_search(my_list, 8, 0, len(my_list)-1))

