import random
from algorithm_implementation.sort.quick_sort import quick_sort, partition


def select(my_array, p, r, i):
    if p == r:
        return my_array[p]
    q = partition(my_array, p, r)
    k = q - p + 1
    if k == i:
        return my_array[q]
    elif i < k:
        return select(my_array, p, q-1, i)
    else:
        return select(my_array, q+1, r, i-k)


if __name__ == '__main__':
    # Generate 10 random numbers between -10 and 10
    my_array = random.sample(range(-10, 10), 10)
    print('initial list \n', my_array)
    key = 4
    value = select(my_array, 0, len(my_array)-1, key)
    print('key selection --> A[%d] = %d ' % (key, value))
    quick_sort(my_array, 0, len(my_array)-1)
    print('sorted list \n', my_array)

