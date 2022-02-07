
class Heap:
    heap_array = []
    heap_size = 0

    def __init__(self, value, size):
        self.heap_array = value
        self.heap_size = size
        self.build_max_heap()

    def parent(self, i):
        return ((i + 1) // 2) - 1

    def left(self, i):
        return 2 * i + 1   # 2 * (parent + 1) - 1

    def right(self, i):
        return 2 * (i + 1)  # (2 * (parent + 1) + 1) - 1

    def max_heapify(self, i):
        largest = self.heap_array[i]
        ind_largest = i
        if self.left(i) < self.heap_size and self.heap_array[self.left(i)] > largest:
            largest = self.heap_array[self.left(i)]
            ind_largest = self.left(i)
        if self.right(i) < self.heap_size and self.heap_array[self.right(i)] > largest:
            largest = self.heap_array[self.right(i)]
            ind_largest = self.right(i)
        if ind_largest != i:
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[ind_largest]
            self.heap_array[ind_largest] = temp
            self.max_heapify(ind_largest)

    def build_max_heap(self):
        last_node = self.heap_size - 1
        for i in range(self.parent(last_node), -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        temp_array = self.heap_array.copy()
        for i in range(self.heap_size-1, 0, -1):
            temp = self.heap_array[0]
            self.heap_array[0] = self.heap_array[i]
            self.heap_array[i] = temp
            self.heap_size -= 1
            self.max_heapify(0)
        sorted_array = self.heap_array.copy()
        self.heap_array = temp_array
        self.heap_size = len(temp_array)
        return sorted_array

    def extract_max(self):
        item = self.heap_array[0]
        self.heap_array[0] =self.heap_array[self.heap_size-1]
        self.heap_size -= 1
        self.max_heapify(0)
        return item



if __name__ == '__main__':
    heap = [1, 7, 2, 4, 8, 14, 9, 3, 10, 16]
    heap_obj = Heap(heap, len(heap))
    print(heap_obj.heap_array)
    print(heap_obj.heap_sort())
    print(heap_obj.extract_max())
    print(heap_obj.heap_array)
    print(heap_obj.heap_size)

