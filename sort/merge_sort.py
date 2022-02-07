import random


class MergeSort:

    def __init__(self):
        self.positive_infinity = float('inf')

    def merge_sort(self, initial_list, start, end):
        if start < end:
            mid = (start + end) // 2
            self.merge_sort(initial_list, start, mid)
            self.merge_sort(initial_list, mid+1, end)
            self.merge(initial_list, start, mid, end)

        return initial_list

    def merge(self,initial_list, start, mid, end):
        left = []
        right = []

        for i in range(start, mid+1):
            left.append(initial_list[i])
        left.append(self.positive_infinity)

        for j in range(mid+1, end+1):
            right.append(initial_list[j])
        right.append(self.positive_infinity)

        i, j = 0, 0
        for k in range(start, end+1):
            if left[i] < right[j]:
                initial_list[k] = left[i]
                i += 1
            else:
                initial_list[k] = right[j]
                j += 1


if __name__ == "__main__":
    # Generate 10 random numbers between 10 and 30
    random_list = random.sample(range(10, 30), 10)
    print('initial list \n',random_list)
    obj = MergeSort()
    sorted_list = obj.merge_sort(random_list, 0, len(random_list)-1)
    print(len(random_list))
    print('sorted list \n', sorted_list)