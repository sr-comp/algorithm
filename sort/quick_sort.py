import random


def quick_sort(my_array, p, r):
    if p < r:
        q = partition(my_array, p, r)
        quick_sort(my_array, p, q-1)
        quick_sort(my_array, q+1, r)


def partition(my_array, p, r):
    rnd = random.randint(p, r)
    temp = my_array[rnd]
    my_array[rnd] = my_array[r]
    my_array[r] = temp
    x = my_array[r]
    i = p - 1
    for j in range(p, r):
        if my_array[j] <= x:
            i += 1
            temp = my_array[i]
            my_array[i] = my_array[j]
            my_array[j] = temp
    i += 1
    temp = my_array[r]
    my_array[r] = my_array[i]
    my_array[i] = temp
    return i


if __name__ == '__main__':
    # Generate 10 random numbers between -10 and 10
    my_array = random.sample(range(-10, 10), 10)
    print('initial list \n', my_array)
    quick_sort(my_array, 0, len(my_array)-1)
    print('sorted list \n', my_array)

