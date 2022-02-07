import random


def insertion_sort(initial_list):
    list_len = len(initial_list)

    for j in range(1, list_len):
        key = initial_list[j]
        i = j - 1

        while i > -1 and initial_list[i] > key:
            initial_list[i + 1] = initial_list[i]
            i -= 1

        initial_list[i + 1] = key

    return initial_list


if __name__ == "__main__":
    # Generate 10 random numbers between 10 and 30
    random_list = random.sample(range(10, 30), 10)
    print('initial list \n', random_list)
    sorted_list = insertion_sort(random_list)
    print('sorted list \n', sorted_list)

