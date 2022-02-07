import random


def max_crossing_subarray(my_array, low, mid, high):
    max_left = float('-inf')
    sum_left = 0
    index_left = low
    for i in range(mid, low , -1):
        sum_left += my_array[i]
        if sum_left > max_left:
            max_left = sum_left
            index_left =i
    max_right = float('-inf')
    sum_right = 0
    index_right = high
    for i in range(mid+1, high):
        sum_right += my_array[i]
        if sum_right > max_right:
            max_right = sum_right
            index_right =i
    return index_left, index_right, max_left+max_right


def maximum_subarray(my_array, low, high):
    if low == high:
        return low, high, my_array[low]
    else:
        mid = (low + high) // 2
        left_answer = maximum_subarray(my_array, low, mid)
        right_answer = maximum_subarray(my_array, mid+1, high)
        cross_answer =max_crossing_subarray(my_array, low, mid, high)
        if left_answer[2] >= right_answer[2] and left_answer[2] >= cross_answer[2]:
            return left_answer
        elif right_answer[2] >= left_answer[2] and right_answer[2] >= cross_answer[2]:
            return right_answer
        else:
            return cross_answer


# my_list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# Generate 10 random numbers between 10 and 30
my_list = random.sample(range(10, 30), 10)
print('initial list \n', my_list)
print(maximum_subarray(my_list, 0, len(my_list)-1))

