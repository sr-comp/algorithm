from algorithm_implementation.sort.insertion_sort import insertion_sort
import random

def bucket(interval_min, interval_max, num, value):
    length = interval_max - interval_min
    step = length / num
    return int((value - interval_min) // step)


def bucket_sort(my_array, interval_min, interval_max):
    n = len(my_array)
    b = []
    for j in range(0, n):
        b.append([])
    for element in my_array:
        b[bucket(interval_min, interval_max, n, element)].append(element)
    for j in range(0, n):
        b[j] = insertion_sort(b[j])
    i = -1
    for j in range(0, n):
        for element in b[j]:
            i += 1
            my_array[i] = element
    return my_array


if __name__ == '__main__':
    my_array = [90, 53, 67, 40, 47, 45, 12, 23, 97, 2, 7]
    print('initial list \n', my_array)
    sorted_list = bucket_sort(my_array, 0, 100)
    print('sorted list \n', sorted_list)





